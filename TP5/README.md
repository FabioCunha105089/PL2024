# TPC5 PL 2024

## Autor
Fábio Jorge Almeida Cunha, A105089

## Relatório
Script que implementa uma máquina de vendas através de um analisador léxico.\
Usa um estado inicial que reconhece os seguintes tokens:
- LISTAR
- SELECCIONAR
- MOEDA
- SAIR
Quando reconhece o token MOEDA, inicia o estado *moedas* para reconhecer as moedas que são inseridas.\