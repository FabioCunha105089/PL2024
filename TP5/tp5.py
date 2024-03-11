import ply.lex as lex

saldo = 0
produtos = {
    1: ("Água", 50),
    2: ("Croissant", 70),
    3: ("Compal", 90),
    4: ("Lanche", 80),
    5: ("Bolachas", 25),
    6: ("Chocolate", 65),
    7: ("Chiclas", 45)
}

states = (
    ('moedas', 'inclusive'),
)

tokens = (
    'SELECCIONAR',
    'LISTAR',
    'MOEDA',
    'SAIR',
    'CENTIMOS',
    'EUROS'
)

t_ignore = ' \t'

def t_SELECCIONAR(t):
    r'SELECCIONAR\s+\d+'
    p_id = int(t.value.split()[1])

    if p_id in produtos:
        global saldo
        valor = produtos[p_id][1]
        if saldo >= valor:
            saldo -= valor
            print(f"Comprou {produtos[p_id][0]}")
            print(f'SALDO = {saldo/100:.2f}€')
        else:
            print('Saldo insuficiente')
    else:
        print('Produto não encontrado')

    return t


def t_LISTAR(t):
    r'LISTAR'
    print("ID | PRODUTO | PREÇO")
    print("--------------------")
    for id, prod in produtos.items():
        print(f"{id} | {prod[0]} | {prod[1]}")
    return t


def t_SAIR(t):
    r'SAIR'
    global saldo
    print(f'TROCO = {saldo/100:.2f}€')
    saldo = 0
    return t


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)
    
    
def t_newline(t):
    r'\n+'
    pass


def t_MOEDA(t):
    r'MOEDA'
    t.lexer.begin('moedas')
    return t


def t_moedas_CENTIMOS(t):
    r'((1|2|5|10|20|50)c)'
    global saldo
    saldo += int(t.value.rstrip('c'))
    return t


def t_moedas_EUROS(t):
    r'((1|2)e)'
    global saldo
    saldo += int(t.value.rstrip('e')) * 100
    return t


def t_moedas_COMMA(t):
    r','
    pass


def t_moedas_newline(t):
    r'\n+'
    t.lexer.begin('INITIAL')


def t_moedas_error(t):
    print(f"Illegal character in 'moedas' state: {t.value[0]}")
    t.lexer.skip(1)


def main():
    lexer = lex.lex()
    
    while True:
        data = input()
        lexer.input(data)
        tok = lexer.token()
        while tok:
            tok = lexer.token()
            

if __name__ == '__main__':
    main()
