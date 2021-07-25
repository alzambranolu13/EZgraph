import queue
from collections import deque
from queue import LifoQueue

class DirectedGraph:
    def __init__( self , numberOfNodes ):
        if( numberOfNodes <= 0 ):
            print("Error: Number of nodes must be positive")
            exit()
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

    def addEdge( self , node1 , node2 ):
        if( node1 < 0 or node1 >= self.nodes or node2 < 0 or node2 >= self.nodes ):
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
        if( node1 == node2 ):
            print("Error: Self loops are not allowed")
            exit()
        if( self.adjacencyMatrix[node1][node2] != None ):
            print("Error: Edge between",node1,"and",node2,"already exists")
            exit()
        self.numberOfEdges = self.numberOfEdges + 1
        self.adjacencyMatrix[node1][node2] = 1
        self.adjacencyList[node1].append( node2 )
        return True

    def deleteEdge(self, node1, node2 ):
        if( node1 < 0 or node1 >= self.nodes or node2 < 0 or node2 >= self.nodes ):
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
        for edge in self.adjacencyList[node1]:
            if edge == node2:
                self.adjacencyList[node1].remove( edge )
                self.adjacencyMatrix[node1][node2] = None
                self.numberOfEdges = self.numberOfEdges - 1
                return True
        print("Error: Edge between",node1,"and",node2,"does not exist")
        exit()

    def getEdges( self ):
        allEdges = []
        for node1 in range(self.nodes):
            for node2 in self.adjacencyList[node1]:
                allEdges.append( [node1,node2] )
        return allEdges
    
    def BFS( self , node ):
        if( node < 0 or node >= self.nodes ):
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
        order = []
        visited = [False] * self.nodes
        q = queue.Queue()
        visited[node] = True
        q.put( node )
        while( q.empty() == False ):
            currNode = q.get()
            order.append( currNode )
            for nextNode in self.adjacencyList[currNode]:
                if visited[nextNode] == False:
                    visited[nextNode] = True
                    q.put( nextNode )
        return order

    def DFS( self , node ):
        if( node < 0 or node >= self.nodes ):
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
        order = []
        visited = [False] * self.nodes
        def DFSrecursion( node ):
            nonlocal order
            nonlocal visited
            order.append( node )
            visited[node] = True
            for nextNode in self.adjacencyList[node]:
                if visited[nextNode] == False:
                    DFSrecursion( nextNode )
        DFSrecursion( node )
        return order

    def minDistanceFromSourceToAll( self , source ):
        if( source < 0 or source >= self.nodes ):
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
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
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
        distance = self.minDistanceFromSourceToAll( source )
        return distance[ destination ]

    def minPath( self , source , destination ):
        if( source < 0 or source >= self.nodes or destination < 0 or destination >= self.nodes ):
            print("Error: Node index is out of bounds. Valid indexes are between 0 and",self.nodes)
            exit()
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
            print( "Error: No path between the nodes" )
            exit()
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
                        print("Error: Negative Weight Cycle")
                        exit()
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
            for nextNode in self.adjacencyList[node]:
                if inStack[nextNode] == True:
                    cycle = True
                elif visited[nextNode] == False:
                    CycleDFS( nextNode )
            inStack[node] = False
        for node in range( self.nodes ):
            CycleDFS( node )
        return cycle
    
    def topSort ( self ):
        q = queue.Queue()
        inDegree = [0] * self.nodes
        for node1 in range( self.nodes ):
            for node2 in self.adjacencyList[node1]:
                inDegree[node2] = inDegree[node2]+1
        topOrder = []
        for node in range( self.nodes ):
            if( inDegree[node] == 0 ):
                q.put( node )
        while( q.empty() == False ):
            currNode = q.get()
            topOrder.append( currNode )
            for nextNode in self.adjacencyList[currNode]:
                inDegree[nextNode] = inDegree[nextNode]-1
                if( inDegree[nextNode] == 0 ):
                    q.put( nextNode )
        if( len(topOrder) != self.nodes ):
            print("Error: Not possible to construct a topological sort")
            exit()
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
            for nextNode in self.adjacencyList[node]:
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

# myGraph = DirectedGraph( 5 )
# myGraph.addEdge( 0 , 1 )
# myGraph.addEdge( 0 , 2 )
# myGraph.addEdge( 1 , 2 )
# myGraph.addEdge( 1 , 3 )
# myGraph.addEdge( 1 , 4 )
# myGraph.addEdge( 3 , 2 )
# myGraph.addEdge( 3 , 1 )
# myGraph.addEdge( 4 , 3 )

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


# myGraph = DirectedGraph( 8 )
# myGraph.addEdge( 0 , 1 )
# myGraph.addEdge( 1 , 2 )
# myGraph.addEdge( 1 , 5 )
# myGraph.addEdge( 1 , 7 )
# myGraph.addEdge( 3 , 1 )
# myGraph.addEdge( 3 , 4 )
# myGraph.addEdge( 4 , 5 )
# myGraph.addEdge( 6 , 4 )
# myGraph.addEdge( 6 , 7 )

# print( myGraph.topSort() )
# print("CYC:", myGraph.hasCycle() )

# myGraph = DirectedGraph( 4 )
# myGraph.addEdge( 0 , 1 )
# myGraph.addEdge( 1 , 2 )
# myGraph.addEdge( 2 , 3 )
# myGraph.addEdge( 3 , 1 )

# print( "TopSort:" , myGraph.topSort() )

# myGraph = DirectedGraph( 5 )
# myGraph.addEdge( 1 , 0 )
# myGraph.addEdge( 0 , 2 )
# myGraph.addEdge( 2 , 1 )
# myGraph.addEdge( 0 , 3 )
# myGraph.addEdge( 3 , 4 )
# print( "SCC:" , myGraph.SCC() )

# print( myGraph.hasCycle() )

# print( str(type(myGraph)) )
