import sys
from antlr4 import *
from gen.EZgraphLexer import EZgraphLexer
from gen.EZgraphParser import EZgraphParser
from gen.EZgraphVisitor import EZgraphVisitor

class EZgraphInterpreterVisitor(EZgraphVisitor):

    def visitS(self, ctx):
        self.visitExp(ctx.exp())

    def visitExp(self, ctx):
        if (ctx.e() != None):
            self.visitE(ctx.e())
            self.visitExp(ctx.exp())
        else:
            pass

    def visitE(self, ctx):
        if (ctx.declaracion() != None):
            self.visitDeclaracion(ctx.declaracion())
            #print("decla")
        elif (ctx.creacion() != None):
            self.visitCreacion(ctx.creacion())
        elif (ctx.asignacion() != None):
            self.visitAsignacion(ctx.asignacion())
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

    def visitCreacion(self, ctx:EZgraphParser.CreacionContext):
        print("entre")
        self.visitTipografo(ctx.tipografo())
        id = ctx.ID()
        #print(id)

    def visitDeclaracion(self, ctx:EZgraphParser.DeclaracionContext):
        if (ctx.value() != None):
            self.visitValue(ctx.value())

    def visitAsignacion(self, ctx:EZgraphParser.AsignacionContext):
        return

    def visitValue(self, ctx:EZgraphParser.ValueContext):
        if (ctx.funciondeclaracion() != None):
            self.visitFunciondeclaracion(ctx.funciondeclaracion())
        elif (ctx.STRING() != None):
            pass
        elif (ctx.INT() != None):
            pass
        elif (ctx.FLOAT() != None):
            pass
        elif (ctx.BOOLEANO() != None):
            pass
        elif (ctx.lista() != None):
            self.visitLista(ctx.lista())
        elif (ctx.matriz() != None):
            self.visitMatriz(ctx.matriz())

    def visitFunciondeclaracion(self, ctx:EZgraphParser.FunciondeclaracionContext):
        if (ctx.FUNCIONCPARAM() != None):
            print(ctx.FUNCIONCPARAM())
        elif (ctx.FUNCIONUNPARAM() != None):
            print(ctx.FUNCIONUNPARAM())
        elif (ctx.FUNCIONDOPARAM() != None):
            print(ctx.FUNCIONDOPARAM())

    def visitFuncion(self, ctx:EZgraphParser.FuncionContext):
        if (ctx.ADDEDGE() != None):
            pass
        elif (ctx.DELETEEDGE() != None):
            pass

    def visitLista(self, ctx:EZgraphParser.ListaContext):
        pass

    def visitMatriz(self, ctx:EZgraphParser.MatrizContext):
        pass

    def visitPintar(self, ctx:EZgraphParser.PintarContext):
        pass

    def visitTipo(self, ctx:EZgraphParser.TipoContext):
        pass

    def visitCiclo(self, ctx:EZgraphParser.CicloContext):
        ##implementar for
        if (ctx.exp() != None):
            self.visitExp(ctx.exp())










