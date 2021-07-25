import sys
from antlr4 import *
from gen.EZgraphLexer import EZgraphLexer
from gen.EZgraphParser import EZgraphParser
from gen.EZgraphVisitor import EZgraphVisitor
from graphClasses.DirectedGraph import DirectedGraph
from graphClasses.UndirectedGraph import UndirectedGraph
from graphClasses.DirectedWeightedGraph import DirectedWeightedGraph
from graphClasses.UndirectedWeightedGraph import UndirectedWeightedGraph
from plotting import paint as paint

dicc_table={}
class EZgraphInterpreterVisitor(EZgraphVisitor):



    def visitS(self, ctx):
        self.visitExp(ctx.exp())

    def visitExp(self, ctx):
        if (ctx.e() != None):
            self.visitE(ctx.e())
            self.visitExp(ctx.exp())

    def visitE(self, ctx):
        if (ctx.declaracion() != None):
            self.visitDeclaracion(ctx.declaracion())
        elif (ctx.creacion() != None):
            self.visitCreacion(ctx.creacion())
        elif (ctx.leer() != None):
            self.visitLeer(ctx.leer())
        elif (ctx.imprimir() != None):
            self.visitImprimir(ctx.imprimir())
        elif (ctx.ciclo() != None):
            self.visitCiclo(ctx.ciclo())
        elif (ctx.pintar() != None):
            self.visitPintar(ctx.pintar())
        elif (ctx.funcion() != None):
            self.visitFuncion(ctx.funcion())

    def visitLeer(self, ctx:EZgraphParser.LeerContext):
        global dicc_table
        id = ctx.ID()
        val = input()
        dicc_table[id] = val

    def visitImprimir(self, ctx:EZgraphParser.ImprimirContext):
        if ctx.value() != None:
            print(self.visitValue(ctx.value()))

    def visitCreacion(self, ctx:EZgraphParser.CreacionContext):
        global dicc_table
        tipo = str(ctx.TIPOGRAFO())
        id = str(ctx.ID())
        size = int(str(ctx.INT()))

        if ( tipo == 'NDGraph'):
            dicc_table[id]= UndirectedGraph(size)
        elif ( tipo == 'DGraph'):
            dicc_table[id]= DirectedGraph(size)
        elif ( tipo == 'DWGraph'):
            dicc_table[id]= DirectedWeightedGraph(size)
        elif ( tipo == 'NDWGraph'):
            dicc_table[id]= UndirectedWeightedGraph(size)



    def visitDeclaracion(self, ctx:EZgraphParser.DeclaracionContext):
        global dicc_table
        id = str(ctx.ID())
        value= self.visitValue(ctx.value())
        dicc_table[id]= value

    def visitValue(self, ctx:EZgraphParser.ValueContext):
        global dicc_table
        if (ctx.funciondeclaracion() != None):
            return self.visitFunciondeclaracion(ctx.funciondeclaracion())
        elif (ctx.STRING() != None):
            return ctx.STRING()
        elif (ctx.INT() != None):
            return int(ctx.INT())
        elif (ctx.DOUBLE() != None):
            return float(ctx.DOUBLE())
        elif (ctx.BOOLEANO() != None):
            if (ctx.BOOLEANO() == "true"):
                return True
            else:
                return False
        elif (ctx.ID() != None):
            if str(ctx.ID()) in dicc_table:
                return dicc_table[str(ctx.ID())]
            else:
                self.Error()
                pass


    def visitFunciondeclaracion(self, ctx:EZgraphParser.FunciondeclaracionContext):
        global dicc_table
        id = str(ctx.ID())

        graph = dicc_table[id]

        tipoGrafo=''
        if type(graph) == UndirectedWeightedGraph:
            tipoGrafo= 'NDW'
        if type(graph) == DirectedGraph:
            tipoGrafo = 'D'
        if type(graph) == DirectedWeightedGraph:
            tipoGrafo = 'DW'
        if type(graph) == UndirectedGraph:
            tipoGrafo = 'ND'

        if ( tipoGrafo == ''):
            self.Error(ctx.start.line,ctx.start.column)

        if (id in dicc_table):
            if ( ctx.FUNCIONCPARAM() != None):
                funcion= str(ctx.FUNCIONCPARAM())
                if funcion == 'getNumEdges':
                    return graph.getNumEdges()
                if funcion == 'getNodes':
                    return graph.getNodes()
                if funcion == 'getEdges':
                    return graph.getEdges()
                if funcion == 'getMatrix':
                    return graph.getAdjacencyMatrix()
                if funcion == 'getAllDistances':
                    return graph.minDistanceFromAllToAll()
                if funcion == 'getMinimumSpanningTree':
                    if tipoGrafo == 'NDW':
                        return graph.MinimumSpanningTree()
                    else:
                        self.Error(ctx.start.line,ctx.start.column)
                        pass
                if funcion == 'getMaximumSpanningTree':
                    if tipoGrafo == 'NDW':
                        return graph.MaximumSpanningTree()
                    else:
                        self.Error(ctx.start.line,ctx.start.column)
                        pass
                if funcion == 'hasCycle':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        return graph.hasCycle()
                    else:
                        self.Error(ctx.start.line,ctx.start.column)
                        pass
                if funcion == 'getSCC':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        return graph.SCC()
                    else:
                        self.Error(ctx.start.line,ctx.start.column)
                        pass
                if funcion == 'getTopologicalOrder':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        return graph.topSort()
                    else:
                        self.Error(ctx.start.line,ctx.start.column)
                        pass
            elif (ctx.FUNCIONUNPARAM() != None):
                funcion = str(ctx.FUNCIONUNPARAM())
                node = int(str(ctx.INT()[0]))
                if funcion == 'getDistanceFromNode':
                    return graph.minDistanceFromSourceToAll(node)
                if funcion == 'BFS':
                    return graph.BFS(node)
                if funcion == 'DFS':
                    return graph.DFS(node)
            elif (ctx.FUNCIONDOPARAM() != None):
                funcion = str(ctx.FUNCIONDOPARAM())
                node1 = int(str(ctx.INT()[0]))
                node2 = int(str(ctx.INT()[1]))
                if funcion == 'getDistance':
                    return graph.minPairDistance(node1, node2)
                if funcion == 'getShortestPath':
                    return graph.minPath(node1, node2)
        else:
            self.Error(ctx.start.line,ctx.start.column)
            pass


    def visitFuncion(self, ctx:EZgraphParser.FuncionContext):
        global dicc_table
        id = str(ctx.ID())
        graph = dicc_table[id]
        tipoGrafo = ''
        if type(graph) == UndirectedWeightedGraph:
            tipoGrafo = 'NDW'
        if type(graph) == DirectedGraph:
            tipoGrafo = 'D'
        if type(graph) == DirectedWeightedGraph:
            tipoGrafo = 'DW'
        if type(graph) ==UndirectedGraph:
            tipoGrafo = 'ND'

        if ( tipoGrafo == ''):
            self.Error(ctx.start.line,ctx.start.column)
            pass

        weighted = False
        if ctx.DOUBLE() != None or len(ctx.INT()) >= 3:
            if tipoGrafo == 'D' or tipoGrafo == 'ND':
                self.Error(ctx.start.line,ctx.start.column)
                pass
            else:
                weighted = True

        if (ctx.ADDEDGE() != None):
            if weighted == True:
                if ( ctx.DOUBLE() != None):
                    peso = float(str(ctx.DOUBLE()))
                else:
                    peso = int(str(ctx.INT()[2]))

                graph.addEdge(int(str(ctx.INT()[0])), int(str(ctx.INT()[1])), peso)
            else:
                graph.addEdge(int(str(ctx.INT()[0])), int(str(ctx.INT()[1])))
        elif (ctx.DELETEEDGE() != None):
            graph.deleteEdge(int(str(ctx.INT()[0])), int(str(ctx.INT()[1])))


    def visitPintar(self, ctx:EZgraphParser.PintarContext):
        global dicc_table
        
        id = str(ctx.ID())
        graph = dicc_table[id]
        paint.paint_graph(graph)
        pass


    def visitCiclo(self, ctx:EZgraphParser.CicloContext):
        global dicc_table
        idx= str(ctx.ID())
        inicial= self.visitValue(ctx.value()[0])
        final = self.visitValue(ctx.value()[1])
        if type(inicial) == int and type(final) == int :
            for i in range(inicial, final):
                dicc_table[idx] = i
                if ctx.exp() != None:
                    self.visitExp(ctx.exp())


    def Error(self,line,column):
        print('Error in line:', line, 'column:', column)
        exit()













