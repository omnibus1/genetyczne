# Generated from MyGrammer.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammerParser.

class MyGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammerParser#expr.
    def visitExpr(self, ctx:MyGrammerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#binary_operator.
    def visitBinary_operator(self, ctx:MyGrammerParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#left_quote.
    def visitLeft_quote(self, ctx:MyGrammerParser.Left_quoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#right_quote.
    def visitRight_quote(self, ctx:MyGrammerParser.Right_quoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#mul.
    def visitMul(self, ctx:MyGrammerParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#div.
    def visitDiv(self, ctx:MyGrammerParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#add.
    def visitAdd(self, ctx:MyGrammerParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#sub.
    def visitSub(self, ctx:MyGrammerParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#floatVal.
    def visitFloatVal(self, ctx:MyGrammerParser.FloatValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#variable.
    def visitVariable(self, ctx:MyGrammerParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#unary_operator.
    def visitUnary_operator(self, ctx:MyGrammerParser.Unary_operatorContext):
        return self.visitChildren(ctx)



del MyGrammerParser