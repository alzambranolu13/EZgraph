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
import re

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
        id = str(ctx.ID())
        val = input()

        if val.isdigit():
            dicc_table[id] = int(val)
        elif not(re.match(r'^-?\d+(?:\.\d+)$', val) is None):
            dicc_table[id] = float(val)
        else:
            dicc_table[id] = val


    def visitImprimir(self, ctx:EZgraphParser.ImprimirContext):
        if ctx.value() != None:
            print(self.visitValue(ctx.value()))

    def visitCreacion(self, ctx:EZgraphParser.CreacionContext):
        global dicc_table
        tipo = str(ctx.TIPOGRAFO())
        id = str(ctx.ID())
        size = self.visitValue(ctx.value())
        if not(str(size).isdigit()):
            self.Error(ctx.start.line, ctx.start.column, "size of graph must be an integer")

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
            string = str(ctx.STRING())
            string = string[1: len(string)-1]
            return string
        elif (ctx.INT() != None):
            return int(str(ctx.INT()))
        elif (ctx.DOUBLE() != None):
            return float(str(ctx.DOUBLE()))
        elif (ctx.BOOLEANO() != None):
            if (ctx.BOOLEANO() == "true"):
                return True
            else:
                return False
        elif (ctx.ID() != None):
            if str(ctx.ID()) in dicc_table:
                return dicc_table[str(ctx.ID())]
            else:
                self.Error(ctx.start.line,ctx.start.column, "variable with id { } does not exist".format(str(ctx.ID())))
                pass


    def visitFunciondeclaracion(self, ctx:EZgraphParser.FunciondeclaracionContext):
        global dicc_table
        id = str(ctx.ID())

        if not(id in dicc_table):
            self.Error(ctx.start.line, ctx.start.column, "variable with id {} does not exist".format(id))

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
            self.Error(ctx.start.line,ctx.start.column,"variable {} is not a graph type".format(graph))

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
                        self.Error(ctx.start.line,ctx.start.column, "variable {} must be of type NDWGraph".format(id))
                        pass
                if funcion == 'getMaximumSpanningTree':
                    if tipoGrafo == 'NDW':
                        return graph.MaximumSpanningTree()
                    else:
                        self.Error(ctx.start.line,ctx.start.column, "variable {} must be of type NDWGraph".format(id))
                        pass
                if funcion == 'hasCycle':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        return graph.hasCycle()
                    else:
                        self.Error(ctx.start.line,ctx.start.column,"variable {} must be of type DWGraph or DGraph".format(id))
                        pass
                if funcion == 'getSCC':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        return graph.SCC()
                    else:
                        self.Error(ctx.start.line,ctx.start.column,"variable {} must be of type DWGraph or DGraph".format(id))
                        pass
                if funcion == 'getTopologicalOrder':
                    if tipoGrafo == 'D' or tipoGrafo == 'DW':
                        return graph.topSort()
                    else:
                        self.Error(ctx.start.line,ctx.start.column,"variable {} must be of type DWGraph or DGraph".format(id))
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
            self.Error(ctx.start.line,ctx.start.column, "variable with id {} does not exist".format(id))
            pass


    def visitFuncion(self, ctx:EZgraphParser.FuncionContext):
        global dicc_table
        id = str(ctx.ID())
        if not(id in dicc_table):
            self.Error(ctx.start.line, ctx.start.column, "variable with id {} does not exist".format(id))

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
            self.Error(ctx.start.line,ctx.start.column, 'variable {} is not a graph type'.format(id))
            pass

        weighted = False
        if len(ctx.value()) >= 3:
            if tipoGrafo == 'D' or tipoGrafo == 'ND':
                self.Error(ctx.start.line,ctx.start.column,"variable {} must be of type DWGraph or NDWGraph".format(id))
                pass
            else:
                weighted = True
        node1 = self.visitValue(ctx.value()[0])
        node2 = self.visitValue(ctx.value()[1])
        if (ctx.ADDEDGE() != None):
            if weighted == True:
                peso = self.visitValue(ctx.value()[2])
                graph.addEdge(node1, node2, peso)
            else:
                graph.addEdge(node1, node2)
        elif (ctx.DELETEEDGE() != None):
            graph.deleteEdge(node1, node2)


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


    def Error(self,line,column,text):
        print('Error in line:', line, 'column:', column,text)
        exit(0)













