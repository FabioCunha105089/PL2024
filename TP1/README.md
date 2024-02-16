# TPC1 PL 20204

## Autor
Fábio Jorge Almeida Cunha, A105089

## Relatório

### 1. Ordenação das modalidades por ordem alfabética
Para obter a lista das modadilades ordenada, guardei as modalidades no set genre para não ter duplicadas e depois para o transformar numa lista e ordenar usei o método sorted().

### 2. Percentagem de atletas aptos e inaptos
Para obter a percentagem de aptos e inaptos, à medida que processei cada atleta, aumentei o contador total para no fim ter o total de atletas e se a letra 't' existisse no campo "Resultado", aumentei o contador fit_count para no fim obter o total de atletas aptos. Por fim, foi só dividor os aptos pelo total de atletas para obter a percentagem de cada.

### 3. Distribuição de atletas por escalão etário
Para obter a distribuição de atletas por escalão etário, por cada atleta que processei verifiquei a que escalão o atleta pertence. Num dicionário de escalões, verifico se esse escalão já existe. Se exister, adiciono um ao valor correspondente, se não, coloco o escalão no dicionário com o valor de 1. No fim, divido a quantidade de atletas em cada escalão pelo total de atletas para obter a distribuição dos atletas pelos escalões. Como não estava claro no enunciado, assumi que a distribuição seria a percentagem de atletas em cada escalão etário.