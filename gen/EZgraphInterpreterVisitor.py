import sys
from antlr4 import *
from gen.EZgraphLexer import EZgraphLexer
from gen.EZgraphParser import EZgraphParser
from gen.EZgraphVisitor import EZgraphVisitor
from graphClasses.DirectedGraph import DirectedGraph
from graphClasses.UndirectedGraph import UndirectedGraph
from graphClasses.DirectedWeightedGraph import DirectedWeightedGraph
from graphClasses.UndirectedWeightedGraph import UndirectedWeightedGraph

class EZgraphInterpreterVisitor(EZgraphVisitor):


    dicc_table = { }
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
            print(ctx.value())

    def visitCreacion(self, ctx:EZgraphParser.CreacionContext):
        global dicc_table
        tipo = ctx.TIPOGRAFO()
        id = ctx.ID()
        size = int(ctx.INT())

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
        id = ctx.ID()
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
        elif (ctx.FLOAT() != None):
            return float(ctx.FLOAT())
        elif (ctx.BOOLEANO() != None):
            if (ctx.BOOLEANO() == "true"):
                return True
            else:
                return False
        elif (ctx.ID() != None):
            if ctx.ID() in dicc_table:
                return dicc_table[ctx.ID()]
            else:
                #ERROR
                pass


    def visitFunciondeclaracion(self, ctx:EZgraphParser.FunciondeclaracionContext):
        global dicc_table
        id = ctx.ID()
        graph = dicc_table[id]
        tipoGrafo=''
        if str(type(graph)) == "<class '__main__.UndirectedWeightedGraph>":
            tipoGrafo= 'NDW'
        if str(type(graph)) == "<class '__main__.DirectedGraph'>":
            tipoGrafo = 'D'
        if str(type(graph)) == "<class '__main__.DirectedWeightedGraph'>":
            tipoGrafo = 'DW'
        if str(type(graph)) == "<class '__main__.UndirectedGraph'>":
            tipoGrafo = 'ND'

        if ( tipoGrafo == ''):
            #ERROR
            pass

        if (id in dicc_table):
            if (ctx.FUNCIONCPARAM() != None):
                if ctx.FUNCIONCPARAM() == 'getNumEdges':
                    return graph.numEdges
                if ctx.FUNCIONCPARAM() == 'getNodes':
                    return graph.nodes
                if ctx.FUNCIONCPARAM() == 'getEdges':
                    pass
                if ctx.FUNCIONCPARAM() == 'getMatrix':
                    pass
                if ctx.FUNCIONCPARAM() == 'getAllDistances':
                    graph.minDistanceFromAllToAll()
                if ctx.FUNCIONCPARAM() == 'getMinimunSpanningTree':
                    if tipoGrafo == 'NDW':
                        graph.minimunSpanningTree()
                    else:
                        #ERROR
                        pass
                if ctx.FUNCIONCPARAM() == 'getMaximunSpanningTree':
                    if tipoGrafo == 'NDW':
                        graph.maximunSpanningTree()
                    else:
                        #ERROR
                        pass
                if ctx.FUNCIONCPARAM() == 'hasCycle':
                    if tipoGrafo == 'NDW' or tipoGrafo == 'DW':
                        graph.hasCycle()
                    else:
                        #ERROR
                        pass
                if ctx.FUNCIONCPARAM() == 'getSCC':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        graph.SCC()
                    else:
                        #ERROR
                        pass
                if ctx.FUNCIONCPARAM() == 'getTopologicalOrder':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        graph.topSort()
                    else:
                        #ERROR
                        pass
            elif (ctx.FUNCIONUNPARAM() != None):
                node = int(ctx.INT())
                if ctx.FUNCIONUNPARAM() == 'getDistancesFromNode':
                    graph.minDistanceSourceToAll(node)
                if ctx.FUNCIONUNPARAM() == 'BFS':
                    graph.BFS(node)
                if ctx.FUNCIONUNPARAM() == 'DFS':
                    graph.DFS(node)
            elif (ctx.FUNCIONDOPARAM() != None):
                node1 = int(ctx.INT()[0])
                node2 = int(ctx.INT()[1])
                if ctx.FUNCIONCPARAM() == 'getDistance':
                    graph.minPairDistance(node1, node2)
                if ctx.FUNCIONCPARAM() == 'getShortestPath':
                    graph.minPath(node1, node2)
        else:
            #ERROR
            pass


    def visitFuncion(self, ctx:EZgraphParser.FuncionContext):
        global dicc_table
        id = ctx.ID()
        graph = dicc_table[id]
        tipoGrafo = ''
        if str(type(graph)) == "<class '__main__.UndirectedWeightedGraph>":
            tipoGrafo = 'NDW'
        if str(type(graph)) == "<class '__main__.DirectedGraph'>":
            tipoGrafo = 'D'
        if str(type(graph)) == "<class '__main__.DirectedWeightedGraph'>":
            tipoGrafo = 'DW'
        if str(type(graph)) == "<class '__main__.UndirectedGraph'>":
            tipoGrafo = 'ND'

        if ( tipoGrafo == ''):
            #ERROR
            pass

        weighted = False
        if len(ctx.INT()) > 2 :
            if tipoGrafo == 'D' or tipoGrafo == 'ND':
                #ERROR
                pass
            else:
                weighted = True
        elif len(ctx.INT()) <= 1:
            #ERROR
            pass

        if (ctx.ADDEDGE() != None):
            if weighted == True:
                graph.addEdge(int(ctx.INT()[0]), int(ctx.INT()[1]), int(ctx.INT()[2]))
            else:
                graph.addEdge(int(ctx.INT()[0]), int(ctx.INT()[1]))
        elif (ctx.DELETEEDGE() != None):
            graph.deleteEdge(int(ctx.INT()[0]), int(ctx.INT()[1]))


    def visitPintar(self, ctx:EZgraphParser.PintarContext):
        pass


    def visitCiclo(self, ctx:EZgraphParser.CicloContext):
        idx= ctx.ID()
        inicial= self.visitValue(ctx.value()[0])
        final = self.visitValue(ctx.value()[1])

        if type(inicial) == int and type(final) == int :
            for i in range(inicial, final):
                if ctx.exp() != None:
                    self.visitExp(ctx.exp())











