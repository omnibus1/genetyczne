# Generated from MyGrammer.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2&\n\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3,\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\2\3\3\2\t\n\2:\2%\3\2\2\2\4+\3\2")
        buf.write("\2\2\6-\3\2\2\2\b/\3\2\2\2\n\61\3\2\2\2\f\63\3\2\2\2\16")
        buf.write("\65\3\2\2\2\20\67\3\2\2\2\229\3\2\2\2\24;\3\2\2\2\26=")
        buf.write("\3\2\2\2\30\31\5\6\4\2\31\32\5\2\2\2\32\33\5\4\3\2\33")
        buf.write("\34\5\2\2\2\34\35\5\b\5\2\35&\3\2\2\2\36\37\5\26\f\2\37")
        buf.write(" \5\6\4\2 !\5\2\2\2!\"\5\b\5\2\"&\3\2\2\2#&\5\22\n\2$")
        buf.write("&\5\24\13\2%\30\3\2\2\2%\36\3\2\2\2%#\3\2\2\2%$\3\2\2")
        buf.write("\2&\3\3\2\2\2\',\5\n\6\2(,\5\f\7\2),\5\16\b\2*,\5\20\t")
        buf.write("\2+\'\3\2\2\2+(\3\2\2\2+)\3\2\2\2+*\3\2\2\2,\5\3\2\2\2")
        buf.write("-.\7\3\2\2.\7\3\2\2\2/\60\7\4\2\2\60\t\3\2\2\2\61\62\7")
        buf.write("\5\2\2\62\13\3\2\2\2\63\64\7\6\2\2\64\r\3\2\2\2\65\66")
        buf.write("\7\7\2\2\66\17\3\2\2\2\678\7\b\2\28\21\3\2\2\29:\7\13")
        buf.write("\2\2:\23\3\2\2\2;<\7\f\2\2<\25\3\2\2\2=>\t\2\2\2>\27\3")
        buf.write("\2\2\2\4%+")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "' * '", "' / '", "' + '", 
                     "' - '", "'sin'", "'cos'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FLOAT", "VARIABLE" ]

    RULE_expr = 0
    RULE_binary_operator = 1
    RULE_left_quote = 2
    RULE_right_quote = 3
    RULE_mul = 4
    RULE_div = 5
    RULE_add = 6
    RULE_sub = 7
    RULE_floatVal = 8
    RULE_variable = 9
    RULE_unary_operator = 10

    ruleNames =  [ "expr", "binary_operator", "left_quote", "right_quote", 
                   "mul", "div", "add", "sub", "floatVal", "variable", "unary_operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    FLOAT=9
    VARIABLE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_quote(self):
            return self.getTypedRuleContext(MyGrammerParser.Left_quoteContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.ExprContext,i)


        def binary_operator(self):
            return self.getTypedRuleContext(MyGrammerParser.Binary_operatorContext,0)


        def right_quote(self):
            return self.getTypedRuleContext(MyGrammerParser.Right_quoteContext,0)


        def unary_operator(self):
            return self.getTypedRuleContext(MyGrammerParser.Unary_operatorContext,0)


        def floatVal(self):
            return self.getTypedRuleContext(MyGrammerParser.FloatValContext,0)


        def variable(self):
            return self.getTypedRuleContext(MyGrammerParser.VariableContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MyGrammerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.left_quote()
                self.state = 23
                self.expr()
                self.state = 24
                self.binary_operator()
                self.state = 25
                self.expr()
                self.state = 26
                self.right_quote()
                pass
            elif token in [MyGrammerParser.T__6, MyGrammerParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.unary_operator()
                self.state = 29
                self.left_quote()
                self.state = 30
                self.expr()
                self.state = 31
                self.right_quote()
                pass
            elif token in [MyGrammerParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.floatVal()
                pass
            elif token in [MyGrammerParser.VARIABLE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.variable()
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

    class Binary_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul(self):
            return self.getTypedRuleContext(MyGrammerParser.MulContext,0)


        def div(self):
            return self.getTypedRuleContext(MyGrammerParser.DivContext,0)


        def add(self):
            return self.getTypedRuleContext(MyGrammerParser.AddContext,0)


        def sub(self):
            return self.getTypedRuleContext(MyGrammerParser.SubContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_binary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_operator" ):
                listener.enterBinary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_operator" ):
                listener.exitBinary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_operator" ):
                return visitor.visitBinary_operator(self)
            else:
                return visitor.visitChildren(self)




    def binary_operator(self):

        localctx = MyGrammerParser.Binary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_binary_operator)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.mul()
                pass
            elif token in [MyGrammerParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.div()
                pass
            elif token in [MyGrammerParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.add()
                pass
            elif token in [MyGrammerParser.T__5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.sub()
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

    class Left_quoteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_left_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_quote" ):
                listener.enterLeft_quote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_quote" ):
                listener.exitLeft_quote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_quote" ):
                return visitor.visitLeft_quote(self)
            else:
                return visitor.visitChildren(self)




    def left_quote(self):

        localctx = MyGrammerParser.Left_quoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_left_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MyGrammerParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Right_quoteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_right_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_quote" ):
                listener.enterRight_quote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_quote" ):
                listener.exitRight_quote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRight_quote" ):
                return visitor.visitRight_quote(self)
            else:
                return visitor.visitChildren(self)




    def right_quote(self):

        localctx = MyGrammerParser.Right_quoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_right_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MyGrammerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)




    def mul(self):

        localctx = MyGrammerParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MyGrammerParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)




    def div(self):

        localctx = MyGrammerParser.DivContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_div)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MyGrammerParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = MyGrammerParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MyGrammerParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)




    def sub(self):

        localctx = MyGrammerParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MyGrammerParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(MyGrammerParser.FLOAT, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_floatVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatVal" ):
                listener.enterFloatVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatVal" ):
                listener.exitFloatVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatVal" ):
                return visitor.visitFloatVal(self)
            else:
                return visitor.visitChildren(self)




    def floatVal(self):

        localctx = MyGrammerParser.FloatValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_floatVal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MyGrammerParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MyGrammerParser.VARIABLE, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = MyGrammerParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MyGrammerParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_unary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_operator" ):
                listener.enterUnary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_operator" ):
                listener.exitUnary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_operator" ):
                return visitor.visitUnary_operator(self)
            else:
                return visitor.visitChildren(self)




    def unary_operator(self):

        localctx = MyGrammerParser.Unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==MyGrammerParser.T__6 or _la==MyGrammerParser.T__7):
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





