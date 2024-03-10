# TPC4 PL 2024

## Autor
Fábio Jorge Almeida Cunha, A105089

## Relatório
Script que implementa um analisador léxico usando a biblioteca Ply para definir tokens de expressões simples de SQL.\
Tokens reconhecidos:
- SELECT_OP
- FROM_OP
- WHERE_OP
- VARIABLE
- COMMA
- NUMBER
- GREATER_THAN_EQUALS

Ignora espaços, *tabs* e carateres *newline*.\
Carateres desconhecidos são identificados como ilegais.\
O script identifica tokens e imprime-os para o ecrã.
