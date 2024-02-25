# TPC1 PL 2024

## Autor
Fábio Jorge Almeida Cunha, A105089

## Relatório

### Cabeçalhos
Faço match de '#' no início das linhas e substituo por '<hx>' onde x é o comprimento do match.

### Bold
Faço match de '\*\**texto*\*\*' e substituo por '\<b>*texto*\</b>'

### Itálico
Faço match de '\**texto*\*' e substituo por '\<i>*texto*\</i>'

### Listas
Pego no prefixo e faço match com 'dígito.' ou '-'.\
No primeiro caso, inicío uma lista numerada com '\<ol>'. No segundo inicío uma lista não numerada com '\<ul>'.\
Em seguida, pego no texto seguinte e ponho-o entre '\<li>\</li>'.\
Quando deteto que já não apanho elementos de uma lista, fecho-a com a respetiva tag.

### Link
Faço match de '\[*texto*](*url*)' e substituo por '\<a href="*url*">*texto*\</a>'

## Imagem
Faço match de '!\[*texto*](*path*)' e substituo por '\<img src="*path*" alt="*texto*"/>'