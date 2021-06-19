import ply.lex as lex
from ply.lex import TOKEN


class JSONLexer(object):
    tokens = (
        "STRING",
        "NUMBER",
        "LBRACE",
        "RBRACE",
        "LBRACKET",
        "RBRACKET",
        "COMMA",
        "COLON",
        "BOOLEAN",
        "NULL"
    )

    lbrace = r'\{'
    rbrace = r'\}'
    lbracket = r'\['
    rbracket = r'\]'

    t_BOOLEAN = r'(true|false)'
    t_NULL = r'(null)'

    t_NUMBER = r'(-?)(0|[1-9][0-9]*)(\.[0-9]*)?([eE][+\-]?[0-9]*)?'

    t_STRING = r'"(\\[bfrnt"/\\]|[^\u0022\u005C\u0000-\u001F\u007F-\u009F]|\\u[0-9a-fA-F]{4})*"'

    t_COMMA = r','

    t_COLON = r':'

    t_ignore = '\t\r '

    def __init__(self):
        self.lexer = None

        self.array_depth = 0

        self.object_depth = 0

        self.last_token = None

        self.line_pos = 0
        return

    @TOKEN(lbrace)
    def t_LBRACE(self, t):
        self.object_depth += 1
        return t

    @TOKEN(rbrace)
    def t_RBRACE(self, t):
        self.object_depth -= 1
        return t

    @TOKEN(lbracket)
    def t_LBRACKET(self, t):
        self.array_depth += 1
        return t

    @TOKEN(rbracket)
    def t_RBRACKET(self, t):
        self.array_depth -= 1
        return t

    def t_NEWLINE(self, t):
        r"""\n+"""
        t.lexer.lineno += t.value.count("\n")
        self.line_pos = 0
        return

    def t_error(self, t):
        raise SyntaxError("Illegal character '{s}' on line {line} near position {pos}."
                          .format(s=t.value[0], line=t.lexer.lineno, pos=t.lexer.lexpos))

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return

    def input(self, text):
        self.lexer.input(text)
        return

    def token(self):
        self.last_token = self.lexer.token()
        return self.last_token

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok.type, tok.value, tok.lexpos)

        return


if __name__ == "__main__":
    l = JSONLexer()
    l.build()
    l.test(r'""')
