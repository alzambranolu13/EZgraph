import queue
from collections import deque
from queue import LifoQueue

class DirectedWeightedGraph:
    def __init__( self , numberOfNodes ):
        self.nodes = numberOfNodes
        self.adjacencyList = []
        self.numberOfEdges = 0
        self.adjacencyMatrix = []
        for i in range(numberOfNodes):
            self.adjacencyMatrix.append( [None] * self.nodes )
        for i in range(numberOfNodes):
            self.adjacencyList.append( [] )

    def getNodes( self ):
        return self.nodes

    def getNumEdges( self ):
        return self.numberOfEdges

    def getAdjacencyList( self ):
        return self.adjacencyList

    def getAdjacencyMatrix( self ):
        return self.adjacencyMatrix

    def addEdge( self , node1 , node2 , weight ):
        if( node1 == node2 ): return False
        if( self.adjacencyMatrix[node1][node2] != None ): return False
        self.numberOfEdges = self.numberOfEdges + 1
        self.adjacencyMatrix[node1][node2] = weight
        self.adjacencyList[node1].append( [node2 , weight] )
        return True

    def deleteEdge(self, node1, node2 ):
        for edge in self.adjacencyList[node1]:
            if edge[0] == node2:
                self.adjacencyList[node1].remove( edge )
                self.adjacencyMatrix[node1][node2] = None
                self.numberOfEdges = self.numberOfEdges - 1
                return True
        return False

    def getEdges( self ):
        allEdges = []
        for node1 in range(self.nodes):
            for edge in self.adjacencyList[node1]:
                node2 = edge[0]
                weight = edge[1]
                allEdges.append( [node1,node2,weight] )
        return allEdges

    def BFS( self , node ):
        order = []
        visited = [False] * self.nodes
        q = queue.Queue()
        visited[node] = True
        q.put( node )
        while( q.empty() == False ):
            currNode = q.get()
            order.append( currNode )
            for edge in self.adjacencyList[currNode]:
                nextNode = edge[0]
                if visited[nextNode] == False:
                    visited[nextNode] = True
                    q.put( nextNode )
        return order

    def DFS( self , node ):
        order = []
        visited = [False] * self.nodes
        def DFSrecursion( node ):
            nonlocal order
            nonlocal visited
            order.append( node )
            visited[node] = True
            for edge in self.adjacencyList[node]:
                nextNode = edge[0]
                if visited[nextNode] == False:
                    DFSrecursion( nextNode )
        DFSrecursion( node )
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

    def hasCycle( self ):
        visited = [False] * self.nodes
        inStack = [False] * self.nodes
        cycle = False
        
        def CycleDFS( node ):
            nonlocal visited
            nonlocal inStack
            nonlocal cycle
            if visited[node] == True:
                return
            visited[node] = True
            inStack[node] = True
            for edge in self.adjacencyList[node]:
                nextNode = edge[0]
                if inStack[nextNode] == True:
                    cycle = True
                elif visited[nextNode] == False:
                    CycleDFS( nextNode )
            inStack[node] = False
        for node in range( self.nodes ):
            CycleDFS( node )
        return cycle
    
    def hasNegativeCycle( self ):
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
                        return True
        return False
    
    def topSort ( self ):
        q = queue.Queue()
        inDegree = [0] * self.nodes
        for node1 in range( self.nodes ):
            for edge in self.adjacencyList[node1]:
                node2 = edge[0]
                weight = edge[1]
                inDegree[node2] = inDegree[node2]+1
        topOrder = []
        for node in range( self.nodes ):
            if( inDegree[node] == 0 ):
                q.put( node )
        while( q.empty() == False ):
            currNode = q.get()
            topOrder.append( currNode )
            for edge in self.adjacencyList[currNode]:
                nextNode = edge[0]
                inDegree[nextNode] = inDegree[nextNode]-1
                if( inDegree[nextNode] == 0 ):
                    q.put( nextNode )
        if( len(topOrder) != self.nodes ):
            return "Error: Not possible to construct a topological sort"
        return topOrder
    
    def SCC( self ):
        disc = [-1] * self.nodes
        low = [-1] * self.nodes
        components = [-1] * self.nodes
        inStack = [ False ] * self.nodes
        stack = LifoQueue( self.nodes )
        nextComponent = 0
        nextDiscovery = 0
        
        def tarjanDFS( node ):
            nonlocal disc
            nonlocal low
            nonlocal components
            nonlocal inStack
            nonlocal stack
            nonlocal nextComponent
            nonlocal nextDiscovery
            if( disc[node] != -1 ):
                return
            disc[node] = nextDiscovery
            low[node] = disc[node]
            nextDiscovery = nextDiscovery + 1
            inStack[node] = True
            stack.put( node )
            for edge in self.adjacencyList[node]:
                nextNode = edge[0]
                if( disc[nextNode] == -1 ):
                    tarjanDFS( nextNode )
                    low[node] = min( low[node] , low[nextNode] )
                elif( inStack[nextNode] == True ):
                    low[node] = min( low[node] , disc[nextNode] )
            if( disc[node] == low[node] ):
                while( True ):
                    currNode = stack.get()
                    components[currNode] = nextComponent
                    inStack[currNode] = False
                    if( currNode == node ):
                        break
                nextComponent = nextComponent + 1

        for node in range( self.nodes ):
            tarjanDFS( node )
        return components
    

# myGraph = DirectedWeightedGraph( 5 )
# myGraph.addEdge( 0 , 1 , -1 )
# myGraph.addEdge( 0 , 2 , 4 )
# myGraph.addEdge( 1 , 2 , 3 )
# myGraph.addEdge( 1 , 3 , 2 )
# myGraph.addEdge( 1 , 4 , 2 )
# myGraph.addEdge( 3 , 2 , 5 )
# myGraph.addEdge( 3 , 1 , 1 )
# myGraph.addEdge( 4 , 3 , -3 )

# print("Edges:",myGraph.getEdges())

# print( "list->", myGraph.adjacencyList )

# for x in myGraph.adjacencyList:
#     print(x)

# print( "dist: " , myGraph.minDistanceFromSourceToAll( 0 ) )

# for x in range( myGraph.nodes ):
#     print( myGraph.minDistanceFromSourceToAll( x ) )
# print( "all: " , myGraph.minDistanceFromAllToAll(  ) )

# print("pair: " , myGraph.minPairDistance(0,4))
# print("path: " , myGraph.minPath(0,4))

# print( myGraph.minDistanceFromSourceToAll( 0 ) )
# myGraph.deleteEdge( 0 , 1 )
# print( myGraph.minDistanceFromSourceToAll( 0 ) )


# myGraph = DirectedWeightedGraph( 8 )
# myGraph.addEdge( 0 , 1 , 1 )
# myGraph.addEdge( 1 , 2 , 1 )
# myGraph.addEdge( 1 , 5 , 1 )
# myGraph.addEdge( 1 , 7 , 1 )
# myGraph.addEdge( 3 , 1 , 1 )
# myGraph.addEdge( 3 , 4 , 1 )
# myGraph.addEdge( 4 , 5 , 1 )
# myGraph.addEdge( 6 , 4 , 1 )
# myGraph.addEdge( 6 , 7 , 1 )

# print( myGraph.topSort() )
# print("CYC:", myGraph.hasCycle() )

# myGraph = DirectedWeightedGraph( 4 )
# myGraph.addEdge( 0 , 1 , 1 )
# myGraph.addEdge( 1 , 2 , 1 )
# myGraph.addEdge( 2 , 3 , 1 )
# myGraph.addEdge( 3 , 1 , 1 )

# print( "TopSort:" , myGraph.topSort() )

# myGraph = DirectedWeightedGraph( 5 )
# myGraph.addEdge( 1 , 0 , 1 )
# myGraph.addEdge( 0 , 2 , 1 )
# myGraph.addEdge( 2 , 1 , 1 )
# myGraph.addEdge( 0 , 3 , 1 )
# myGraph.addEdge( 3 , 4 , 1 )
# print( "SCC:" , myGraph.SCC() )

# print( myGraph.hasCycle() )

# print( str(type(myGraph)) )
