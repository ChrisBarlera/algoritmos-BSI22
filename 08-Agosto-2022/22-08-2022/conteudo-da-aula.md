# Descrição
Aula inicial sobre Arrays, detalhando suas funcionalidades dentro da programação e mostrando como escrevê-los em python.

**Arrays** são homogêneos (todos os itens do mesmo tipo) e de tamanho conhecido. Precisam ter, no mínimo, um índice.
Como no Python não é necessário especificar tamanho pra criar uma variável com mais de um valor, nós simulamos esse comportamento utilizando a biblioteca *numpy*.

Exemplo de código:
```
import numpy

#Inicializa o vetor
LEN = 10
vetorX = numpy.zeros(LEN)
```
(O método `zeros()` retorna uma lista inicializada com todos os valores em 0 e d tamanho recebido por parâmetro)
