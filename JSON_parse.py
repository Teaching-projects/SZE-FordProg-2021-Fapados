from JSON_lex import JSONLexer
import ply.yacc as yacc


class JSONParser:
    def __init__(self):
        self.json_lexer = JSONLexer()

        self.json_lexer.build()
        self.tokens = self.json_lexer.tokens

        self.json_parser = yacc.yacc(module=self, start="start")
        return

    def p_value(self, p):
        """
        value : NUMBER
              | STRING
              | BOOLEAN
              | NULL
              | object
              | array
        """
        return

    def p_start(self, p):
        """
        start : object
              | array
        """
        return

    def p_object(self, p):
        """
        object : LBRACE pairs RBRACE
        """
        return

    def p_pairs(self, p):
        """
        pairs : pair
              | empty
        """
        return

    def p_pair(self, p):
        """
        pair : STRING COLON value COMMA pair
             | STRING COLON value
        """

    def p_array(self, p):
        """
        array : LBRACKET items RBRACKET
        """
        return

    def p_items(self, p):
        """
        items : item
              | empty
        """
        return

    def p_item(self, p):
        """
        item : value COMMA item
             | value
        """

    def p_empty(self, p):
        """
        empty :
        """
        return

    def p_error(self, p):
        if p:
            raise SyntaxError("Error on line {line} near position {pos} (token: '{tok}')."
                              .format(line=p.lineno, pos=p.lexpos, tok=p.value))

        else:
            if self.json_lexer.array_depth != 0:
                raise SyntaxError("You seem to have an unclosed array.")
            elif self.json_lexer.object_depth != 0:
                raise SyntaxError("You seem to have an unclosed object.")

            raise SyntaxError("There's something wrong...")

    def parse(self, text):
        self.json_parser.parse(input=text, lexer=self.json_lexer)
        return True


if __name__ == "__main__":
    j = JSONParser()
    j.parse(r"""
    {,}
    """)
