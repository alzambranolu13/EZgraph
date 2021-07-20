from collections import deque
import queue

class UndirectedGraph:
    def __init__( self , numberOfNodes ):
        self.nodes = numberOfNodes
        self.adjacencyList = []
        self.numberOfEdges = 0
        for i in range(numberOfNodes):
            self.adjacencyList.append( [] )

    def addEdge( self , node1 , node2 ):
        for edge in self.adjacencyList[node1]:
            if edge == node2:
                return False
        for edge in self.adjacencyList[node2]:
            if edge == node1:
                return False
        self.numberOfEdges = self.numberOfEdges + 1
        self.adjacencyList[node1].append( node2 )
        self.adjacencyList[node2].append( node1 )
        return True

    def deleteEdge( self , node1, node2 ):
        for edge in self.adjacencyList[node1]:
            if edge == node2:
                self.adjacencyList[node1].remove( edge )
        for edge in self.adjacencyList[node2]:
            if edge == node1:
                self.adjacencyList[node2].remove( edge )
                self.numberOfEdges = self.numberOfEdges - 1
                return True
        return False

    def minDistanceFromSourceToAll( self , source ):
        if( source < 0 or source >= self.nodes ):
            return False
        distance = [ float('inf') ] * self.nodes
        distance[source] = 0
        q = queue.Queue()
        q.put( source )
        while( q.empty() == False ):
            currentNode = q.get()
            for nextNode in self.adjacencyList[currentNode]:
                if( distance[nextNode] > distance[currentNode] + 1 ):
                    distance[nextNode] = distance[currentNode] + 1
                    q.put( nextNode )
        return distance

    def minPairDistance( self , source , destination ):
        if( source < 0 or source >= self.nodes or destination < 0 or destination >= self.nodes ):
            return False
        distance = self.minDistanceFromSourceToAll( source )
        return distance[ destination ]

    def minPath( self , source , destination ):
        if( source < 0 or source >= self.nodes or destination < 0 or destination >= self.nodes ):
            return False
        distance = [ float('inf') ] * self.nodes
        distance[source] = 0
        q = queue.Queue()
        q.put( source )
        previousNode = [-1] * self.nodes
        while( q.empty() == False ):
            currentNode = q.get()
            for nextNode in self.adjacencyList[currentNode]:
                if( distance[nextNode] > distance[currentNode] + 1 ):
                    distance[nextNode] = distance[currentNode] + 1
                    previousNode[nextNode] = currentNode
                    q.put( nextNode )
        if( previousNode[destination] == -1 ):
            return "Error: No path between the nodes"
        path = deque([destination])
        currentNode = destination
        while( currentNode != source ):
            currentNode = previousNode[currentNode]
            path.appendleft(currentNode)
        return list(path)

    def minDistanceFromAllToAll( self ):
        distance = [[float('inf') for col in range(self.nodes)] for row in range(self.nodes)]
        for node1 in range( self.nodes ):
            distance[node1][node1] = 0
            for edge in self.adjacencyList[node1]:
                node2 = edge
                distance[node1][node2] = min( distance[node1][node2] , 1 )
        for k in range( self.nodes ):
            for i in range( self.nodes ):
                for j in range( self.nodes ):
                    distance[i][j] = min( distance[i][j] , distance[i][k] + distance[k][j] )
        for k in range( self.nodes ):
            for i in range( self.nodes ):
                for j in range( self.nodes ):
                    if( distance[i][j] > distance[i][k] + distance[k][j] ):
                        return "Error: Negative Weight Cycle"
        return distance
            

myGraph = UndirectedGraph( 7 )
myGraph.addEdge( 0 , 1 )
myGraph.addEdge( 0 , 2 )
myGraph.addEdge( 1 , 3 )
myGraph.addEdge( 2 , 3 )
myGraph.addEdge( 2 , 4 )
myGraph.addEdge( 3 , 5 )
myGraph.addEdge( 5 , 6 )

print( "list->", myGraph.adjacencyList )

for x in myGraph.adjacencyList:
    print(x)

print( "dist: " , myGraph.minDistanceFromSourceToAll( 0 ) )

for x in range( myGraph.nodes ):
    print( myGraph.minDistanceFromSourceToAll( x ) )
print( "all: " , myGraph.minDistanceFromAllToAll(  ) )

print("pair: " , myGraph.minPairDistance(0,5))
print("path: " , myGraph.minPath(0,5))

print( myGraph.minDistanceFromSourceToAll( 0 ) )
myGraph.deleteEdge( 1 , 3 )
print( myGraph.minDistanceFromSourceToAll( 0 ) )

print( str(type(myGraph)) )
