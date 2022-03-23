from sly import Lexer

class BasicLexer(Lexer):
    #Himpunan token
    tokens = {NAME, NUMBER, STRING, PRINT, FOR, TO, IF, THEN, ELSE, FUNCTION, ARROW, EQ}
    literals = {'=', '+', '-', '*', '/', '(', ')', ';', '<', '>'}
    ignore = '\t '

    #Ekspresi regular untuk token
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    PRINT = r'cetak'
    FOR = r'untuk'
    TO = r'sampai'
    IF = r'jika' 
    THEN = r'maka'
    ELSE = r'jikatidak' 
    FUNCTION = r'fungsi' 
    ARROW = r'=>'
    EQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    #abaikan komentar
    @_(r'%.*')
    def COMMENT(self, t):
        pass

    #pelacak nomor baris
    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('sanca > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
