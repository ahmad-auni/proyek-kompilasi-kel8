import sanca_lexer
import sanca_parser
import sanca_interpreter

from sys import *

#Input langsung dari pengguna
if __name__ == '__main__':
    lexer = sanca_lexer.BasicLexer()
    parser = sanca_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('sanca > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            sanca_interpreter.BasicExecute(tree, env)
