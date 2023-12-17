# Generated from MyGrammer.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#expr.
    def enterExpr(self, ctx:MyGrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#expr.
    def exitExpr(self, ctx:MyGrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#binary_operator.
    def enterBinary_operator(self, ctx:MyGrammerParser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#binary_operator.
    def exitBinary_operator(self, ctx:MyGrammerParser.Binary_operatorContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#left_quote.
    def enterLeft_quote(self, ctx:MyGrammerParser.Left_quoteContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#left_quote.
    def exitLeft_quote(self, ctx:MyGrammerParser.Left_quoteContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#right_quote.
    def enterRight_quote(self, ctx:MyGrammerParser.Right_quoteContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#right_quote.
    def exitRight_quote(self, ctx:MyGrammerParser.Right_quoteContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#mul.
    def enterMul(self, ctx:MyGrammerParser.MulContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#mul.
    def exitMul(self, ctx:MyGrammerParser.MulContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#div.
    def enterDiv(self, ctx:MyGrammerParser.DivContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#div.
    def exitDiv(self, ctx:MyGrammerParser.DivContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#add.
    def enterAdd(self, ctx:MyGrammerParser.AddContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#add.
    def exitAdd(self, ctx:MyGrammerParser.AddContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#sub.
    def enterSub(self, ctx:MyGrammerParser.SubContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#sub.
    def exitSub(self, ctx:MyGrammerParser.SubContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#floatVal.
    def enterFloatVal(self, ctx:MyGrammerParser.FloatValContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#floatVal.
    def exitFloatVal(self, ctx:MyGrammerParser.FloatValContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#variable.
    def enterVariable(self, ctx:MyGrammerParser.VariableContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#variable.
    def exitVariable(self, ctx:MyGrammerParser.VariableContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#unary_operator.
    def enterUnary_operator(self, ctx:MyGrammerParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#unary_operator.
    def exitUnary_operator(self, ctx:MyGrammerParser.Unary_operatorContext):
        pass


