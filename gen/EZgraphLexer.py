# Generated from C:/Users/a-zam/OneDrive/Documentos/Universidad/Lenguajes de programacion/proyectoFinal/EZgraph/grammar\EZgraph.g4 by ANTLR 4.9.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\66\u0215\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\3\2\3\2\3\3\3\3\3\4\3")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write(u"\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3")
        buf.write(u"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3")
        buf.write(u"\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write(u"\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3-")
        buf.write(u"\7-\u01bc\n-\f-\16-\u01bf\13-\3-\3-\3-\3-\3-\3.\3.\3")
        buf.write(u".\3.\7.\u01ca\n.\f.\16.\u01cd\13.\3.\3.\3/\3/\3/\3/\3")
        buf.write(u"/\3/\7/\u01d7\n/\f/\16/\u01da\13/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3\60\6\60\u01e5\n\60\r\60\16\60\u01e6\3\60\3\60")
        buf.write(u"\3\61\6\61\u01ec\n\61\r\61\16\61\u01ed\3\61\3\61\6\61")
        buf.write(u"\u01f2\n\61\r\61\16\61\u01f3\3\62\6\62\u01f7\n\62\r\62")
        buf.write(u"\16\62\u01f8\3\63\3\63\7\63\u01fd\n\63\f\63\16\63\u0200")
        buf.write(u"\13\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\5\64\u020d\n\64\3\65\3\65\7\65\u0211\n\65\f")
        buf.write(u"\65\16\65\u0214\13\65\5\u01bd\u01d8\u01fe\2\66\3\3\5")
        buf.write(u"\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write(u"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write(u"\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+")
        buf.write(u"U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66\3\2\b\4\2\f\f\17")
        buf.write(u"\17\5\2\13\f\17\17\"\"\3\2\62;\3\2\60\60\4\2C\\c|\6\2")
        buf.write(u"\62;C\\aac|\2\u021e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write(u"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write(u"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write(u"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write(u"\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write(u"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write(u"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write(u"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write(u"E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write(u"\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write(u"\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write(u"\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3")
        buf.write(u"\2\2\2\5m\3\2\2\2\7o\3\2\2\2\tq\3\2\2\2\13y\3\2\2\2\r")
        buf.write(u"\u0080\3\2\2\2\17\u0088\3\2\2\2\21\u0091\3\2\2\2\23\u0093")
        buf.write(u"\3\2\2\2\25\u0098\3\2\2\2\27\u009a\3\2\2\2\31\u009c\3")
        buf.write(u"\2\2\2\33\u00a2\3\2\2\2\35\u00a4\3\2\2\2\37\u00b0\3\2")
        buf.write(u"\2\2!\u00b9\3\2\2\2#\u00c2\3\2\2\2%\u00ca\3\2\2\2\'\u00d4")
        buf.write(u"\3\2\2\2)\u00e9\3\2\2\2+\u00f9\3\2\2\2-\u0105\3\2\2\2")
        buf.write(u"/\u0107\3\2\2\2\61\u0117\3\2\2\2\63\u012e\3\2\2\2\65")
        buf.write(u"\u0145\3\2\2\2\67\u014e\3\2\2\29\u0155\3\2\2\2;\u0169")
        buf.write(u"\3\2\2\2=\u016d\3\2\2\2?\u0171\3\2\2\2A\u0179\3\2\2\2")
        buf.write(u"C\u0184\3\2\2\2E\u018a\3\2\2\2G\u018e\3\2\2\2I\u0195")
        buf.write(u"\3\2\2\2K\u019c\3\2\2\2M\u01a1\3\2\2\2O\u01a6\3\2\2\2")
        buf.write(u"Q\u01ad\3\2\2\2S\u01b1\3\2\2\2U\u01b3\3\2\2\2W\u01b5")
        buf.write(u"\3\2\2\2Y\u01b7\3\2\2\2[\u01c5\3\2\2\2]\u01d0\3\2\2\2")
        buf.write(u"_\u01e4\3\2\2\2a\u01eb\3\2\2\2c\u01f6\3\2\2\2e\u01fa")
        buf.write(u"\3\2\2\2g\u020c\3\2\2\2i\u020e\3\2\2\2kl\7]\2\2l\4\3")
        buf.write(u"\2\2\2mn\7_\2\2n\6\3\2\2\2op\7=\2\2p\b\3\2\2\2qr\7P\2")
        buf.write(u"\2rs\7F\2\2st\7I\2\2tu\7t\2\2uv\7c\2\2vw\7r\2\2wx\7j")
        buf.write(u"\2\2x\n\3\2\2\2yz\7F\2\2z{\7I\2\2{|\7t\2\2|}\7c\2\2}")
        buf.write(u"~\7r\2\2~\177\7j\2\2\177\f\3\2\2\2\u0080\u0081\7F\2\2")
        buf.write(u"\u0081\u0082\7Y\2\2\u0082\u0083\7I\2\2\u0083\u0084\7")
        buf.write(u"t\2\2\u0084\u0085\7c\2\2\u0085\u0086\7r\2\2\u0086\u0087")
        buf.write(u"\7j\2\2\u0087\16\3\2\2\2\u0088\u0089\7P\2\2\u0089\u008a")
        buf.write(u"\7F\2\2\u008a\u008b\7Y\2\2\u008b\u008c\7I\2\2\u008c\u008d")
        buf.write(u"\7t\2\2\u008d\u008e\7c\2\2\u008e\u008f\7r\2\2\u008f\u0090")
        buf.write(u"\7j\2\2\u0090\20\3\2\2\2\u0091\u0092\7?\2\2\u0092\22")
        buf.write(u"\3\2\2\2\u0093\u0094\7t\2\2\u0094\u0095\7g\2\2\u0095")
        buf.write(u"\u0096\7c\2\2\u0096\u0097\7f\2\2\u0097\24\3\2\2\2\u0098")
        buf.write(u"\u0099\7*\2\2\u0099\26\3\2\2\2\u009a\u009b\7+\2\2\u009b")
        buf.write(u"\30\3\2\2\2\u009c\u009d\7r\2\2\u009d\u009e\7t\2\2\u009e")
        buf.write(u"\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1")
        buf.write(u"\32\3\2\2\2\u00a2\u00a3\7\60\2\2\u00a3\34\3\2\2\2\u00a4")
        buf.write(u"\u00a5\7i\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7v\2\2\u00a7")
        buf.write(u"\u00a8\7P\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7o\2\2\u00aa")
        buf.write(u"\u00ab\7G\2\2\u00ab\u00ac\7f\2\2\u00ac\u00ad\7i\2\2\u00ad")
        buf.write(u"\u00ae\7g\2\2\u00ae\u00af\7u\2\2\u00af\36\3\2\2\2\u00b0")
        buf.write(u"\u00b1\7i\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7v\2\2\u00b3")
        buf.write(u"\u00b4\7P\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7f\2\2\u00b6")
        buf.write(u"\u00b7\7g\2\2\u00b7\u00b8\7u\2\2\u00b8 \3\2\2\2\u00b9")
        buf.write(u"\u00ba\7i\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7v\2\2\u00bc")
        buf.write(u"\u00bd\7G\2\2\u00bd\u00be\7f\2\2\u00be\u00bf\7i\2\2\u00bf")
        buf.write(u"\u00c0\7g\2\2\u00c0\u00c1\7u\2\2\u00c1\"\3\2\2\2\u00c2")
        buf.write(u"\u00c3\7i\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write(u"\u00c6\7U\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7|\2\2\u00c8")
        buf.write(u"\u00c9\7g\2\2\u00c9$\3\2\2\2\u00ca\u00cb\7i\2\2\u00cb")
        buf.write(u"\u00cc\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7O\2\2\u00ce")
        buf.write(u"\u00cf\7c\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write(u"\u00d2\7k\2\2\u00d2\u00d3\7z\2\2\u00d3&\3\2\2\2\u00d4")
        buf.write(u"\u00d5\7i\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7v\2\2\u00d7")
        buf.write(u"\u00d8\7F\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7u\2\2\u00da")
        buf.write(u"\u00db\7v\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write(u"\u00de\7e\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7u\2\2\u00e0")
        buf.write(u"\u00e1\7H\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7q\2\2\u00e3")
        buf.write(u"\u00e4\7o\2\2\u00e4\u00e5\7P\2\2\u00e5\u00e6\7q\2\2\u00e6")
        buf.write(u"\u00e7\7f\2\2\u00e7\u00e8\7g\2\2\u00e8(\3\2\2\2\u00e9")
        buf.write(u"\u00ea\7i\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7v\2\2\u00ec")
        buf.write(u"\u00ed\7C\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7n\2\2\u00ef")
        buf.write(u"\u00f0\7F\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7u\2\2\u00f2")
        buf.write(u"\u00f3\7v\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7p\2\2\u00f5")
        buf.write(u"\u00f6\7e\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7u\2\2\u00f8")
        buf.write(u"*\3\2\2\2\u00f9\u00fa\7i\2\2\u00fa\u00fb\7g\2\2\u00fb")
        buf.write(u"\u00fc\7v\2\2\u00fc\u00fd\7F\2\2\u00fd\u00fe\7k\2\2\u00fe")
        buf.write(u"\u00ff\7u\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7c\2\2\u0101")
        buf.write(u"\u0102\7p\2\2\u0102\u0103\7e\2\2\u0103\u0104\7g\2\2\u0104")
        buf.write(u",\3\2\2\2\u0105\u0106\7.\2\2\u0106.\3\2\2\2\u0107\u0108")
        buf.write(u"\7i\2\2\u0108\u0109\7g\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write(u"\7U\2\2\u010b\u010c\7j\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write(u"\7t\2\2\u010e\u010f\7v\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write(u"\7u\2\2\u0111\u0112\7v\2\2\u0112\u0113\7R\2\2\u0113\u0114")
        buf.write(u"\7c\2\2\u0114\u0115\7v\2\2\u0115\u0116\7j\2\2\u0116\60")
        buf.write(u"\3\2\2\2\u0117\u0118\7i\2\2\u0118\u0119\7g\2\2\u0119")
        buf.write(u"\u011a\7v\2\2\u011a\u011b\7O\2\2\u011b\u011c\7k\2\2\u011c")
        buf.write(u"\u011d\7p\2\2\u011d\u011e\7k\2\2\u011e\u011f\7o\2\2\u011f")
        buf.write(u"\u0120\7w\2\2\u0120\u0121\7p\2\2\u0121\u0122\7U\2\2\u0122")
        buf.write(u"\u0123\7r\2\2\u0123\u0124\7c\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write(u"\u0126\7p\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128")
        buf.write(u"\u0129\7i\2\2\u0129\u012a\7V\2\2\u012a\u012b\7t\2\2\u012b")
        buf.write(u"\u012c\7g\2\2\u012c\u012d\7g\2\2\u012d\62\3\2\2\2\u012e")
        buf.write(u"\u012f\7i\2\2\u012f\u0130\7g\2\2\u0130\u0131\7v\2\2\u0131")
        buf.write(u"\u0132\7O\2\2\u0132\u0133\7c\2\2\u0133\u0134\7z\2\2\u0134")
        buf.write(u"\u0135\7k\2\2\u0135\u0136\7o\2\2\u0136\u0137\7w\2\2\u0137")
        buf.write(u"\u0138\7p\2\2\u0138\u0139\7U\2\2\u0139\u013a\7r\2\2\u013a")
        buf.write(u"\u013b\7c\2\2\u013b\u013c\7p\2\2\u013c\u013d\7p\2\2\u013d")
        buf.write(u"\u013e\7k\2\2\u013e\u013f\7p\2\2\u013f\u0140\7i\2\2\u0140")
        buf.write(u"\u0141\7V\2\2\u0141\u0142\7t\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write(u"\u0144\7g\2\2\u0144\64\3\2\2\2\u0145\u0146\7j\2\2\u0146")
        buf.write(u"\u0147\7c\2\2\u0147\u0148\7u\2\2\u0148\u0149\7E\2\2\u0149")
        buf.write(u"\u014a\7{\2\2\u014a\u014b\7e\2\2\u014b\u014c\7n\2\2\u014c")
        buf.write(u"\u014d\7g\2\2\u014d\66\3\2\2\2\u014e\u014f\7i\2\2\u014f")
        buf.write(u"\u0150\7g\2\2\u0150\u0151\7v\2\2\u0151\u0152\7U\2\2\u0152")
        buf.write(u"\u0153\7E\2\2\u0153\u0154\7E\2\2\u01548\3\2\2\2\u0155")
        buf.write(u"\u0156\7i\2\2\u0156\u0157\7g\2\2\u0157\u0158\7v\2\2\u0158")
        buf.write(u"\u0159\7V\2\2\u0159\u015a\7q\2\2\u015a\u015b\7r\2\2\u015b")
        buf.write(u"\u015c\7q\2\2\u015c\u015d\7n\2\2\u015d\u015e\7q\2\2\u015e")
        buf.write(u"\u015f\7i\2\2\u015f\u0160\7k\2\2\u0160\u0161\7e\2\2\u0161")
        buf.write(u"\u0162\7c\2\2\u0162\u0163\7n\2\2\u0163\u0164\7Q\2\2\u0164")
        buf.write(u"\u0165\7t\2\2\u0165\u0166\7f\2\2\u0166\u0167\7g\2\2\u0167")
        buf.write(u"\u0168\7t\2\2\u0168:\3\2\2\2\u0169\u016a\7D\2\2\u016a")
        buf.write(u"\u016b\7H\2\2\u016b\u016c\7U\2\2\u016c<\3\2\2\2\u016d")
        buf.write(u"\u016e\7F\2\2\u016e\u016f\7H\2\2\u016f\u0170\7U\2\2\u0170")
        buf.write(u">\3\2\2\2\u0171\u0172\7c\2\2\u0172\u0173\7f\2\2\u0173")
        buf.write(u"\u0174\7f\2\2\u0174\u0175\7G\2\2\u0175\u0176\7f\2\2\u0176")
        buf.write(u"\u0177\7i\2\2\u0177\u0178\7g\2\2\u0178@\3\2\2\2\u0179")
        buf.write(u"\u017a\7f\2\2\u017a\u017b\7g\2\2\u017b\u017c\7n\2\2\u017c")
        buf.write(u"\u017d\7g\2\2\u017d\u017e\7v\2\2\u017e\u017f\7g\2\2\u017f")
        buf.write(u"\u0180\7G\2\2\u0180\u0181\7f\2\2\u0181\u0182\7i\2\2\u0182")
        buf.write(u"\u0183\7g\2\2\u0183B\3\2\2\2\u0184\u0185\7r\2\2\u0185")
        buf.write(u"\u0186\7c\2\2\u0186\u0187\7k\2\2\u0187\u0188\7p\2\2\u0188")
        buf.write(u"\u0189\7v\2\2\u0189D\3\2\2\2\u018a\u018b\7k\2\2\u018b")
        buf.write(u"\u018c\7p\2\2\u018c\u018d\7v\2\2\u018dF\3\2\2\2\u018e")
        buf.write(u"\u018f\7u\2\2\u018f\u0190\7v\2\2\u0190\u0191\7t\2\2\u0191")
        buf.write(u"\u0192\7k\2\2\u0192\u0193\7p\2\2\u0193\u0194\7i\2\2\u0194")
        buf.write(u"H\3\2\2\2\u0195\u0196\7f\2\2\u0196\u0197\7q\2\2\u0197")
        buf.write(u"\u0198\7w\2\2\u0198\u0199\7d\2\2\u0199\u019a\7n\2\2\u019a")
        buf.write(u"\u019b\7g\2\2\u019bJ\3\2\2\2\u019c\u019d\7d\2\2\u019d")
        buf.write(u"\u019e\7q\2\2\u019e\u019f\7q\2\2\u019f\u01a0\7n\2\2\u01a0")
        buf.write(u"L\3\2\2\2\u01a1\u01a2\7N\2\2\u01a2\u01a3\7k\2\2\u01a3")
        buf.write(u"\u01a4\7u\2\2\u01a4\u01a5\7v\2\2\u01a5N\3\2\2\2\u01a6")
        buf.write(u"\u01a7\7O\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9\7v\2\2\u01a9")
        buf.write(u"\u01aa\7t\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac\7z\2\2\u01ac")
        buf.write(u"P\3\2\2\2\u01ad\u01ae\7h\2\2\u01ae\u01af\7q\2\2\u01af")
        buf.write(u"\u01b0\7t\2\2\u01b0R\3\2\2\2\u01b1\u01b2\7<\2\2\u01b2")
        buf.write(u"T\3\2\2\2\u01b3\u01b4\7}\2\2\u01b4V\3\2\2\2\u01b5\u01b6")
        buf.write(u"\7\177\2\2\u01b6X\3\2\2\2\u01b7\u01b8\7\61\2\2\u01b8")
        buf.write(u"\u01b9\7,\2\2\u01b9\u01bd\3\2\2\2\u01ba\u01bc\13\2\2")
        buf.write(u"\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01be")
        buf.write(u"\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf")
        buf.write(u"\u01bd\3\2\2\2\u01c0\u01c1\7,\2\2\u01c1\u01c2\7\61\2")
        buf.write(u"\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\b-\2\2\u01c4Z\3\2")
        buf.write(u"\2\2\u01c5\u01c6\7\61\2\2\u01c6\u01c7\7\61\2\2\u01c7")
        buf.write(u"\u01cb\3\2\2\2\u01c8\u01ca\n\2\2\2\u01c9\u01c8\3\2\2")
        buf.write(u"\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc")
        buf.write(u"\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce")
        buf.write(u"\u01cf\b.\2\2\u01cf\\\3\2\2\2\u01d0\u01d1\7\u00f2\2\2")
        buf.write(u"\u01d1\u01d2\7\u017a\2\2\u01d2\u01d3\7\u02de\2\2\u01d3")
        buf.write(u"\u01d4\7\u0162\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d7\13")
        buf.write(u"\2\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8")
        buf.write(u"\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db\3\2\2")
        buf.write(u"\2\u01da\u01d8\3\2\2\2\u01db\u01dc\7\u00f2\2\2\u01dc")
        buf.write(u"\u01dd\7\u017a\2\2\u01dd\u01de\7\u02de\2\2\u01de\u01df")
        buf.write(u"\7\u0162\2\2\u01df\u01e0\7\"\2\2\u01e0\u01e1\3\2\2\2")
        buf.write(u"\u01e1\u01e2\b/\2\2\u01e2^\3\2\2\2\u01e3\u01e5\t\3\2")
        buf.write(u"\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e4")
        buf.write(u"\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8")
        buf.write(u"\u01e9\b\60\2\2\u01e9`\3\2\2\2\u01ea\u01ec\t\4\2\2\u01eb")
        buf.write(u"\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01eb\3\2\2")
        buf.write(u"\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f1")
        buf.write(u"\t\5\2\2\u01f0\u01f2\t\4\2\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write(u"\u01f3\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2")
        buf.write(u"\2\u01f4b\3\2\2\2\u01f5\u01f7\t\4\2\2\u01f6\u01f5\3\2")
        buf.write(u"\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9")
        buf.write(u"\3\2\2\2\u01f9d\3\2\2\2\u01fa\u01fe\7$\2\2\u01fb\u01fd")
        buf.write(u"\13\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe")
        buf.write(u"\u01ff\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u0201\3\2\2")
        buf.write(u"\2\u0200\u01fe\3\2\2\2\u0201\u0202\7$\2\2\u0202f\3\2")
        buf.write(u"\2\2\u0203\u0204\7v\2\2\u0204\u0205\7t\2\2\u0205\u0206")
        buf.write(u"\7w\2\2\u0206\u020d\7g\2\2\u0207\u0208\7h\2\2\u0208\u0209")
        buf.write(u"\7c\2\2\u0209\u020a\7n\2\2\u020a\u020b\7u\2\2\u020b\u020d")
        buf.write(u"\7g\2\2\u020c\u0203\3\2\2\2\u020c\u0207\3\2\2\2\u020d")
        buf.write(u"h\3\2\2\2\u020e\u0212\t\6\2\2\u020f\u0211\t\7\2\2\u0210")
        buf.write(u"\u020f\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2")
        buf.write(u"\2\u0212\u0213\3\2\2\2\u0213j\3\2\2\2\u0214\u0212\3\2")
        buf.write(u"\2\2\r\2\u01bd\u01cb\u01d8\u01e6\u01ed\u01f3\u01f8\u01fe")
        buf.write(u"\u020c\u0212\3\b\2\2")
        return buf.getvalue()


class EZgraphLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    COMMENT = 44
    LINE_COMMENT = 45
    EASTEREGG = 46
    WS = 47
    DOUBLE = 48
    INT = 49
    STRING = 50
    BOOLEANO = 51
    ID = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'['", u"']'", u"';'", u"'NDGraph'", u"'DGraph'", u"'DWGraph'", 
            u"'NDWGraph'", u"'='", u"'read'", u"'('", u"')'", u"'print'", 
            u"'.'", u"'getNumEdges'", u"'getNodes'", u"'getEdges'", u"'getSize'", 
            u"'getMatrix'", u"'getDistancesFromNode'", u"'getAllDistances'", 
            u"'getDistance'", u"','", u"'getShortestPath'", u"'getMinimunSpanningTree'", 
            u"'getMaximunSpanningTree'", u"'hasCycle'", u"'getSCC'", u"'getTopologicalOrder'", 
            u"'BFS'", u"'DFS'", u"'addEdge'", u"'deleteEdge'", u"'paint'", 
            u"'int'", u"'string'", u"'double'", u"'bool'", u"'List'", u"'Matrix'", 
            u"'for'", u"':'", u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>",
            u"COMMENT", u"LINE_COMMENT", u"EASTEREGG", u"WS", u"DOUBLE", 
            u"INT", u"STRING", u"BOOLEANO", u"ID" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"T__14", u"T__15", u"T__16", u"T__17", 
                  u"T__18", u"T__19", u"T__20", u"T__21", u"T__22", u"T__23", 
                  u"T__24", u"T__25", u"T__26", u"T__27", u"T__28", u"T__29", 
                  u"T__30", u"T__31", u"T__32", u"T__33", u"T__34", u"T__35", 
                  u"T__36", u"T__37", u"T__38", u"T__39", u"T__40", u"T__41", 
                  u"T__42", u"COMMENT", u"LINE_COMMENT", u"EASTEREGG", u"WS", 
                  u"DOUBLE", u"INT", u"STRING", u"BOOLEANO", u"ID" ]

    grammarFileName = u"EZgraph.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(EZgraphLexer, self).__init__(input, output=output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


