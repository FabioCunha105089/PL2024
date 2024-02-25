# TPC3 PL 2024

## Autor
Fábio Jorge Almeida Cunha, A105089

## Relatório
O ***pattern*** usado vai detetar todos os elementos **'on'**, **'off'**, **'='** e sequências de 
dígitos que podem, ou não, ter um sinal apegado.\
Uso o ***finditer()*** para ter os matches com os elementos pela ordem em que aparecem
na linha e o ***m.group()*** para colocar o match numa lista.\
O **'on'** e o **'off'** ativam/desativam respetivamente a soma.\
O **'='** dá *print* no ecrã do valor atual da soma.\
No caso do match ser uma sequência de dígitos, se a soma estiver ativa, somo a
sequência.
