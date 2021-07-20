# Generated from C:/Users/a-zam/OneDrive/Documentos/Universidad/Lenguajes de programacion/proyectoFinal/EZgraph/grammar\EZgraph.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u01e8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u009e\n\27\f\27\16\27\u00a1\13\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\7\30\u00ac\n\30\f\30\16\30\u00af")
        buf.write("\13\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u00b9")
        buf.write("\n\31\f\31\16\31\u00bc\13\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\6\32\u00c7\n\32\r\32\16\32\u00c8")
        buf.write("\3\32\3\32\3\33\6\33\u00ce\n\33\r\33\16\33\u00cf\3\33")
        buf.write("\3\33\6\33\u00d4\n\33\r\33\16\33\u00d5\3\34\6\34\u00d9")
        buf.write("\n\34\r\34\16\34\u00da\3\35\3\35\7\35\u00df\n\35\f\35")
        buf.write("\16\35\u00e2\13\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u00ef\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0187\n\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \5 \u01a3\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01e0\n")
        buf.write("$\3%\3%\7%\u01e4\n%\f%\16%\u01e7\13%\5\u009f\u00ba\u00e0")
        buf.write("\2&\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&\3")
        buf.write("\2\b\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3\2\62;\3\2\60\60")
        buf.write("\4\2C\\c|\6\2\62;C\\aac|\2\u0201\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\3K\3\2\2\2\5M\3\2\2")
        buf.write("\2\7O\3\2\2\2\tQ\3\2\2\2\13S\3\2\2\2\rX\3\2\2\2\17Z\3")
        buf.write("\2\2\2\21\\\3\2\2\2\23b\3\2\2\2\25d\3\2\2\2\27f\3\2\2")
        buf.write("\2\31l\3\2\2\2\33p\3\2\2\2\35w\3\2\2\2\37~\3\2\2\2!\u0083")
        buf.write("\3\2\2\2#\u0088\3\2\2\2%\u008f\3\2\2\2\'\u0093\3\2\2\2")
        buf.write(")\u0095\3\2\2\2+\u0097\3\2\2\2-\u0099\3\2\2\2/\u00a7\3")
        buf.write("\2\2\2\61\u00b2\3\2\2\2\63\u00c6\3\2\2\2\65\u00cd\3\2")
        buf.write("\2\2\67\u00d8\3\2\2\29\u00dc\3\2\2\2;\u00ee\3\2\2\2=\u0186")
        buf.write("\3\2\2\2?\u01a2\3\2\2\2A\u01a4\3\2\2\2C\u01b0\3\2\2\2")
        buf.write("E\u01b8\3\2\2\2G\u01df\3\2\2\2I\u01e1\3\2\2\2KL\7]\2\2")
        buf.write("L\4\3\2\2\2MN\7_\2\2N\6\3\2\2\2OP\7=\2\2P\b\3\2\2\2QR")
        buf.write("\7?\2\2R\n\3\2\2\2ST\7t\2\2TU\7g\2\2UV\7c\2\2VW\7f\2\2")
        buf.write("W\f\3\2\2\2XY\7*\2\2Y\16\3\2\2\2Z[\7+\2\2[\20\3\2\2\2")
        buf.write("\\]\7r\2\2]^\7t\2\2^_\7k\2\2_`\7p\2\2`a\7v\2\2a\22\3\2")
        buf.write("\2\2bc\7\60\2\2c\24\3\2\2\2de\7.\2\2e\26\3\2\2\2fg\7r")
        buf.write("\2\2gh\7c\2\2hi\7k\2\2ij\7p\2\2jk\7v\2\2k\30\3\2\2\2l")
        buf.write("m\7k\2\2mn\7p\2\2no\7v\2\2o\32\3\2\2\2pq\7u\2\2qr\7v\2")
        buf.write("\2rs\7t\2\2st\7k\2\2tu\7p\2\2uv\7i\2\2v\34\3\2\2\2wx\7")
        buf.write("f\2\2xy\7q\2\2yz\7w\2\2z{\7d\2\2{|\7n\2\2|}\7g\2\2}\36")
        buf.write("\3\2\2\2~\177\7d\2\2\177\u0080\7q\2\2\u0080\u0081\7q\2")
        buf.write("\2\u0081\u0082\7n\2\2\u0082 \3\2\2\2\u0083\u0084\7N\2")
        buf.write("\2\u0084\u0085\7k\2\2\u0085\u0086\7u\2\2\u0086\u0087\7")
        buf.write("v\2\2\u0087\"\3\2\2\2\u0088\u0089\7O\2\2\u0089\u008a\7")
        buf.write("c\2\2\u008a\u008b\7v\2\2\u008b\u008c\7t\2\2\u008c\u008d")
        buf.write("\7k\2\2\u008d\u008e\7z\2\2\u008e$\3\2\2\2\u008f\u0090")
        buf.write("\7h\2\2\u0090\u0091\7q\2\2\u0091\u0092\7t\2\2\u0092&\3")
        buf.write("\2\2\2\u0093\u0094\7<\2\2\u0094(\3\2\2\2\u0095\u0096\7")
        buf.write("}\2\2\u0096*\3\2\2\2\u0097\u0098\7\177\2\2\u0098,\3\2")
        buf.write("\2\2\u0099\u009a\7\61\2\2\u009a\u009b\7,\2\2\u009b\u009f")
        buf.write("\3\2\2\2\u009c\u009e\13\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u00a0\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7")
        buf.write(",\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\b\27\2\2\u00a6.\3\2\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9")
        buf.write("\7\61\2\2\u00a9\u00ad\3\2\2\2\u00aa\u00ac\n\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3")
        buf.write("\2\2\2\u00b0\u00b1\b\30\2\2\u00b1\60\3\2\2\2\u00b2\u00b3")
        buf.write("\7\u00f2\2\2\u00b3\u00b4\7\u017a\2\2\u00b4\u00b5\7\u02de")
        buf.write("\2\2\u00b5\u00b6\7\u0162\2\2\u00b6\u00ba\3\2\2\2\u00b7")
        buf.write("\u00b9\13\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2")
        buf.write("\2\u00ba\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bd")
        buf.write("\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\7\u00f2\2\2\u00be")
        buf.write("\u00bf\7\u017a\2\2\u00bf\u00c0\7\u02de\2\2\u00c0\u00c1")
        buf.write("\7\u0162\2\2\u00c1\u00c2\7\"\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c4\b\31\2\2\u00c4\62\3\2\2\2\u00c5\u00c7\t\3\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\b")
        buf.write("\32\2\2\u00cb\64\3\2\2\2\u00cc\u00ce\t\4\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\t\5\2\2")
        buf.write("\u00d2\u00d4\t\4\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\66")
        buf.write("\3\2\2\2\u00d7\u00d9\t\4\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db8\3\2\2\2\u00dc\u00e0\7$\2\2\u00dd\u00df\13\2\2")
        buf.write("\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e3\u00e4\7$\2\2\u00e4:\3\2\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7w\2\2\u00e8")
        buf.write("\u00ef\7g\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb\7c\2\2\u00eb")
        buf.write("\u00ec\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ef\7g\2\2\u00ee")
        buf.write("\u00e5\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ef<\3\2\2\2\u00f0")
        buf.write("\u00f1\7i\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7v\2\2\u00f3")
        buf.write("\u00f4\7P\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7o\2\2\u00f6")
        buf.write("\u00f7\7G\2\2\u00f7\u00f8\7f\2\2\u00f8\u00f9\7i\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\u0187\7u\2\2\u00fb\u00fc\7i\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7P\2\2\u00ff")
        buf.write("\u0100\7q\2\2\u0100\u0101\7f\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("\u0187\7u\2\2\u0103\u0104\7i\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("\u0106\7v\2\2\u0106\u0107\7G\2\2\u0107\u0108\7f\2\2\u0108")
        buf.write("\u0109\7i\2\2\u0109\u010a\7g\2\2\u010a\u0187\7u\2\2\u010b")
        buf.write("\u010c\7i\2\2\u010c\u010d\7g\2\2\u010d\u010e\7v\2\2\u010e")
        buf.write("\u010f\7U\2\2\u010f\u0110\7k\2\2\u0110\u0111\7|\2\2\u0111")
        buf.write("\u0187\7g\2\2\u0112\u0113\7i\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("\u0115\7v\2\2\u0115\u0116\7O\2\2\u0116\u0117\7c\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118\u0119\7t\2\2\u0119\u011a\7k\2\2\u011a")
        buf.write("\u0187\7z\2\2\u011b\u011c\7i\2\2\u011c\u011d\7g\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\u011f\7C\2\2\u011f\u0120\7n\2\2\u0120")
        buf.write("\u0121\7n\2\2\u0121\u0122\7F\2\2\u0122\u0123\7k\2\2\u0123")
        buf.write("\u0124\7u\2\2\u0124\u0125\7v\2\2\u0125\u0126\7c\2\2\u0126")
        buf.write("\u0127\7p\2\2\u0127\u0128\7e\2\2\u0128\u0129\7g\2\2\u0129")
        buf.write("\u0187\7u\2\2\u012a\u012b\7i\2\2\u012b\u012c\7g\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7U\2\2\u012e\u012f\7j\2\2\u012f")
        buf.write("\u0130\7q\2\2\u0130\u0131\7t\2\2\u0131\u0132\7v\2\2\u0132")
        buf.write("\u0133\7g\2\2\u0133\u0134\7u\2\2\u0134\u0135\7v\2\2\u0135")
        buf.write("\u0136\7R\2\2\u0136\u0137\7c\2\2\u0137\u0138\7v\2\2\u0138")
        buf.write("\u0187\7j\2\2\u0139\u013a\7i\2\2\u013a\u013b\7g\2\2\u013b")
        buf.write("\u013c\7v\2\2\u013c\u013d\7O\2\2\u013d\u013e\7k\2\2\u013e")
        buf.write("\u013f\7p\2\2\u013f\u0140\7k\2\2\u0140\u0141\7o\2\2\u0141")
        buf.write("\u0142\7w\2\2\u0142\u0143\7p\2\2\u0143\u0144\7U\2\2\u0144")
        buf.write("\u0145\7r\2\2\u0145\u0146\7c\2\2\u0146\u0147\7p\2\2\u0147")
        buf.write("\u0148\7p\2\2\u0148\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a")
        buf.write("\u014b\7i\2\2\u014b\u014c\7V\2\2\u014c\u014d\7t\2\2\u014d")
        buf.write("\u014e\7g\2\2\u014e\u0187\7g\2\2\u014f\u0150\7i\2\2\u0150")
        buf.write("\u0151\7g\2\2\u0151\u0152\7v\2\2\u0152\u0153\7O\2\2\u0153")
        buf.write("\u0154\7c\2\2\u0154\u0155\7z\2\2\u0155\u0156\7k\2\2\u0156")
        buf.write("\u0157\7o\2\2\u0157\u0158\7w\2\2\u0158\u0159\7p\2\2\u0159")
        buf.write("\u015a\7U\2\2\u015a\u015b\7r\2\2\u015b\u015c\7c\2\2\u015c")
        buf.write("\u015d\7p\2\2\u015d\u015e\7p\2\2\u015e\u015f\7k\2\2\u015f")
        buf.write("\u0160\7p\2\2\u0160\u0161\7i\2\2\u0161\u0162\7V\2\2\u0162")
        buf.write("\u0163\7t\2\2\u0163\u0164\7g\2\2\u0164\u0187\7g\2\2\u0165")
        buf.write("\u0166\7j\2\2\u0166\u0167\7c\2\2\u0167\u0168\7u\2\2\u0168")
        buf.write("\u0169\7E\2\2\u0169\u016a\7{\2\2\u016a\u016b\7e\2\2\u016b")
        buf.write("\u016c\7n\2\2\u016c\u0187\7g\2\2\u016d\u016e\7i\2\2\u016e")
        buf.write("\u016f\7g\2\2\u016f\u0170\7v\2\2\u0170\u0171\7U\2\2\u0171")
        buf.write("\u0172\7E\2\2\u0172\u0187\7E\2\2\u0173\u0174\7i\2\2\u0174")
        buf.write("\u0175\7g\2\2\u0175\u0176\7v\2\2\u0176\u0177\7V\2\2\u0177")
        buf.write("\u0178\7q\2\2\u0178\u0179\7r\2\2\u0179\u017a\7q\2\2\u017a")
        buf.write("\u017b\7n\2\2\u017b\u017c\7q\2\2\u017c\u017d\7i\2\2\u017d")
        buf.write("\u017e\7k\2\2\u017e\u017f\7e\2\2\u017f\u0180\7c\2\2\u0180")
        buf.write("\u0181\7n\2\2\u0181\u0182\7Q\2\2\u0182\u0183\7t\2\2\u0183")
        buf.write("\u0184\7f\2\2\u0184\u0185\7g\2\2\u0185\u0187\7t\2\2\u0186")
        buf.write("\u00f0\3\2\2\2\u0186\u00fb\3\2\2\2\u0186\u0103\3\2\2\2")
        buf.write("\u0186\u010b\3\2\2\2\u0186\u0112\3\2\2\2\u0186\u011b\3")
        buf.write("\2\2\2\u0186\u012a\3\2\2\2\u0186\u0139\3\2\2\2\u0186\u014f")
        buf.write("\3\2\2\2\u0186\u0165\3\2\2\2\u0186\u016d\3\2\2\2\u0186")
        buf.write("\u0173\3\2\2\2\u0187>\3\2\2\2\u0188\u0189\7i\2\2\u0189")
        buf.write("\u018a\7g\2\2\u018a\u018b\7v\2\2\u018b\u018c\7F\2\2\u018c")
        buf.write("\u018d\7k\2\2\u018d\u018e\7u\2\2\u018e\u018f\7v\2\2\u018f")
        buf.write("\u0190\7c\2\2\u0190\u0191\7p\2\2\u0191\u0192\7e\2\2\u0192")
        buf.write("\u0193\7g\2\2\u0193\u0194\7u\2\2\u0194\u0195\7H\2\2\u0195")
        buf.write("\u0196\7t\2\2\u0196\u0197\7q\2\2\u0197\u0198\7o\2\2\u0198")
        buf.write("\u0199\7P\2\2\u0199\u019a\7q\2\2\u019a\u019b\7f\2\2\u019b")
        buf.write("\u01a3\7g\2\2\u019c\u019d\7D\2\2\u019d\u019e\7H\2\2\u019e")
        buf.write("\u01a3\7U\2\2\u019f\u01a0\7F\2\2\u01a0\u01a1\7H\2\2\u01a1")
        buf.write("\u01a3\7U\2\2\u01a2\u0188\3\2\2\2\u01a2\u019c\3\2\2\2")
        buf.write("\u01a2\u019f\3\2\2\2\u01a3@\3\2\2\2\u01a4\u01a5\7i\2\2")
        buf.write("\u01a5\u01a6\7g\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8\7F")
        buf.write("\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa\7u\2\2\u01aa\u01ab")
        buf.write("\7v\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ad\7p\2\2\u01ad\u01ae")
        buf.write("\7e\2\2\u01ae\u01af\7g\2\2\u01afB\3\2\2\2\u01b0\u01b1")
        buf.write("\7c\2\2\u01b1\u01b2\7f\2\2\u01b2\u01b3\7f\2\2\u01b3\u01b4")
        buf.write("\7G\2\2\u01b4\u01b5\7f\2\2\u01b5\u01b6\7i\2\2\u01b6\u01b7")
        buf.write("\7g\2\2\u01b7D\3\2\2\2\u01b8\u01b9\7f\2\2\u01b9\u01ba")
        buf.write("\7g\2\2\u01ba\u01bb\7n\2\2\u01bb\u01bc\7g\2\2\u01bc\u01bd")
        buf.write("\7v\2\2\u01bd\u01be\7g\2\2\u01be\u01bf\7G\2\2\u01bf\u01c0")
        buf.write("\7f\2\2\u01c0\u01c1\7i\2\2\u01c1\u01c2\7g\2\2\u01c2F\3")
        buf.write("\2\2\2\u01c3\u01c4\7P\2\2\u01c4\u01c5\7F\2\2\u01c5\u01c6")
        buf.write("\7I\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8\7c\2\2\u01c8\u01c9")
        buf.write("\7r\2\2\u01c9\u01e0\7j\2\2\u01ca\u01cb\7F\2\2\u01cb\u01cc")
        buf.write("\7I\2\2\u01cc\u01cd\7t\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf")
        buf.write("\7r\2\2\u01cf\u01e0\7j\2\2\u01d0\u01d1\7F\2\2\u01d1\u01d2")
        buf.write("\7Y\2\2\u01d2\u01d3\7I\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5")
        buf.write("\7c\2\2\u01d5\u01d6\7r\2\2\u01d6\u01e0\7j\2\2\u01d7\u01d8")
        buf.write("\7P\2\2\u01d8\u01d9\7F\2\2\u01d9\u01da\7Y\2\2\u01da\u01db")
        buf.write("\7I\2\2\u01db\u01dc\7t\2\2\u01dc\u01dd\7c\2\2\u01dd\u01de")
        buf.write("\7r\2\2\u01de\u01e0\7j\2\2\u01df\u01c3\3\2\2\2\u01df\u01ca")
        buf.write("\3\2\2\2\u01df\u01d0\3\2\2\2\u01df\u01d7\3\2\2\2\u01e0")
        buf.write("H\3\2\2\2\u01e1\u01e5\t\6\2\2\u01e2\u01e4\t\7\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6J\3\2\2\2\u01e7\u01e5\3\2\2")
        buf.write("\2\20\2\u009f\u00ad\u00ba\u00c8\u00cf\u00d5\u00da\u00e0")
        buf.write("\u00ee\u0186\u01a2\u01df\u01e5\3\b\2\2")
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
    COMMENT = 22
    LINE_COMMENT = 23
    EASTEREGG = 24
    WS = 25
    DOUBLE = 26
    INT = 27
    STRING = 28
    BOOLEANO = 29
    FUNCIONCPARAM = 30
    FUNCIONUNPARM = 31
    FUNCIONDOPARAM = 32
    ADDEDGE = 33
    DELETEEDGE = 34
    TIPOGRAFO = 35
    ID = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "';'", "'='", "'read'", "'('", "')'", "'print'", 
            "'.'", "','", "'paint'", "'int'", "'string'", "'double'", "'bool'", 
            "'List'", "'Matrix'", "'for'", "':'", "'{'", "'}'", "'getDistance'", 
            "'addEdge'", "'deleteEdge'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "EASTEREGG", "WS", "DOUBLE", "INT", 
            "STRING", "BOOLEANO", "FUNCIONCPARAM", "FUNCIONUNPARM", "FUNCIONDOPARAM", 
            "ADDEDGE", "DELETEEDGE", "TIPOGRAFO", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "COMMENT", "LINE_COMMENT", "EASTEREGG", "WS", 
                  "DOUBLE", "INT", "STRING", "BOOLEANO", "FUNCIONCPARAM", 
                  "FUNCIONUNPARM", "FUNCIONDOPARAM", "ADDEDGE", "DELETEEDGE", 
                  "TIPOGRAFO", "ID" ]

    grammarFileName = "EZgraph.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


