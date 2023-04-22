# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\u023b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b9\n\6\3\7\3\7\3\7")
        buf.write("\7\7\u00be\n\7\f\7\16\7\u00c1\13\7\3\7\3\7\6\7\u00c5\n")
        buf.write("\7\r\7\16\7\u00c6\7\7\u00c9\n\7\f\7\16\7\u00cc\13\7\3")
        buf.write("\7\5\7\u00cf\n\7\3\b\3\b\3\t\3\t\3\t\7\t\u00d6\n\t\f\t")
        buf.write("\16\t\u00d9\13\t\3\t\3\t\5\t\u00dd\n\t\3\t\5\t\u00e0\n")
        buf.write("\t\3\t\3\t\5\t\u00e4\n\t\3\t\5\t\u00e7\n\t\3\t\3\t\3\n")
        buf.write("\3\n\7\n\u00ed\n\n\f\n\16\n\u00f0\13\n\3\13\3\13\7\13")
        buf.write("\u00f4\n\13\f\13\16\13\u00f7\13\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\5\f\u00ff\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
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
        buf.write("!\3!\3\"\3\"\7\"\u017e\n\"\f\"\16\"\u0181\13\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01ec\n#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\6A\u0230\nA\rA\16A\u0231\3A\3A\3B")
        buf.write("\3B\3C\3C\3D\3D\3\u009d\2E\3\3\5\4\7\5\t\6\13\2\r\7\17")
        buf.write("\2\21\b\23\2\25\t\27\2\31\n\33\13\35\f\37\r!\16#\17%\20")
        buf.write("\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33")
        buf.write("=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60")
        buf.write("g\61i\62k\63m\64o\65q\66s\67u8w9y:{;}<\177=\u0081>\u0083")
        buf.write("?\u0085@\u0087A\3\2\20\4\2\f\f\17\17\3\2\62\62\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\3\2//\3\2$$\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2}}\3\2\177\177\3\2..\3\2??\5\2\13\f\17\17\"\"\2")
        buf.write("\u0256\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
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
        buf.write("\3\2\2\2\13\u00b8\3\2\2\2\r\u00ce\3\2\2\2\17\u00d0\3\2")
        buf.write("\2\2\21\u00d2\3\2\2\2\23\u00ea\3\2\2\2\25\u00f1\3\2\2")
        buf.write("\2\27\u00fe\3\2\2\2\31\u0100\3\2\2\2\33\u0105\3\2\2\2")
        buf.write("\35\u010b\3\2\2\2\37\u0113\3\2\2\2!\u0116\3\2\2\2#\u011b")
        buf.write("\3\2\2\2%\u0121\3\2\2\2\'\u0127\3\2\2\2)\u012b\3\2\2\2")
        buf.write("+\u0134\3\2\2\2-\u0137\3\2\2\2/\u013f\3\2\2\2\61\u0146")
        buf.write("\3\2\2\2\63\u014d\3\2\2\2\65\u0152\3\2\2\2\67\u0158\3")
        buf.write("\2\2\29\u015d\3\2\2\2;\u0161\3\2\2\2=\u016a\3\2\2\2?\u016d")
        buf.write("\3\2\2\2A\u0175\3\2\2\2C\u017b\3\2\2\2E\u01eb\3\2\2\2")
        buf.write("G\u01ed\3\2\2\2I\u01ef\3\2\2\2K\u01f1\3\2\2\2M\u01f3\3")
        buf.write("\2\2\2O\u01f5\3\2\2\2Q\u01f7\3\2\2\2S\u01f9\3\2\2\2U\u01fc")
        buf.write("\3\2\2\2W\u01ff\3\2\2\2Y\u0202\3\2\2\2[\u0205\3\2\2\2")
        buf.write("]\u0207\3\2\2\2_\u020a\3\2\2\2a\u020c\3\2\2\2c\u020f\3")
        buf.write("\2\2\2e\u0212\3\2\2\2g\u0214\3\2\2\2i\u0216\3\2\2\2k\u0218")
        buf.write("\3\2\2\2m\u021a\3\2\2\2o\u021c\3\2\2\2q\u021e\3\2\2\2")
        buf.write("s\u0220\3\2\2\2u\u0222\3\2\2\2w\u0224\3\2\2\2y\u0226\3")
        buf.write("\2\2\2{\u0228\3\2\2\2}\u022a\3\2\2\2\177\u022c\3\2\2\2")
        buf.write("\u0081\u022f\3\2\2\2\u0083\u0235\3\2\2\2\u0085\u0237\3")
        buf.write("\2\2\2\u0087\u0239\3\2\2\2\u0089\u008a\7}\2\2\u008a\u008b")
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
        buf.write("\3\2\2\2\u00b0\u00b1\7\177\2\2\u00b1\n\3\2\2\2\u00b2\u00b9")
        buf.write("\5\r\7\2\u00b3\u00b9\5\21\t\2\u00b4\u00b9\5\63\32\2\u00b5")
        buf.write("\u00b9\5#\22\2\u00b6\u00b9\5\25\13\2\u00b7\u00b9\5C\"")
        buf.write("\2\u00b8\u00b2\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8\u00b4")
        buf.write("\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\f\3\2\2\2\u00ba\u00cf\t\3\2\2\u00bb")
        buf.write("\u00bf\t\4\2\2\u00bc\u00be\5\17\b\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0")
        buf.write("\3\2\2\2\u00c0\u00ca\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2")
        buf.write("\u00c4\7a\2\2\u00c3\u00c5\5\17\b\2\u00c4\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c9\u00cc")
        buf.write("\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00cf\b\7\3\2")
        buf.write("\u00ce\u00ba\3\2\2\2\u00ce\u00bb\3\2\2\2\u00cf\16\3\2")
        buf.write("\2\2\u00d0\u00d1\t\5\2\2\u00d1\20\3\2\2\2\u00d2\u00e6")
        buf.write("\5\r\7\2\u00d3\u00d7\5q9\2\u00d4\u00d6\t\5\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00df\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00da\u00dc\t\6\2\2\u00db\u00dd\t\7\2\2\u00dc\u00db\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0")
        buf.write("\5\23\n\2\u00df\u00da\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e7\3\2\2\2\u00e1\u00e3\t\6\2\2\u00e2\u00e4\t\7\2\2")
        buf.write("\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3")
        buf.write("\2\2\2\u00e5\u00e7\5\23\n\2\u00e6\u00d3\3\2\2\2\u00e6")
        buf.write("\u00e1\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\b\t\4\2")
        buf.write("\u00e9\22\3\2\2\2\u00ea\u00ee\t\4\2\2\u00eb\u00ed\5\17")
        buf.write("\b\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\24\3\2\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f1\u00f5\5}?\2\u00f2\u00f4\5\27\f\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f8\u00f9\5}?\2\u00f9\u00fa\b\13\5\2\u00fa\26")
        buf.write("\3\2\2\2\u00fb\u00ff\n\b\2\2\u00fc\u00fd\7^\2\2\u00fd")
        buf.write("\u00ff\7$\2\2\u00fe\u00fb\3\2\2\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00ff\30\3\2\2\2\u0100\u0101\7c\2\2\u0101\u0102\7w\2")
        buf.write("\2\u0102\u0103\7v\2\2\u0103\u0104\7q\2\2\u0104\32\3\2")
        buf.write("\2\2\u0105\u0106\7d\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7c\2\2\u0109\u010a\7m\2\2\u010a\34")
        buf.write("\3\2\2\2\u010b\u010c\7d\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7n\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7c\2\2\u0111\u0112\7p\2\2\u0112\36\3\2\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114\u0115\7q\2\2\u0115 \3\2\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117\u0118\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\"\3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120$\3\2\2\2\u0121\u0122\7h\2\2\u0122\u0123")
        buf.write("\7n\2\2\u0123\u0124\7q\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7v\2\2\u0126&\3\2\2\2\u0127\u0128\7h\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7t\2\2\u012a(\3\2\2\2\u012b\u012c")
        buf.write("\7h\2\2\u012c\u012d\7w\2\2\u012d\u012e\7p\2\2\u012e\u012f")
        buf.write("\7e\2\2\u012f\u0130\7v\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7q\2\2\u0132\u0133\7p\2\2\u0133*\3\2\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7h\2\2\u0136,\3\2\2\2\u0137\u0138")
        buf.write("\7k\2\2\u0138\u0139\7p\2\2\u0139\u013a\7v\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013b\u013c\7i\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7t\2\2\u013e.\3\2\2\2\u013f\u0140\7t\2\2\u0140\u0141")
        buf.write("\7g\2\2\u0141\u0142\7v\2\2\u0142\u0143\7w\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144\u0145\7p\2\2\u0145\60\3\2\2\2\u0146\u0147")
        buf.write("\7u\2\2\u0147\u0148\7v\2\2\u0148\u0149\7t\2\2\u0149\u014a")
        buf.write("\7k\2\2\u014a\u014b\7p\2\2\u014b\u014c\7i\2\2\u014c\62")
        buf.write("\3\2\2\2\u014d\u014e\7v\2\2\u014e\u014f\7t\2\2\u014f\u0150")
        buf.write("\7w\2\2\u0150\u0151\7g\2\2\u0151\64\3\2\2\2\u0152\u0153")
        buf.write("\7y\2\2\u0153\u0154\7j\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7n\2\2\u0156\u0157\7g\2\2\u0157\66\3\2\2\2\u0158\u0159")
        buf.write("\7x\2\2\u0159\u015a\7q\2\2\u015a\u015b\7k\2\2\u015b\u015c")
        buf.write("\7f\2\2\u015c8\3\2\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7w\2\2\u015f\u0160\7v\2\2\u0160:\3\2\2\2\u0161\u0162")
        buf.write("\7e\2\2\u0162\u0163\7q\2\2\u0163\u0164\7p\2\2\u0164\u0165")
        buf.write("\7v\2\2\u0165\u0166\7k\2\2\u0166\u0167\7p\2\2\u0167\u0168")
        buf.write("\7w\2\2\u0168\u0169\7g\2\2\u0169<\3\2\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7h\2\2\u016c>\3\2\2\2\u016d\u016e")
        buf.write("\7k\2\2\u016e\u016f\7p\2\2\u016f\u0170\7j\2\2\u0170\u0171")
        buf.write("\7g\2\2\u0171\u0172\7t\2\2\u0172\u0173\7k\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174@\3\2\2\2\u0175\u0176\7c\2\2\u0176\u0177")
        buf.write("\7t\2\2\u0177\u0178\7t\2\2\u0178\u0179\7c\2\2\u0179\u017a")
        buf.write("\7{\2\2\u017aB\3\2\2\2\u017b\u017f\t\t\2\2\u017c\u017e")
        buf.write("\t\n\2\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180D\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0183\7t\2\2\u0183\u0184\7g\2\2\u0184")
        buf.write("\u0185\7c\2\2\u0185\u0186\7f\2\2\u0186\u0187\7K\2\2\u0187")
        buf.write("\u0188\7p\2\2\u0188\u0189\7v\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write("\u018b\7i\2\2\u018b\u018c\7g\2\2\u018c\u01ec\7t\2\2\u018d")
        buf.write("\u018e\7r\2\2\u018e\u018f\7t\2\2\u018f\u0190\7k\2\2\u0190")
        buf.write("\u0191\7p\2\2\u0191\u0192\7v\2\2\u0192\u0193\7K\2\2\u0193")
        buf.write("\u0194\7p\2\2\u0194\u0195\7v\2\2\u0195\u0196\7g\2\2\u0196")
        buf.write("\u0197\7i\2\2\u0197\u0198\7g\2\2\u0198\u01ec\7t\2\2\u0199")
        buf.write("\u019a\7t\2\2\u019a\u019b\7g\2\2\u019b\u019c\7c\2\2\u019c")
        buf.write("\u019d\7f\2\2\u019d\u019e\7H\2\2\u019e\u019f\7n\2\2\u019f")
        buf.write("\u01a0\7q\2\2\u01a0\u01a1\7c\2\2\u01a1\u01ec\7v\2\2\u01a2")
        buf.write("\u01a3\7y\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5\7k\2\2\u01a5")
        buf.write("\u01a6\7v\2\2\u01a6\u01a7\7g\2\2\u01a7\u01a8\7H\2\2\u01a8")
        buf.write("\u01a9\7n\2\2\u01a9\u01aa\7q\2\2\u01aa\u01ab\7c\2\2\u01ab")
        buf.write("\u01ec\7v\2\2\u01ac\u01ad\7t\2\2\u01ad\u01ae\7g\2\2\u01ae")
        buf.write("\u01af\7c\2\2\u01af\u01b0\7f\2\2\u01b0\u01b1\7D\2\2\u01b1")
        buf.write("\u01b2\7q\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4\7n\2\2\u01b4")
        buf.write("\u01b5\7g\2\2\u01b5\u01b6\7c\2\2\u01b6\u01ec\7p\2\2\u01b7")
        buf.write("\u01b8\7r\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7k\2\2\u01ba")
        buf.write("\u01bb\7p\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd\7D\2\2\u01bd")
        buf.write("\u01be\7q\2\2\u01be\u01bf\7q\2\2\u01bf\u01c0\7n\2\2\u01c0")
        buf.write("\u01c1\7g\2\2\u01c1\u01c2\7c\2\2\u01c2\u01ec\7p\2\2\u01c3")
        buf.write("\u01c4\7t\2\2\u01c4\u01c5\7g\2\2\u01c5\u01c6\7c\2\2\u01c6")
        buf.write("\u01c7\7f\2\2\u01c7\u01c8\7U\2\2\u01c8\u01c9\7v\2\2\u01c9")
        buf.write("\u01ca\7t\2\2\u01ca\u01cb\7k\2\2\u01cb\u01cc\7p\2\2\u01cc")
        buf.write("\u01ec\7i\2\2\u01cd\u01ce\7r\2\2\u01ce\u01cf\7t\2\2\u01cf")
        buf.write("\u01d0\7k\2\2\u01d0\u01d1\7p\2\2\u01d1\u01d2\7v\2\2\u01d2")
        buf.write("\u01d3\7U\2\2\u01d3\u01d4\7v\2\2\u01d4\u01d5\7t\2\2\u01d5")
        buf.write("\u01d6\7k\2\2\u01d6\u01d7\7p\2\2\u01d7\u01ec\7i\2\2\u01d8")
        buf.write("\u01d9\7r\2\2\u01d9\u01da\7t\2\2\u01da\u01db\7g\2\2\u01db")
        buf.write("\u01dc\7x\2\2\u01dc\u01dd\7g\2\2\u01dd\u01de\7p\2\2\u01de")
        buf.write("\u01df\7v\2\2\u01df\u01e0\7F\2\2\u01e0\u01e1\7g\2\2\u01e1")
        buf.write("\u01e2\7h\2\2\u01e2\u01e3\7c\2\2\u01e3\u01e4\7w\2\2\u01e4")
        buf.write("\u01e5\7n\2\2\u01e5\u01ec\7v\2\2\u01e6\u01e7\7u\2\2\u01e7")
        buf.write("\u01e8\7w\2\2\u01e8\u01e9\7r\2\2\u01e9\u01ea\7g\2\2\u01ea")
        buf.write("\u01ec\7t\2\2\u01eb\u0182\3\2\2\2\u01eb\u018d\3\2\2\2")
        buf.write("\u01eb\u0199\3\2\2\2\u01eb\u01a2\3\2\2\2\u01eb\u01ac\3")
        buf.write("\2\2\2\u01eb\u01b7\3\2\2\2\u01eb\u01c3\3\2\2\2\u01eb\u01cd")
        buf.write("\3\2\2\2\u01eb\u01d8\3\2\2\2\u01eb\u01e6\3\2\2\2\u01ec")
        buf.write("F\3\2\2\2\u01ed\u01ee\7-\2\2\u01eeH\3\2\2\2\u01ef\u01f0")
        buf.write("\7/\2\2\u01f0J\3\2\2\2\u01f1\u01f2\7,\2\2\u01f2L\3\2\2")
        buf.write("\2\u01f3\u01f4\7\61\2\2\u01f4N\3\2\2\2\u01f5\u01f6\7\'")
        buf.write("\2\2\u01f6P\3\2\2\2\u01f7\u01f8\7#\2\2\u01f8R\3\2\2\2")
        buf.write("\u01f9\u01fa\7(\2\2\u01fa\u01fb\7(\2\2\u01fbT\3\2\2\2")
        buf.write("\u01fc\u01fd\7~\2\2\u01fd\u01fe\7~\2\2\u01feV\3\2\2\2")
        buf.write("\u01ff\u0200\7?\2\2\u0200\u0201\7?\2\2\u0201X\3\2\2\2")
        buf.write("\u0202\u0203\7#\2\2\u0203\u0204\7?\2\2\u0204Z\3\2\2\2")
        buf.write("\u0205\u0206\7>\2\2\u0206\\\3\2\2\2\u0207\u0208\7>\2\2")
        buf.write("\u0208\u0209\7?\2\2\u0209^\3\2\2\2\u020a\u020b\7@\2\2")
        buf.write("\u020b`\3\2\2\2\u020c\u020d\7@\2\2\u020d\u020e\7?\2\2")
        buf.write("\u020eb\3\2\2\2\u020f\u0210\7<\2\2\u0210\u0211\7<\2\2")
        buf.write("\u0211d\3\2\2\2\u0212\u0213\7*\2\2\u0213f\3\2\2\2\u0214")
        buf.write("\u0215\7+\2\2\u0215h\3\2\2\2\u0216\u0217\t\13\2\2\u0217")
        buf.write("j\3\2\2\2\u0218\u0219\t\f\2\2\u0219l\3\2\2\2\u021a\u021b")
        buf.write("\7]\2\2\u021bn\3\2\2\2\u021c\u021d\7_\2\2\u021dp\3\2\2")
        buf.write("\2\u021e\u021f\7\60\2\2\u021fr\3\2\2\2\u0220\u0221\t\r")
        buf.write("\2\2\u0221t\3\2\2\2\u0222\u0223\7=\2\2\u0223v\3\2\2\2")
        buf.write("\u0224\u0225\7<\2\2\u0225x\3\2\2\2\u0226\u0227\t\16\2")
        buf.write("\2\u0227z\3\2\2\2\u0228\u0229\7)\2\2\u0229|\3\2\2\2\u022a")
        buf.write("\u022b\7$\2\2\u022b~\3\2\2\2\u022c\u022d\7^\2\2\u022d")
        buf.write("\u0080\3\2\2\2\u022e\u0230\t\17\2\2\u022f\u022e\3\2\2")
        buf.write("\2\u0230\u0231\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232")
        buf.write("\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\bA\2\2\u0234")
        buf.write("\u0082\3\2\2\2\u0235\u0236\13\2\2\2\u0236\u0084\3\2\2")
        buf.write("\2\u0237\u0238\13\2\2\2\u0238\u0086\3\2\2\2\u0239\u023a")
        buf.write("\13\2\2\2\u023a\u0088\3\2\2\2\27\2\u0092\u009d\u00ab\u00ae")
        buf.write("\u00b8\u00bf\u00c6\u00ca\u00ce\u00d7\u00dc\u00df\u00e3")
        buf.write("\u00e6\u00ee\u00f5\u00fe\u017f\u01eb\u0231\6\b\2\2\3\7")
        buf.write("\2\3\t\3\3\13\4")
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
     


