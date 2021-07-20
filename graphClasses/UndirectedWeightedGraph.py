from queue import PriorityQueue
from collections import deque
import queue

class UndirectedWeightedGraph:
    def __init__( self , numberOfNodes ):
        self.nodes = numberOfNodes
        self.adjacencyList = []
        self.numberOfEdges = 0
        self.adjacencyMatrix = [ [None] * numberOfNodes ] * numberOfNodes
        for i in range(numberOfNodes):
            self.adjacencyList.append( [] )

    def addEdge( self , node1 , node2 , weight ):
        for edge in self.adjacencyList[node1]:
            if edge[0] == node2:
                return False
        for edge in self.adjacencyList[node2]:
            if edge[0] == node1:
                return False
        self.numberOfEdges = self.numberOfEdges + 1
        self.adjacencyMatrix[node1][node2] = weight
        self.adjacencyMatrix[node2][node1] = weight
        self.adjacencyList[node1].append( [node2 , weight] )
        self.adjacencyList[node2].append( [node1 , weight] )
        return True

    def deleteEdge( self , node1, node2 ):
        for edge in self.adjacencyList[node1]:
            if edge[0] == node2:
                self.adjacencyList[node1].remove( edge )
                self.adjacencyMatrix[node1][node2] = None
        for edge in self.adjacencyList[node2]:
            if edge[0] == node1:
                self.adjacencyList[node2].remove( edge )
                self.adjacencyMatrix[node2][node1] = None
                self.numberOfEdges = self.numberOfEdges - 1
                return True
        return False

    def BFS( self , node ):
        order = []
        visited = [False] * self.nodes
        q = queue.Queue()
        visited[node] = True
        q.put( node )
        while( q.empty() == False ):
            currNode = q.get()
            order.append( currNode )
            for edge in self.adjacencyList[node]:
                nextNode = edge[0]
                if visited[nextNode] == False:
                    visited[nextNode] = True
                    q.put( nextNode )
        return order

    def minDistanceFromSourceToAll( self , source ):
        if( source < 0 or source >= self.nodes ):
            return False
        distance = [ float('inf') ] * self.nodes
        distance[source] = 0
        for i in range( self.nodes-1 ):
            for node1 in range( self.nodes ):
                for edge in self.adjacencyList[node1]:
                    node2 = edge[0]
                    weight = edge[1]
                    if( distance[node2] > distance[node1] + weight ):
                        distance[node2] = distance[node1] + weight
        for node1 in range( self.nodes ):
            for edge in self.adjacencyList[node1]:
                node2 = edge[0]
                weight = edge[1]
                if( distance[node2] > distance[node1] + weight ):
                    return "Error: Negative Weight Cycle"
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
        previousNode = [-1] * self.nodes
        for i in range( self.nodes-1 ):
            for node1 in range( self.nodes ):
                for edge in self.adjacencyList[node1]:
                    node2 = edge[0]
                    weight = edge[1]
                    if( distance[node2] > distance[node1] + weight ):
                        distance[node2] = distance[node1] + weight
                        previousNode[node2] = node1
        for node1 in range( self.nodes ):
            for edge in self.adjacencyList[node1]:
                node2 = edge[0]
                weight = edge[1]
                if( distance[node2] > distance[node1] + weight ):
                    return "Error: Negative Weight Cycle"
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
                node2 = edge[0]
                weight = edge[1]
                distance[node1][node2] = min( distance[node1][node2] , weight )
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
    
    def MinimumSpanningTree( self ):
        tree = UndirectedWeightedGraph( self.nodes )
        pq = PriorityQueue()
        visited = [ False ] * self.nodes
        visited[0] = True
        for edge in self.adjacencyList[0]:
            node = edge[0]
            weight = edge[1]
            if( visited[node] == False ):
                pq.put((weight , (0,node,weight) ))
        while( pq.empty() == False ):
            currentEdge = pq.get()
            node1 = currentEdge[1][0]
            node2 = currentEdge[1][1]
            weight = currentEdge[1][2]
            if ( visited[node2] == True ):
                continue
            visited[node2] = True
            tree.addEdge( node1 , node2 , weight )
            for edge in self.adjacencyList[node2]:
                node3 = edge[0]
                weight = edge[1]
                if( visited[node3] == False ):
                    pq.put((weight , (node2,node3,weight) ))
        return tree

    def MaximumSpanningTree( self ):
        tree = UndirectedWeightedGraph( self.nodes )
        pq = PriorityQueue()
        visited = [ False ] * self.nodes
        visited[0] = True
        for edge in self.adjacencyList[0]:
            node = edge[0]
            weight = edge[1]
            if( visited[node] == False ):
                pq.put((-weight , (0,node,weight) ))
        while( pq.empty() == False ):
            currentEdge = pq.get()
            node1 = currentEdge[1][0]
            node2 = currentEdge[1][1]
            weight = currentEdge[1][2]
            if ( visited[node2] == True ):
                continue
            visited[node2] = True
            tree.addEdge( node1 , node2 , weight )
            for edge in self.adjacencyList[node2]:
                node3 = edge[0]
                weight = edge[1]
                if( visited[node3] == False ):
                    pq.put((weight , (node2,node3,weight) ))
        return tree
            

myGraph = UndirectedWeightedGraph( 7 )
myGraph.addEdge( 0 , 1 , 2 )
myGraph.addEdge( 0 , 2 , 1 )
myGraph.addEdge( 1 , 3 , 2 )
myGraph.addEdge( 2 , 3 , 5 )
myGraph.addEdge( 2 , 4 , 7 )
myGraph.addEdge( 3 , 5 , 5 )
myGraph.addEdge( 5 , 6 , 11 )

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

myGraph = UndirectedWeightedGraph( 7 )
myGraph.addEdge( 0 , 1 , 5 )
myGraph.addEdge( 0 , 2 , 1 )
myGraph.addEdge( 0 , 4 , 4 )
myGraph.addEdge( 1 , 4 , 8 )
myGraph.addEdge( 1 , 5 , 6 )
myGraph.addEdge( 2 , 3 , 3 )
myGraph.addEdge( 2 , 4 , 2 )
myGraph.addEdge( 3 , 5 , 8 )
myGraph.addEdge( 4 , 5 , 7 )
myGraph.addEdge( 4 , 6 , 9 )

print("MST: " , myGraph.MinimumSpanningTree().adjacencyList)
print("CMP: " , myGraph.adjacencyList)