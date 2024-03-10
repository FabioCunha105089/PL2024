import ply.lex as lex

tokens = (
    'SELECT_OP',
    'FROM_OP',
    'WHERE_OP',
    'VARIABLE',
    'COMMA',
    'NUMBER',
    'GREATER_THAN_EQUALS'
)

t_VARIABLE = r'[A-Za-z_]*[A-Za-z0-9-_\.]'
t_COMMA = r'\,'
t_GREATER_THAN_EQUALS = r'\>\='

def t_SELECT_OP(t):
    r'SELECT'
    return t


def t_FROM_OP(t):
    r'FROM'
    return t


def t_WHERE_OP(t):
    r'WHERE'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


def main():
    lexer = lex.lex()
    data = input()
    lexer.input(data)
    
    tok = lexer.token()
    while tok:
        print(tok)
        tok = lexer.token()


if __name__ == '__main__':
    main()
