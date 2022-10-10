# Descrição
Aula inicial sobre **tuplas , conjuntos e dicionários**, detalhando suas funcionalidades dentro da programação e mostrando como usar e escrevê-los em Python.

## Tuplas
Tuplas são muito semelhantes às listas, porém têm a diferença de serem imutáveis e declaradas em parenteses (opcionais, também pode ser `tupla = 1, 2, 3`) no Python.

- `lista = [1, 2, 3]`
- `tupla = (1, 2, 3)`

- `tupla = ()` : Tupla vazia
- `tupla = (1)` : **NÃO** é tupla
- `tupla = (2,)` : Tupla com um elemento
- `tupla = 2,` : Tupla com um elemento

Tuplas **NÃO** podem ter seus valores alterados, porém, é possível realizar operações com seus valores.
```
t = 'a','b' #Cria a tupla
print(t*2)  #('a','b','a','b')
```

## Conjuntos
São uma estrutura de dados que implementa operações de união, intersecção, diferença, entre outros. (Representam os conjuntos matemáticos dentro do python)

Características principais:
- Não admitir a repetição de elementos
- Não mantém a ordem dos elementos

```
C = set()   #Cria o conjunto C
C.add(1)    #Adiciona o valor 1 ao conjunto

print(C)    #{1}
```

## Dicionário

Ao contrário do que vimos agora com listas indexadas em que acessamos os elementos através de um índice numérico, os dicionários são listas acessáveis através de uma chave (string).

```
pessoa = {'nome':'fulano','idade':18}   #Declarando um dicionário
print(pessoa)           #{'nome':'fulano','idade':18}
print(pessoa[0])        #Erro
print(pessoa['nome'])   #Fulano
print(pessoa['idade'])  #18
```


# Atividades
Refazer atividades anteriores mas dessa vez utilizando os novos conhecimentos de tuplas conjuntos e dicionários.

[Lista](Lista%20II.pdf)