# Generated from MyGrammer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\5\n\65\n\n")
        buf.write("\3\n\6\n8\n\n\r\n\16\n9\3\n\3\n\6\n>\n\n\r\n\16\n?\3\n")
        buf.write("\5\nC\n\n\3\n\3\n\6\nG\n\n\r\n\16\nH\5\nK\n\n\3\13\3\13")
        buf.write("\3\13\3\13\5\13Q\n\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\3\2\4\3\2//\3\2\62;\2X\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33\3\2\2\2\t\37\3\2")
        buf.write("\2\2\13#\3\2\2\2\r\'\3\2\2\2\17+\3\2\2\2\21/\3\2\2\2\23")
        buf.write("J\3\2\2\2\25P\3\2\2\2\27\30\7*\2\2\30\4\3\2\2\2\31\32")
        buf.write("\7+\2\2\32\6\3\2\2\2\33\34\7\"\2\2\34\35\7,\2\2\35\36")
        buf.write("\7\"\2\2\36\b\3\2\2\2\37 \7\"\2\2 !\7\61\2\2!\"\7\"\2")
        buf.write("\2\"\n\3\2\2\2#$\7\"\2\2$%\7-\2\2%&\7\"\2\2&\f\3\2\2\2")
        buf.write("\'(\7\"\2\2()\7/\2\2)*\7\"\2\2*\16\3\2\2\2+,\7u\2\2,-")
        buf.write("\7k\2\2-.\7p\2\2.\20\3\2\2\2/\60\7e\2\2\60\61\7q\2\2\61")
        buf.write("\62\7u\2\2\62\22\3\2\2\2\63\65\t\2\2\2\64\63\3\2\2\2\64")
        buf.write("\65\3\2\2\2\65\67\3\2\2\2\668\t\3\2\2\67\66\3\2\2\289")
        buf.write("\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;=\7\60\2\2<>")
        buf.write("\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@K\3\2")
        buf.write("\2\2AC\t\2\2\2BA\3\2\2\2BC\3\2\2\2CD\3\2\2\2DF\7\60\2")
        buf.write("\2EG\t\3\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I")
        buf.write("K\3\2\2\2J\64\3\2\2\2JB\3\2\2\2K\24\3\2\2\2LM\7Z\2\2M")
        buf.write("Q\7\63\2\2NO\7Z\2\2OQ\7\64\2\2PL\3\2\2\2PN\3\2\2\2Q\26")
        buf.write("\3\2\2\2\n\2\649?BHJP\2")
        return buf.getvalue()


class MyGrammerLexer(Lexer):

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
    FLOAT = 9
    VARIABLE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "' * '", "' / '", "' + '", "' - '", "'sin'", "'cos'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "VARIABLE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "FLOAT", "VARIABLE" ]

    grammarFileName = "MyGrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


