import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from antlr4 import *
from gen.EZgraphLexer import EZgraphLexer
from gen.EZgraphParser import EZgraphParser
from gen.EZgraphInterpreterVisitor import EZgraphInterpreterVisitor
from gen.EZgraphVisitor import EZgraphVisitor

def main(argv):
    input = FileStream("input.txt")
    lexer = EZgraphLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EZgraphParser(stream)
    tree = parser.s()
    output = open("output.py", "w")
    Interprete = EZgraphInterpreterVisitor()
    Interprete.visit(tree)


    output.close()


if __name__ == '__main__':
    main(sys.argv)