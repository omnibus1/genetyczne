import sys
from antlr4 import *
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
import math
start_index = {}
import sys

def simple_equation(ctx):
    try:
        first_is_simple = not (ctx.parentCtx.children[1].binary_operator() or ctx.parentCtx.children[1].unary_operator())
    except:
        first_is_simple = True
    try:
        second_is_simple = not (ctx.parentCtx.children[3].binary_operator() or ctx.parentCtx.children[3].unary_operator())
    except:
        second_is_simple = True
    return first_is_simple, second_is_simple

class MyVisitor(MyGrammerVisitor):
    output = ""
    node_index = {}

    # Visit a parse tree produced by MyGrammerParser#expr.
    def visitExpr(self, ctx: MyGrammerParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyGrammerParser#binary_operator.
    def visitBinary_operator(self, ctx: MyGrammerParser.Binary_operatorContext):
        first_simple, second_simple= simple_equation(ctx)

        if first_simple and second_simple:
            first_float = ctx.parentCtx.children[1].floatVal()
            second_float = ctx.parentCtx.children[3].floatVal()
            if first_float and second_float:
                self.output += "<"+str(eval(ctx.parentCtx.getText()[1:-1]))+">"
            else:
                self.output += ctx.parentCtx.getText()[1:-1]

        elif first_simple:
            self.output += ctx.parentCtx.children[1].getText()
            self.output += ctx.getText()
            self.visitChildren(ctx)

        elif second_simple:
            self.output += ctx.getText()
            self.output += ctx.parentCtx.children[3].getText()

        else:
            self.output += ctx.getText()
        self.visitChildren(ctx)

    # Visit a parse tree produced by MyGrammerParser#mul.
    def visitMul(self, ctx: MyGrammerParser.MulContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyGrammerParser#div.
    def visitDiv(self, ctx: MyGrammerParser.DivContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyGrammerParser#add.
    def visitAdd(self, ctx: MyGrammerParser.AddContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyGrammerParser#sub.
    def visitSub(self, ctx: MyGrammerParser.SubContext):
        return self.visitChildren(ctx)

    def visitLeft_quote(self, ctx: MyGrammerParser.Left_quoteContext):
        self.output += "("
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#right_quote.
    def visitRight_quote(self, ctx:MyGrammerParser.Right_quoteContext):
        self.output += ")"
        return self.visitChildren(ctx)

    def visitUnary_operator(self, ctx:MyGrammerParser.Unary_operatorContext):
        is_simple = ctx.parentCtx.children[2].floatVal()
        if is_simple:
            new_str = ctx.parentCtx.getText()
            new_str = new_str.replace("sin", "math.sin")
            new_str = new_str.replace("cos", "math.cos")
            val = eval(new_str)
            self.output += str(val)
        else:
            self.output += ctx.getText()
        return self.visitChildren(ctx)

    def format_output(self):
        output = self.output
        output = output.replace("()", "")
        output = output.replace("(<", "")
        output = output.replace(">)", "")
        return output

def simplify_expression(input):
    first_input = input
    while True:
        data = InputStream(input)
        lexer = MyGrammerLexer(data)
        stream = CommonTokenStream(lexer)
        parser = MyGrammerParser(stream)
        tree = parser.expr()
        visitor = MyVisitor()
        visitor.visit(tree)
        output = visitor.format_output()

        if input == output or not (output.startswith("(") or output.startswith("sin") or output.startswith("cos")):
            break
        else:
            input = output

    return output


def print_resoult(input, output):
    print("")
    print("======================")
    print(input)
    print("simplified:")
    print(output)
    print("======================")
    print("")

def clear_output(output):
    output = output.replace("()", "")
    output = output.replace("(<", "")
    output = output.replace(">)", "")
    return output


if __name__ == "__main__":         
    equation_file = open(sys.argv[1], "r")
    print(simplify_expression(equation_file.read()))

