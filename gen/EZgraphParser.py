# Generated from C:/Users/a-zam/OneDrive/Documentos/Universidad/Lenguajes de programacion/proyectoFinal/EZgraph/grammar\EZgraph.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u00df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3+\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\65\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6G\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\nh\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u0080\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u009f\n\f\3\r\3")
        buf.write("\r\3\r\7\r\u00a4\n\r\f\r\16\r\u00a7\13\r\3\r\3\r\3\r\3")
        buf.write("\r\7\r\u00ad\n\r\f\r\16\r\u00b0\13\r\3\r\3\r\3\r\3\r\7")
        buf.write("\r\u00b6\n\r\f\r\16\r\u00b9\13\r\3\r\5\r\u00bc\n\r\3\16")
        buf.write("\3\16\3\16\3\16\7\16\u00c2\n\16\f\16\16\16\u00c5\13\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\6\u00a5\u00ae\u00b7\u00c3\2\23\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"\2\5\4\2\36\36&&\4\2")
        buf.write("\16\23%%\4\2\35\35&&\2\u00e6\2$\3\2\2\2\4*\3\2\2\2\6\64")
        buf.write("\3\2\2\2\b\66\3\2\2\2\nF\3\2\2\2\fH\3\2\2\2\16L\3\2\2")
        buf.write("\2\20R\3\2\2\2\22g\3\2\2\2\24\177\3\2\2\2\26\u009e\3\2")
        buf.write("\2\2\30\u00bb\3\2\2\2\32\u00bd\3\2\2\2\34\u00c8\3\2\2")
        buf.write("\2\36\u00cb\3\2\2\2 \u00d2\3\2\2\2\"\u00d4\3\2\2\2$%\5")
        buf.write("\4\3\2%\3\3\2\2\2&\'\5\6\4\2\'(\5\4\3\2(+\3\2\2\2)+\3")
        buf.write("\2\2\2*&\3\2\2\2*)\3\2\2\2+\5\3\2\2\2,\65\5\n\6\2-\65")
        buf.write("\5\b\5\2.\65\5\f\7\2/\65\5\16\b\2\60\65\5\20\t\2\61\65")
        buf.write("\5\"\22\2\62\65\5\36\20\2\63\65\5\26\f\2\64,\3\2\2\2\64")
        buf.write("-\3\2\2\2\64.\3\2\2\2\64/\3\2\2\2\64\60\3\2\2\2\64\61")
        buf.write("\3\2\2\2\64\62\3\2\2\2\64\63\3\2\2\2\65\7\3\2\2\2\66\67")
        buf.write("\7%\2\2\678\7&\2\289\7\3\2\29:\7\35\2\2:;\7\4\2\2;<\7")
        buf.write("\5\2\2<\t\3\2\2\2=>\5 \21\2>?\7&\2\2?@\7\6\2\2@A\5\22")
        buf.write("\n\2AG\3\2\2\2BC\5 \21\2CD\7&\2\2DE\7\5\2\2EG\3\2\2\2")
        buf.write("F=\3\2\2\2FB\3\2\2\2G\13\3\2\2\2HI\7&\2\2IJ\7\6\2\2JK")
        buf.write("\5\22\n\2K\r\3\2\2\2LM\7\7\2\2MN\7\b\2\2NO\7&\2\2OP\7")
        buf.write("\t\2\2PQ\7\5\2\2Q\17\3\2\2\2RS\7\n\2\2ST\7\b\2\2TU\t\2")
        buf.write("\2\2UV\7\t\2\2VW\7\5\2\2W\21\3\2\2\2Xh\5\24\13\2YZ\7\36")
        buf.write("\2\2Zh\7\5\2\2[\\\7\35\2\2\\h\7\5\2\2]^\7\'\2\2^h\7\5")
        buf.write("\2\2_`\7\37\2\2`h\7\5\2\2ab\5\30\r\2bc\7\5\2\2ch\3\2\2")
        buf.write("\2de\5\32\16\2ef\7\5\2\2fh\3\2\2\2gX\3\2\2\2gY\3\2\2\2")
        buf.write("g[\3\2\2\2g]\3\2\2\2g_\3\2\2\2ga\3\2\2\2gd\3\2\2\2h\23")
        buf.write("\3\2\2\2ij\7&\2\2jk\7\13\2\2kl\7 \2\2lm\7\b\2\2mn\7\t")
        buf.write("\2\2n\u0080\7\5\2\2op\7&\2\2pq\7\13\2\2qr\7!\2\2rs\7\b")
        buf.write("\2\2st\7\35\2\2tu\7\t\2\2u\u0080\7\5\2\2vw\7&\2\2wx\7")
        buf.write("\13\2\2xy\7\"\2\2yz\7\b\2\2z{\7\35\2\2{|\7\f\2\2|}\7\35")
        buf.write("\2\2}~\7\t\2\2~\u0080\7\5\2\2\177i\3\2\2\2\177o\3\2\2")
        buf.write("\2\177v\3\2\2\2\u0080\25\3\2\2\2\u0081\u0082\7&\2\2\u0082")
        buf.write("\u0083\7\13\2\2\u0083\u0084\7#\2\2\u0084\u0085\7\b\2\2")
        buf.write("\u0085\u0086\7\35\2\2\u0086\u0087\7\f\2\2\u0087\u0088")
        buf.write("\7\35\2\2\u0088\u0089\7\t\2\2\u0089\u009f\7\5\2\2\u008a")
        buf.write("\u008b\7&\2\2\u008b\u008c\7\13\2\2\u008c\u008d\7#\2\2")
        buf.write("\u008d\u008e\7\b\2\2\u008e\u008f\7\35\2\2\u008f\u0090")
        buf.write("\7\f\2\2\u0090\u0091\7\35\2\2\u0091\u0092\7\f\2\2\u0092")
        buf.write("\u0093\7\35\2\2\u0093\u0094\7\t\2\2\u0094\u009f\7\5\2")
        buf.write("\2\u0095\u0096\7&\2\2\u0096\u0097\7\13\2\2\u0097\u0098")
        buf.write("\7$\2\2\u0098\u0099\7\b\2\2\u0099\u009a\7\35\2\2\u009a")
        buf.write("\u009b\7\f\2\2\u009b\u009c\7\35\2\2\u009c\u009d\7\t\2")
        buf.write("\2\u009d\u009f\7\5\2\2\u009e\u0081\3\2\2\2\u009e\u008a")
        buf.write("\3\2\2\2\u009e\u0095\3\2\2\2\u009f\27\3\2\2\2\u00a0\u00a1")
        buf.write("\7\3\2\2\u00a1\u00a5\7\35\2\2\u00a2\u00a4\13\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a5\u00a3\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a8\u00bc\7\4\2\2\u00a9\u00aa\7\3\2\2\u00aa\u00ae")
        buf.write("\7\'\2\2\u00ab\u00ad\13\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00af\u00b1\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00bc\7")
        buf.write("\4\2\2\u00b2\u00b3\7\3\2\2\u00b3\u00b7\7\36\2\2\u00b4")
        buf.write("\u00b6\13\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2")
        buf.write("\2\u00b7\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba")
        buf.write("\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bc\7\4\2\2\u00bb")
        buf.write("\u00a0\3\2\2\2\u00bb\u00a9\3\2\2\2\u00bb\u00b2\3\2\2\2")
        buf.write("\u00bc\31\3\2\2\2\u00bd\u00be\7\3\2\2\u00be\u00bf\5\30")
        buf.write("\r\2\u00bf\u00c3\5\34\17\2\u00c0\u00c2\13\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c3\u00c1\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c3\3")
        buf.write("\2\2\2\u00c6\u00c7\7\4\2\2\u00c7\33\3\2\2\2\u00c8\u00c9")
        buf.write("\7\5\2\2\u00c9\u00ca\5\30\r\2\u00ca\35\3\2\2\2\u00cb\u00cc")
        buf.write("\7&\2\2\u00cc\u00cd\7\13\2\2\u00cd\u00ce\7\r\2\2\u00ce")
        buf.write("\u00cf\7\b\2\2\u00cf\u00d0\7\t\2\2\u00d0\u00d1\7\5\2\2")
        buf.write("\u00d1\37\3\2\2\2\u00d2\u00d3\t\3\2\2\u00d3!\3\2\2\2\u00d4")
        buf.write("\u00d5\7\24\2\2\u00d5\u00d6\7&\2\2\u00d6\u00d7\7\6\2\2")
        buf.write("\u00d7\u00d8\t\4\2\2\u00d8\u00d9\7\25\2\2\u00d9\u00da")
        buf.write("\7&\2\2\u00da\u00db\7\26\2\2\u00db\u00dc\5\4\3\2\u00dc")
        buf.write("\u00dd\7\27\2\2\u00dd#\3\2\2\2\r*\64Fg\177\u009e\u00a5")
        buf.write("\u00ae\u00b7\u00bb\u00c3")
        return buf.getvalue()


class EZgraphParser ( Parser ):

    grammarFileName = "EZgraph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "';'", "'='", "'read'", 
                     "'('", "')'", "'print'", "'.'", "','", "'paint'", "'int'", 
                     "'string'", "'double'", "'bool'", "'List'", "'Matrix'", 
                     "'for'", "':'", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'getDistance'", "'addEdge'", "'deleteEdge'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COMMENT", "LINE_COMMENT", 
                      "EASTEREGG", "WS", "DOUBLE", "INT", "STRING", "BOOLEANO", 
                      "FUNCIONCPARAM", "FUNCIONUNPARM", "FUNCIONDOPARAM", 
                      "ADDEDGE", "DELETEEDGE", "TIPOGRAFO", "ID", "FLOAT" ]

    RULE_s = 0
    RULE_exp = 1
    RULE_e = 2
    RULE_creacion = 3
    RULE_declaracion = 4
    RULE_asignacion = 5
    RULE_leer = 6
    RULE_imprimir = 7
    RULE_value = 8
    RULE_funciondeclaracion = 9
    RULE_funcion = 10
    RULE_lista = 11
    RULE_matriz = 12
    RULE_dentro = 13
    RULE_pintar = 14
    RULE_tipo = 15
    RULE_ciclo = 16

    ruleNames =  [ "s", "exp", "e", "creacion", "declaracion", "asignacion", 
                   "leer", "imprimir", "value", "funciondeclaracion", "funcion", 
                   "lista", "matriz", "dentro", "pintar", "tipo", "ciclo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    COMMENT=22
    LINE_COMMENT=23
    EASTEREGG=24
    WS=25
    DOUBLE=26
    INT=27
    STRING=28
    BOOLEANO=29
    FUNCIONCPARAM=30
    FUNCIONUNPARM=31
    FUNCIONDOPARAM=32
    ADDEDGE=33
    DELETEEDGE=34
    TIPOGRAFO=35
    ID=36
    FLOAT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(EZgraphParser.ExpContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = EZgraphParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e(self):
            return self.getTypedRuleContext(EZgraphParser.EContext,0)


        def exp(self):
            return self.getTypedRuleContext(EZgraphParser.ExpContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = EZgraphParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EZgraphParser.T__4, EZgraphParser.T__7, EZgraphParser.T__11, EZgraphParser.T__12, EZgraphParser.T__13, EZgraphParser.T__14, EZgraphParser.T__15, EZgraphParser.T__16, EZgraphParser.T__17, EZgraphParser.TIPOGRAFO, EZgraphParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.e()
                self.state = 37
                self.exp()
                pass
            elif token in [EZgraphParser.EOF, EZgraphParser.T__20]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(EZgraphParser.DeclaracionContext,0)


        def creacion(self):
            return self.getTypedRuleContext(EZgraphParser.CreacionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(EZgraphParser.AsignacionContext,0)


        def leer(self):
            return self.getTypedRuleContext(EZgraphParser.LeerContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(EZgraphParser.ImprimirContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(EZgraphParser.CicloContext,0)


        def pintar(self):
            return self.getTypedRuleContext(EZgraphParser.PintarContext,0)


        def funcion(self):
            return self.getTypedRuleContext(EZgraphParser.FuncionContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = EZgraphParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_e)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 42
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 43
                self.creacion()
                pass

            elif la_ == 3:
                self.state = 44
                self.asignacion()
                pass

            elif la_ == 4:
                self.state = 45
                self.leer()
                pass

            elif la_ == 5:
                self.state = 46
                self.imprimir()
                pass

            elif la_ == 6:
                self.state = 47
                self.ciclo()
                pass

            elif la_ == 7:
                self.state = 48
                self.pintar()
                pass

            elif la_ == 8:
                self.state = 49
                self.funcion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPOGRAFO(self):
            return self.getToken(EZgraphParser.TIPOGRAFO, 0)

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def INT(self):
            return self.getToken(EZgraphParser.INT, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_creacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreacion" ):
                listener.enterCreacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreacion" ):
                listener.exitCreacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreacion" ):
                return visitor.visitCreacion(self)
            else:
                return visitor.visitChildren(self)




    def creacion(self):

        localctx = EZgraphParser.CreacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_creacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(EZgraphParser.TIPOGRAFO)
            self.state = 53
            self.match(EZgraphParser.ID)
            self.state = 54
            self.match(EZgraphParser.T__0)
            self.state = 55
            self.match(EZgraphParser.INT)
            self.state = 56
            self.match(EZgraphParser.T__1)
            self.state = 57
            self.match(EZgraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(EZgraphParser.TipoContext,0)


        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(EZgraphParser.ValueContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = EZgraphParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.tipo()
                self.state = 60
                self.match(EZgraphParser.ID)
                self.state = 61
                self.match(EZgraphParser.T__3)
                self.state = 62
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.tipo()
                self.state = 65
                self.match(EZgraphParser.ID)
                self.state = 66
                self.match(EZgraphParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(EZgraphParser.ValueContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = EZgraphParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(EZgraphParser.ID)
            self.state = 71
            self.match(EZgraphParser.T__3)
            self.state = 72
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_leer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeer" ):
                listener.enterLeer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeer" ):
                listener.exitLeer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeer" ):
                return visitor.visitLeer(self)
            else:
                return visitor.visitChildren(self)




    def leer(self):

        localctx = EZgraphParser.LeerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_leer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EZgraphParser.T__4)
            self.state = 75
            self.match(EZgraphParser.T__5)
            self.state = 76
            self.match(EZgraphParser.ID)
            self.state = 77
            self.match(EZgraphParser.T__6)
            self.state = 78
            self.match(EZgraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EZgraphParser.STRING, 0)

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = EZgraphParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_imprimir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(EZgraphParser.T__7)
            self.state = 81
            self.match(EZgraphParser.T__5)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==EZgraphParser.STRING or _la==EZgraphParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 83
            self.match(EZgraphParser.T__6)
            self.state = 84
            self.match(EZgraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funciondeclaracion(self):
            return self.getTypedRuleContext(EZgraphParser.FunciondeclaracionContext,0)


        def STRING(self):
            return self.getToken(EZgraphParser.STRING, 0)

        def INT(self):
            return self.getToken(EZgraphParser.INT, 0)

        def FLOAT(self):
            return self.getToken(EZgraphParser.FLOAT, 0)

        def BOOLEANO(self):
            return self.getToken(EZgraphParser.BOOLEANO, 0)

        def lista(self):
            return self.getTypedRuleContext(EZgraphParser.ListaContext,0)


        def matriz(self):
            return self.getTypedRuleContext(EZgraphParser.MatrizContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = EZgraphParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.funciondeclaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(EZgraphParser.STRING)
                self.state = 88
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(EZgraphParser.INT)
                self.state = 90
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(EZgraphParser.FLOAT)
                self.state = 92
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.match(EZgraphParser.BOOLEANO)
                self.state = 94
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 95
                self.lista()
                self.state = 96
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.matriz()
                self.state = 99
                self.match(EZgraphParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunciondeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def FUNCIONCPARAM(self):
            return self.getToken(EZgraphParser.FUNCIONCPARAM, 0)

        def FUNCIONUNPARM(self):
            return self.getToken(EZgraphParser.FUNCIONUNPARM, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(EZgraphParser.INT)
            else:
                return self.getToken(EZgraphParser.INT, i)

        def FUNCIONDOPARAM(self):
            return self.getToken(EZgraphParser.FUNCIONDOPARAM, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_funciondeclaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunciondeclaracion" ):
                listener.enterFunciondeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunciondeclaracion" ):
                listener.exitFunciondeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunciondeclaracion" ):
                return visitor.visitFunciondeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def funciondeclaracion(self):

        localctx = EZgraphParser.FunciondeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funciondeclaracion)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(EZgraphParser.ID)
                self.state = 104
                self.match(EZgraphParser.T__8)
                self.state = 105
                self.match(EZgraphParser.FUNCIONCPARAM)
                self.state = 106
                self.match(EZgraphParser.T__5)
                self.state = 107
                self.match(EZgraphParser.T__6)
                self.state = 108
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(EZgraphParser.ID)
                self.state = 110
                self.match(EZgraphParser.T__8)
                self.state = 111
                self.match(EZgraphParser.FUNCIONUNPARM)
                self.state = 112
                self.match(EZgraphParser.T__5)
                self.state = 113
                self.match(EZgraphParser.INT)
                self.state = 114
                self.match(EZgraphParser.T__6)
                self.state = 115
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(EZgraphParser.ID)
                self.state = 117
                self.match(EZgraphParser.T__8)
                self.state = 118
                self.match(EZgraphParser.FUNCIONDOPARAM)
                self.state = 119
                self.match(EZgraphParser.T__5)
                self.state = 120
                self.match(EZgraphParser.INT)
                self.state = 121
                self.match(EZgraphParser.T__9)
                self.state = 122
                self.match(EZgraphParser.INT)
                self.state = 123
                self.match(EZgraphParser.T__6)
                self.state = 124
                self.match(EZgraphParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def ADDEDGE(self):
            return self.getToken(EZgraphParser.ADDEDGE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(EZgraphParser.INT)
            else:
                return self.getToken(EZgraphParser.INT, i)

        def DELETEEDGE(self):
            return self.getToken(EZgraphParser.DELETEEDGE, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = EZgraphParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcion)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(EZgraphParser.ID)
                self.state = 128
                self.match(EZgraphParser.T__8)
                self.state = 129
                self.match(EZgraphParser.ADDEDGE)
                self.state = 130
                self.match(EZgraphParser.T__5)
                self.state = 131
                self.match(EZgraphParser.INT)
                self.state = 132
                self.match(EZgraphParser.T__9)
                self.state = 133
                self.match(EZgraphParser.INT)
                self.state = 134
                self.match(EZgraphParser.T__6)
                self.state = 135
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(EZgraphParser.ID)
                self.state = 137
                self.match(EZgraphParser.T__8)
                self.state = 138
                self.match(EZgraphParser.ADDEDGE)
                self.state = 139
                self.match(EZgraphParser.T__5)
                self.state = 140
                self.match(EZgraphParser.INT)
                self.state = 141
                self.match(EZgraphParser.T__9)
                self.state = 142
                self.match(EZgraphParser.INT)
                self.state = 143
                self.match(EZgraphParser.T__9)
                self.state = 144
                self.match(EZgraphParser.INT)
                self.state = 145
                self.match(EZgraphParser.T__6)
                self.state = 146
                self.match(EZgraphParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(EZgraphParser.ID)
                self.state = 148
                self.match(EZgraphParser.T__8)
                self.state = 149
                self.match(EZgraphParser.DELETEEDGE)
                self.state = 150
                self.match(EZgraphParser.T__5)
                self.state = 151
                self.match(EZgraphParser.INT)
                self.state = 152
                self.match(EZgraphParser.T__9)
                self.state = 153
                self.match(EZgraphParser.INT)
                self.state = 154
                self.match(EZgraphParser.T__6)
                self.state = 155
                self.match(EZgraphParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(EZgraphParser.INT, 0)

        def FLOAT(self):
            return self.getToken(EZgraphParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(EZgraphParser.STRING, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = EZgraphParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lista)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(EZgraphParser.T__0)

                self.state = 159
                self.match(EZgraphParser.INT)
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 160
                        self.matchWildcard() 
                    self.state = 165
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 166
                self.match(EZgraphParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(EZgraphParser.T__0)

                self.state = 168
                self.match(EZgraphParser.FLOAT)
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 169
                        self.matchWildcard() 
                    self.state = 174
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 175
                self.match(EZgraphParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(EZgraphParser.T__0)

                self.state = 177
                self.match(EZgraphParser.STRING)
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 178
                        self.matchWildcard() 
                    self.state = 183
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 184
                self.match(EZgraphParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista(self):
            return self.getTypedRuleContext(EZgraphParser.ListaContext,0)


        def dentro(self):
            return self.getTypedRuleContext(EZgraphParser.DentroContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = EZgraphParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_matriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(EZgraphParser.T__0)
            self.state = 188
            self.lista()
            self.state = 189
            self.dentro()
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 190
                    self.matchWildcard() 
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 196
            self.match(EZgraphParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DentroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista(self):
            return self.getTypedRuleContext(EZgraphParser.ListaContext,0)


        def getRuleIndex(self):
            return EZgraphParser.RULE_dentro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDentro" ):
                listener.enterDentro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDentro" ):
                listener.exitDentro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDentro" ):
                return visitor.visitDentro(self)
            else:
                return visitor.visitChildren(self)




    def dentro(self):

        localctx = EZgraphParser.DentroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dentro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(EZgraphParser.T__2)
            self.state = 199
            self.lista()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PintarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EZgraphParser.ID, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_pintar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPintar" ):
                listener.enterPintar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPintar" ):
                listener.exitPintar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPintar" ):
                return visitor.visitPintar(self)
            else:
                return visitor.visitChildren(self)




    def pintar(self):

        localctx = EZgraphParser.PintarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_pintar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(EZgraphParser.ID)
            self.state = 202
            self.match(EZgraphParser.T__8)
            self.state = 203
            self.match(EZgraphParser.T__10)
            self.state = 204
            self.match(EZgraphParser.T__5)
            self.state = 205
            self.match(EZgraphParser.T__6)
            self.state = 206
            self.match(EZgraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPOGRAFO(self):
            return self.getToken(EZgraphParser.TIPOGRAFO, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = EZgraphParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EZgraphParser.T__11) | (1 << EZgraphParser.T__12) | (1 << EZgraphParser.T__13) | (1 << EZgraphParser.T__14) | (1 << EZgraphParser.T__15) | (1 << EZgraphParser.T__16) | (1 << EZgraphParser.TIPOGRAFO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EZgraphParser.ID)
            else:
                return self.getToken(EZgraphParser.ID, i)

        def exp(self):
            return self.getTypedRuleContext(EZgraphParser.ExpContext,0)


        def INT(self):
            return self.getToken(EZgraphParser.INT, 0)

        def getRuleIndex(self):
            return EZgraphParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo" ):
                return visitor.visitCiclo(self)
            else:
                return visitor.visitChildren(self)




    def ciclo(self):

        localctx = EZgraphParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ciclo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(EZgraphParser.T__17)
            self.state = 211
            self.match(EZgraphParser.ID)
            self.state = 212
            self.match(EZgraphParser.T__3)
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==EZgraphParser.INT or _la==EZgraphParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 214
            self.match(EZgraphParser.T__18)
            self.state = 215
            self.match(EZgraphParser.ID)
            self.state = 216
            self.match(EZgraphParser.T__19)
            self.state = 217
            self.exp()
            self.state = 218
            self.match(EZgraphParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





