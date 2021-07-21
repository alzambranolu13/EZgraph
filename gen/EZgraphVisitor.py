# Generated from C:/Users/a-zam/OneDrive/Documentos/Universidad/Lenguajes de programacion/proyectoFinal/EZgraph/grammar\EZgraph.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EZgraphParser import EZgraphParser
else:
    from EZgraphParser import EZgraphParser

# This class defines a complete generic visitor for a parse tree produced by EZgraphParser.

class EZgraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EZgraphParser#s.
    def visitS(self, ctx:EZgraphParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#exp.
    def visitExp(self, ctx:EZgraphParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#e.
    def visitE(self, ctx:EZgraphParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#creacion.
    def visitCreacion(self, ctx:EZgraphParser.CreacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#tipografo.
    def visitTipografo(self, ctx:EZgraphParser.TipografoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#declaracion.
    def visitDeclaracion(self, ctx:EZgraphParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#asignacion.
    def visitAsignacion(self, ctx:EZgraphParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#leer.
    def visitLeer(self, ctx:EZgraphParser.LeerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#imprimir.
    def visitImprimir(self, ctx:EZgraphParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#value.
    def visitValue(self, ctx:EZgraphParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#funciondeclaracion.
    def visitFunciondeclaracion(self, ctx:EZgraphParser.FunciondeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#funcion.
    def visitFuncion(self, ctx:EZgraphParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#lista.
    def visitLista(self, ctx:EZgraphParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#matriz.
    def visitMatriz(self, ctx:EZgraphParser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#dentro.
    def visitDentro(self, ctx:EZgraphParser.DentroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#pintar.
    def visitPintar(self, ctx:EZgraphParser.PintarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#tipo.
    def visitTipo(self, ctx:EZgraphParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EZgraphParser#ciclo.
    def visitCiclo(self, ctx:EZgraphParser.CicloContext):
        return self.visitChildren(ctx)



del EZgraphParser