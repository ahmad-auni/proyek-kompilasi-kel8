import sanca_lexer
import sanca_parser
import sanca_interpreter

from sys import *

#Di run di terminal dengan program yang telah dibuat
lexer = sanca_lexer.BasicLexer()
parser = sanca_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    sanca_interpreter.BasicExecute(tree, env)
