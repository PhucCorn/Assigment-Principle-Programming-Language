# Generated from c:\D\BKU\PPL\as3\assignment3-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u023c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0091\n\3\f\3")
        buf.write("\16\3\u0094\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u009c\n\4")
        buf.write("\f\4\16\4\u009f\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\7\5\u00aa\n\5\f\5\16\5\u00ad\13\5\5\5\u00af\n\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ba\n\6\3\7\3\7")
        buf.write("\3\7\7\7\u00bf\n\7\f\7\16\7\u00c2\13\7\3\7\3\7\6\7\u00c6")
        buf.write("\n\7\r\7\16\7\u00c7\7\7\u00ca\n\7\f\7\16\7\u00cd\13\7")
        buf.write("\3\7\5\7\u00d0\n\7\3\b\3\b\3\t\3\t\3\t\7\t\u00d7\n\t\f")
        buf.write("\t\16\t\u00da\13\t\3\t\3\t\5\t\u00de\n\t\3\t\5\t\u00e1")
        buf.write("\n\t\3\t\3\t\5\t\u00e5\n\t\3\t\5\t\u00e8\n\t\3\t\3\t\3")
        buf.write("\n\3\n\7\n\u00ee\n\n\f\n\16\n\u00f1\13\n\3\13\3\13\7\13")
        buf.write("\u00f5\n\13\f\13\16\13\u00f8\13\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\5\f\u0100\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\7\"\u017f\n\"\f\"\16\"\u0182\13\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01ed\n#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\6A\u0231\nA\rA\16A\u0232\3A\3A\3B")
        buf.write("\3B\3C\3C\3D\3D\3\u009d\2E\3\3\5\4\7\5\t\6\13\2\r\7\17")
        buf.write("\2\21\b\23\2\25\t\27\2\31\n\33\13\35\f\37\r!\16#\17%\20")
        buf.write("\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33")
        buf.write("=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60")
        buf.write("g\61i\62k\63m\64o\65q\66s\67u8w9y:{;}<\177=\u0081>\u0083")
        buf.write("?\u0085@\u0087A\3\2\20\4\2\f\f\17\17\3\2\62\62\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\3\2//\3\2$$\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2}}\3\2\177\177\3\2..\3\2??\5\2\13\f\17\17\"\"\2")
        buf.write("\u0258\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\21\3\2\2\2\2\25\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\3\u0089\3\2\2\2\5\u008c\3\2\2\2\7\u0097\3\2\2\2\t\u00a5")
        buf.write("\3\2\2\2\13\u00b9\3\2\2\2\r\u00cf\3\2\2\2\17\u00d1\3\2")
        buf.write("\2\2\21\u00d3\3\2\2\2\23\u00eb\3\2\2\2\25\u00f2\3\2\2")
        buf.write("\2\27\u00ff\3\2\2\2\31\u0101\3\2\2\2\33\u0106\3\2\2\2")
        buf.write("\35\u010c\3\2\2\2\37\u0114\3\2\2\2!\u0117\3\2\2\2#\u011c")
        buf.write("\3\2\2\2%\u0122\3\2\2\2\'\u0128\3\2\2\2)\u012c\3\2\2\2")
        buf.write("+\u0135\3\2\2\2-\u0138\3\2\2\2/\u0140\3\2\2\2\61\u0147")
        buf.write("\3\2\2\2\63\u014e\3\2\2\2\65\u0153\3\2\2\2\67\u0159\3")
        buf.write("\2\2\29\u015e\3\2\2\2;\u0162\3\2\2\2=\u016b\3\2\2\2?\u016e")
        buf.write("\3\2\2\2A\u0176\3\2\2\2C\u017c\3\2\2\2E\u01ec\3\2\2\2")
        buf.write("G\u01ee\3\2\2\2I\u01f0\3\2\2\2K\u01f2\3\2\2\2M\u01f4\3")
        buf.write("\2\2\2O\u01f6\3\2\2\2Q\u01f8\3\2\2\2S\u01fa\3\2\2\2U\u01fd")
        buf.write("\3\2\2\2W\u0200\3\2\2\2Y\u0203\3\2\2\2[\u0206\3\2\2\2")
        buf.write("]\u0208\3\2\2\2_\u020b\3\2\2\2a\u020d\3\2\2\2c\u0210\3")
        buf.write("\2\2\2e\u0213\3\2\2\2g\u0215\3\2\2\2i\u0217\3\2\2\2k\u0219")
        buf.write("\3\2\2\2m\u021b\3\2\2\2o\u021d\3\2\2\2q\u021f\3\2\2\2")
        buf.write("s\u0221\3\2\2\2u\u0223\3\2\2\2w\u0225\3\2\2\2y\u0227\3")
        buf.write("\2\2\2{\u0229\3\2\2\2}\u022b\3\2\2\2\177\u022d\3\2\2\2")
        buf.write("\u0081\u0230\3\2\2\2\u0083\u0236\3\2\2\2\u0085\u0238\3")
        buf.write("\2\2\2\u0087\u023a\3\2\2\2\u0089\u008a\7}\2\2\u008a\u008b")
        buf.write("\7\177\2\2\u008b\4\3\2\2\2\u008c\u008d\7\61\2\2\u008d")
        buf.write("\u008e\7\61\2\2\u008e\u0092\3\2\2\2\u008f\u0091\n\2\2")
        buf.write("\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0095\u0096\b\3\2\2\u0096\6\3\2\2\2\u0097")
        buf.write("\u0098\7\61\2\2\u0098\u0099\7,\2\2\u0099\u009d\3\2\2\2")
        buf.write("\u009a\u009c\13\2\2\2\u009b\u009a\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7,\2\2")
        buf.write("\u00a1\u00a2\7\61\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4")
        buf.write("\b\4\2\2\u00a4\b\3\2\2\2\u00a5\u00ae\7}\2\2\u00a6\u00ab")
        buf.write("\5\13\6\2\u00a7\u00a8\7.\2\2\u00a8\u00aa\5\13\6\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ae\u00a6\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b1\7\177\2\2\u00b1\n\3\2\2\2\u00b2\u00ba")
        buf.write("\5\r\7\2\u00b3\u00ba\5\21\t\2\u00b4\u00ba\5\63\32\2\u00b5")
        buf.write("\u00ba\5#\22\2\u00b6\u00ba\5\25\13\2\u00b7\u00ba\5C\"")
        buf.write("\2\u00b8\u00ba\5\t\5\2\u00b9\u00b2\3\2\2\2\u00b9\u00b3")
        buf.write("\3\2\2\2\u00b9\u00b4\3\2\2\2\u00b9\u00b5\3\2\2\2\u00b9")
        buf.write("\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\f\3\2\2\2\u00bb\u00d0\t\3\2\2\u00bc\u00c0\t\4\2")
        buf.write("\2\u00bd\u00bf\5\17\b\2\u00be\u00bd\3\2\2\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00cb\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c5\7a\2\2")
        buf.write("\u00c4\u00c6\5\17\b\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00ca\3\2\2\2\u00c9\u00c3\3\2\2\2\u00ca\u00cd\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d0\b\7\3\2\u00cf\u00bb")
        buf.write("\3\2\2\2\u00cf\u00bc\3\2\2\2\u00d0\16\3\2\2\2\u00d1\u00d2")
        buf.write("\t\5\2\2\u00d2\20\3\2\2\2\u00d3\u00e7\5\r\7\2\u00d4\u00d8")
        buf.write("\5q9\2\u00d5\u00d7\t\5\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00da")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00e0\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\t\6\2\2")
        buf.write("\u00dc\u00de\t\7\2\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3")
        buf.write("\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\5\23\n\2\u00e0")
        buf.write("\u00db\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e8\3\2\2\2")
        buf.write("\u00e2\u00e4\t\6\2\2\u00e3\u00e5\t\7\2\2\u00e4\u00e3\3")
        buf.write("\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8")
        buf.write("\5\23\n\2\u00e7\u00d4\3\2\2\2\u00e7\u00e2\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ea\b\t\4\2\u00ea\22\3\2\2\2\u00eb")
        buf.write("\u00ef\t\4\2\2\u00ec\u00ee\5\17\b\2\u00ed\u00ec\3\2\2")
        buf.write("\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\24\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f6")
        buf.write("\5}?\2\u00f3\u00f5\5\27\f\2\u00f4\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f9\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\5")
        buf.write("}?\2\u00fa\u00fb\b\13\5\2\u00fb\26\3\2\2\2\u00fc\u0100")
        buf.write("\n\b\2\2\u00fd\u00fe\7^\2\2\u00fe\u0100\7$\2\2\u00ff\u00fc")
        buf.write("\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\30\3\2\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7w\2\2\u0103\u0104\7v\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\32\3\2\2\2\u0106\u0107\7d\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7g\2\2\u0109\u010a\7c\2\2\u010a\u010b")
        buf.write("\7m\2\2\u010b\34\3\2\2\2\u010c\u010d\7d\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7q\2\2\u010f\u0110\7n\2\2\u0110\u0111")
        buf.write("\7g\2\2\u0111\u0112\7c\2\2\u0112\u0113\7p\2\2\u0113\36")
        buf.write("\3\2\2\2\u0114\u0115\7f\2\2\u0115\u0116\7q\2\2\u0116 ")
        buf.write("\3\2\2\2\u0117\u0118\7g\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7u\2\2\u011a\u011b\7g\2\2\u011b\"\3\2\2\2\u011c\u011d")
        buf.write("\7h\2\2\u011d\u011e\7c\2\2\u011e\u011f\7n\2\2\u011f\u0120")
        buf.write("\7u\2\2\u0120\u0121\7g\2\2\u0121$\3\2\2\2\u0122\u0123")
        buf.write("\7h\2\2\u0123\u0124\7n\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7c\2\2\u0126\u0127\7v\2\2\u0127&\3\2\2\2\u0128\u0129")
        buf.write("\7h\2\2\u0129\u012a\7q\2\2\u012a\u012b\7t\2\2\u012b(\3")
        buf.write("\2\2\2\u012c\u012d\7h\2\2\u012d\u012e\7w\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f\u0130\7e\2\2\u0130\u0131\7v\2\2\u0131\u0132")
        buf.write("\7k\2\2\u0132\u0133\7q\2\2\u0133\u0134\7p\2\2\u0134*\3")
        buf.write("\2\2\2\u0135\u0136\7k\2\2\u0136\u0137\7h\2\2\u0137,\3")
        buf.write("\2\2\2\u0138\u0139\7k\2\2\u0139\u013a\7p\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b\u013c\7g\2\2\u013c\u013d\7i\2\2\u013d\u013e")
        buf.write("\7g\2\2\u013e\u013f\7t\2\2\u013f.\3\2\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u0145\7t\2\2\u0145\u0146\7p\2\2\u0146\60")
        buf.write("\3\2\2\2\u0147\u0148\7u\2\2\u0148\u0149\7v\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7k\2\2\u014b\u014c\7p\2\2\u014c\u014d")
        buf.write("\7i\2\2\u014d\62\3\2\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7t\2\2\u0150\u0151\7w\2\2\u0151\u0152\7g\2\2\u0152\64")
        buf.write("\3\2\2\2\u0153\u0154\7y\2\2\u0154\u0155\7j\2\2\u0155\u0156")
        buf.write("\7k\2\2\u0156\u0157\7n\2\2\u0157\u0158\7g\2\2\u0158\66")
        buf.write("\3\2\2\2\u0159\u015a\7x\2\2\u015a\u015b\7q\2\2\u015b\u015c")
        buf.write("\7k\2\2\u015c\u015d\7f\2\2\u015d8\3\2\2\2\u015e\u015f")
        buf.write("\7q\2\2\u015f\u0160\7w\2\2\u0160\u0161\7v\2\2\u0161:\3")
        buf.write("\2\2\2\u0162\u0163\7e\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write("\7p\2\2\u0165\u0166\7v\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168\u0169\7w\2\2\u0169\u016a\7g\2\2\u016a<\3")
        buf.write("\2\2\2\u016b\u016c\7q\2\2\u016c\u016d\7h\2\2\u016d>\3")
        buf.write("\2\2\2\u016e\u016f\7k\2\2\u016f\u0170\7p\2\2\u0170\u0171")
        buf.write("\7j\2\2\u0171\u0172\7g\2\2\u0172\u0173\7t\2\2\u0173\u0174")
        buf.write("\7k\2\2\u0174\u0175\7v\2\2\u0175@\3\2\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7t\2\2\u0178\u0179\7t\2\2\u0179\u017a")
        buf.write("\7c\2\2\u017a\u017b\7{\2\2\u017bB\3\2\2\2\u017c\u0180")
        buf.write("\t\t\2\2\u017d\u017f\t\n\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181D\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\7t\2\2")
        buf.write("\u0184\u0185\7g\2\2\u0185\u0186\7c\2\2\u0186\u0187\7f")
        buf.write("\2\2\u0187\u0188\7K\2\2\u0188\u0189\7p\2\2\u0189\u018a")
        buf.write("\7v\2\2\u018a\u018b\7g\2\2\u018b\u018c\7i\2\2\u018c\u018d")
        buf.write("\7g\2\2\u018d\u01ed\7t\2\2\u018e\u018f\7r\2\2\u018f\u0190")
        buf.write("\7t\2\2\u0190\u0191\7k\2\2\u0191\u0192\7p\2\2\u0192\u0193")
        buf.write("\7v\2\2\u0193\u0194\7K\2\2\u0194\u0195\7p\2\2\u0195\u0196")
        buf.write("\7v\2\2\u0196\u0197\7g\2\2\u0197\u0198\7i\2\2\u0198\u0199")
        buf.write("\7g\2\2\u0199\u01ed\7t\2\2\u019a\u019b\7t\2\2\u019b\u019c")
        buf.write("\7g\2\2\u019c\u019d\7c\2\2\u019d\u019e\7f\2\2\u019e\u019f")
        buf.write("\7H\2\2\u019f\u01a0\7n\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2")
        buf.write("\7c\2\2\u01a2\u01ed\7v\2\2\u01a3\u01a4\7y\2\2\u01a4\u01a5")
        buf.write("\7t\2\2\u01a5\u01a6\7k\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8\u01a9\7H\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab")
        buf.write("\7q\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ed\7v\2\2\u01ad\u01ae")
        buf.write("\7t\2\2\u01ae\u01af\7g\2\2\u01af\u01b0\7c\2\2\u01b0\u01b1")
        buf.write("\7f\2\2\u01b1\u01b2\7D\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4")
        buf.write("\7q\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7")
        buf.write("\7c\2\2\u01b7\u01ed\7p\2\2\u01b8\u01b9\7r\2\2\u01b9\u01ba")
        buf.write("\7t\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc\7p\2\2\u01bc\u01bd")
        buf.write("\7v\2\2\u01bd\u01be\7D\2\2\u01be\u01bf\7q\2\2\u01bf\u01c0")
        buf.write("\7q\2\2\u01c0\u01c1\7n\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3")
        buf.write("\7c\2\2\u01c3\u01ed\7p\2\2\u01c4\u01c5\7t\2\2\u01c5\u01c6")
        buf.write("\7g\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8\7f\2\2\u01c8\u01c9")
        buf.write("\7U\2\2\u01c9\u01ca\7v\2\2\u01ca\u01cb\7t\2\2\u01cb\u01cc")
        buf.write("\7k\2\2\u01cc\u01cd\7p\2\2\u01cd\u01ed\7i\2\2\u01ce\u01cf")
        buf.write("\7r\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7k\2\2\u01d1\u01d2")
        buf.write("\7p\2\2\u01d2\u01d3\7v\2\2\u01d3\u01d4\7U\2\2\u01d4\u01d5")
        buf.write("\7v\2\2\u01d5\u01d6\7t\2\2\u01d6\u01d7\7k\2\2\u01d7\u01d8")
        buf.write("\7p\2\2\u01d8\u01ed\7i\2\2\u01d9\u01da\7r\2\2\u01da\u01db")
        buf.write("\7t\2\2\u01db\u01dc\7g\2\2\u01dc\u01dd\7x\2\2\u01dd\u01de")
        buf.write("\7g\2\2\u01de\u01df\7p\2\2\u01df\u01e0\7v\2\2\u01e0\u01e1")
        buf.write("\7F\2\2\u01e1\u01e2\7g\2\2\u01e2\u01e3\7h\2\2\u01e3\u01e4")
        buf.write("\7c\2\2\u01e4\u01e5\7w\2\2\u01e5\u01e6\7n\2\2\u01e6\u01ed")
        buf.write("\7v\2\2\u01e7\u01e8\7u\2\2\u01e8\u01e9\7w\2\2\u01e9\u01ea")
        buf.write("\7r\2\2\u01ea\u01eb\7g\2\2\u01eb\u01ed\7t\2\2\u01ec\u0183")
        buf.write("\3\2\2\2\u01ec\u018e\3\2\2\2\u01ec\u019a\3\2\2\2\u01ec")
        buf.write("\u01a3\3\2\2\2\u01ec\u01ad\3\2\2\2\u01ec\u01b8\3\2\2\2")
        buf.write("\u01ec\u01c4\3\2\2\2\u01ec\u01ce\3\2\2\2\u01ec\u01d9\3")
        buf.write("\2\2\2\u01ec\u01e7\3\2\2\2\u01edF\3\2\2\2\u01ee\u01ef")
        buf.write("\7-\2\2\u01efH\3\2\2\2\u01f0\u01f1\7/\2\2\u01f1J\3\2\2")
        buf.write("\2\u01f2\u01f3\7,\2\2\u01f3L\3\2\2\2\u01f4\u01f5\7\61")
        buf.write("\2\2\u01f5N\3\2\2\2\u01f6\u01f7\7\'\2\2\u01f7P\3\2\2\2")
        buf.write("\u01f8\u01f9\7#\2\2\u01f9R\3\2\2\2\u01fa\u01fb\7(\2\2")
        buf.write("\u01fb\u01fc\7(\2\2\u01fcT\3\2\2\2\u01fd\u01fe\7~\2\2")
        buf.write("\u01fe\u01ff\7~\2\2\u01ffV\3\2\2\2\u0200\u0201\7?\2\2")
        buf.write("\u0201\u0202\7?\2\2\u0202X\3\2\2\2\u0203\u0204\7#\2\2")
        buf.write("\u0204\u0205\7?\2\2\u0205Z\3\2\2\2\u0206\u0207\7>\2\2")
        buf.write("\u0207\\\3\2\2\2\u0208\u0209\7>\2\2\u0209\u020a\7?\2\2")
        buf.write("\u020a^\3\2\2\2\u020b\u020c\7@\2\2\u020c`\3\2\2\2\u020d")
        buf.write("\u020e\7@\2\2\u020e\u020f\7?\2\2\u020fb\3\2\2\2\u0210")
        buf.write("\u0211\7<\2\2\u0211\u0212\7<\2\2\u0212d\3\2\2\2\u0213")
        buf.write("\u0214\7*\2\2\u0214f\3\2\2\2\u0215\u0216\7+\2\2\u0216")
        buf.write("h\3\2\2\2\u0217\u0218\t\13\2\2\u0218j\3\2\2\2\u0219\u021a")
        buf.write("\t\f\2\2\u021al\3\2\2\2\u021b\u021c\7]\2\2\u021cn\3\2")
        buf.write("\2\2\u021d\u021e\7_\2\2\u021ep\3\2\2\2\u021f\u0220\7\60")
        buf.write("\2\2\u0220r\3\2\2\2\u0221\u0222\t\r\2\2\u0222t\3\2\2\2")
        buf.write("\u0223\u0224\7=\2\2\u0224v\3\2\2\2\u0225\u0226\7<\2\2")
        buf.write("\u0226x\3\2\2\2\u0227\u0228\t\16\2\2\u0228z\3\2\2\2\u0229")
        buf.write("\u022a\7)\2\2\u022a|\3\2\2\2\u022b\u022c\7$\2\2\u022c")
        buf.write("~\3\2\2\2\u022d\u022e\7^\2\2\u022e\u0080\3\2\2\2\u022f")
        buf.write("\u0231\t\17\2\2\u0230\u022f\3\2\2\2\u0231\u0232\3\2\2")
        buf.write("\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234")
        buf.write("\3\2\2\2\u0234\u0235\bA\2\2\u0235\u0082\3\2\2\2\u0236")
        buf.write("\u0237\13\2\2\2\u0237\u0084\3\2\2\2\u0238\u0239\13\2\2")
        buf.write("\2\u0239\u0086\3\2\2\2\u023a\u023b\13\2\2\2\u023b\u0088")
        buf.write("\3\2\2\2\27\2\u0092\u009d\u00ab\u00ae\u00b9\u00c0\u00c7")
        buf.write("\u00cb\u00cf\u00d8\u00dd\u00e0\u00e4\u00e7\u00ef\u00f6")
        buf.write("\u00ff\u0180\u01ec\u0232\6\b\2\2\3\7\2\3\t\3\3\13\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMEMTLINE = 2
    COMMENTBOX = 3
    ARR = 4
    INT = 5
    FL = 6
    STR = 7
    AUTO = 8
    BREAK = 9
    BOOLEAN = 10
    DO = 11
    ELSE = 12
    FALSE = 13
    FLOAT = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    INTEGER = 18
    RETURN = 19
    STRING = 20
    TRUE = 21
    WHILE = 22
    VOID = 23
    OUT = 24
    CONTINUE = 25
    OF = 26
    INHERIT = 27
    ARRAY = 28
    ID = 29
    SPECIAL_FUNC = 30
    ADD = 31
    MINUS = 32
    MUL = 33
    DIV = 34
    PER = 35
    NOT = 36
    AND = 37
    OR = 38
    EQUAL = 39
    DIF = 40
    SMALLER = 41
    SMALLER_OR_EQUAL = 42
    BIGGER = 43
    BIGGER_OR_EQUAL = 44
    DOUBLECOLON = 45
    LB = 46
    RB = 47
    LCB = 48
    RCB = 49
    LSB = 50
    RSB = 51
    DOT = 52
    COMMA = 53
    SEMI = 54
    COLON = 55
    EQ = 56
    SQ = 57
    DQ = 58
    BS = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{}'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'return'", "'string'", "'true'", "'while'", "'void'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", 
            "'.'", "';'", "':'", "'''", "'\"'", "'\\'" ]

    symbolicNames = [ "<INVALID>",
            "COMMEMTLINE", "COMMENTBOX", "ARR", "INT", "FL", "STR", "AUTO", 
            "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ID", "SPECIAL_FUNC", 
            "ADD", "MINUS", "MUL", "DIV", "PER", "NOT", "AND", "OR", "EQUAL", 
            "DIF", "SMALLER", "SMALLER_OR_EQUAL", "BIGGER", "BIGGER_OR_EQUAL", 
            "DOUBLECOLON", "LB", "RB", "LCB", "RCB", "LSB", "RSB", "DOT", 
            "COMMA", "SEMI", "COLON", "EQ", "SQ", "DQ", "BS", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "COMMEMTLINE", "COMMENTBOX", "ARR", "VAL", "INT", 
                  "NUM", "FL", "DIGIT", "STR", "INSTR", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ID", 
                  "SPECIAL_FUNC", "ADD", "MINUS", "MUL", "DIV", "PER", "NOT", 
                  "AND", "OR", "EQUAL", "DIF", "SMALLER", "SMALLER_OR_EQUAL", 
                  "BIGGER", "BIGGER_OR_EQUAL", "DOUBLECOLON", "LB", "RB", 
                  "LCB", "RCB", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", 
                  "EQ", "SQ", "DQ", "BS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.INT_action 
            actions[7] = self.FL_action 
            actions[9] = self.STR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     


