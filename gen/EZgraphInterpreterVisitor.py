import sys
from antlr4 import *
from gen.EZgraphLexer import EZgraphLexer
from gen.EZgraphParser import EZgraphParser
from gen.EZgraphVisitor import EZgraphVisitor

class EZgraphInterpreterVisitor(EZgraphVisitor):

    def visitS(self, ctx):
        return

    def visitExp(self, ctx):
        if (ctx.e() != None):
            self.visitE(ctx.e())
            self.visitExp(ctx.exp())
        else:

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



