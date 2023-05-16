# Integrantes
| Nome |  Matrícula
| :------: | :-------:
| [Fernando Vargas](https://github.com/SFernandoS) | 180016491
| [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421

# Introdução 
Este repositório foi criado para o desenvolvimento do segundo módulo de Grafos da disciplina Projeto de Algoritmos do Professor Maurício Serrano. Ele aborda os algoritmos de Dijkstra, Prim e Kruskal.
Portanto fizemos a resolução de alguns exercícios em Judges.

# Apresentação

[Link para a apresentação da dupla 29](https://youtu.be/qbtwo4-GwQA) 

# Foram feitos os exercícios no LeetCode

## [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)

Neste problema, é fornecida uma rede de nós numerados de 1 a n. Também são fornecidos tempos, uma lista de tempos de viagem como arestas direcionadas, onde times[i] = (ui, vi, wi), em que ui é o nó de origem, vi é o nó de destino e wi é o tempo necessário para que um sinal percorra do nó de origem ao nó de destino. O objetivo é enviar um sinal a partir de um determinado nó k e retornar o tempo mínimo necessário para que todos os n nós recebam o sinal. Se for impossível para todos os nós n receberem o sinal, retorne -1.

![Network Delay Time](/images/743.png)

## [ 2492. Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)

Dado um número inteiro positivo n que representa n cidades numeradas de 1 a n, e uma matriz 2D chamada roads, onde roads[i] = [ai, bi, distancei] indica que há uma estrada bidirecional entre as cidades ai e bi com uma distância igual a distancei. O grafo das cidades não necessariamente é conectado.

A pontuação de um caminho entre duas cidades é definida como a menor distância de uma estrada nesse caminho.

Retorne a pontuação mínima possível de um caminho entre as cidades 1 e n.

![Minimum Score of a Path Between Two Citie](/images/2492.png)

## [ 1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)


Dado um array de pontos chamado "points" representando as coordenadas inteiras de alguns pontos em um plano 2D, onde points[i] = [xi, yi].

O custo de conectar dois pontos [xi, yi] e [xj, yj] é a distância manhattan entre eles: |xi - xj| + |yi - yj|, onde |val| denota o valor absoluto de "val".

Retorne o custo mínimo para conectar todos os pontos. Todos os pontos são conectados se houver exatamente um caminho simples entre qualquer dois pontos.

![Minimum Score of a Path Between Two Citie](/images/1584.png)

## [ 787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

Existem n cidades conectadas por um certo número de voos. É fornecido um array chamado "flights" onde flights[i] = [fromi, toi, pricei] indica que existe um voo da cidade fromi para a cidade toi com custo pricei.

Também são fornecidos três números inteiros chamados src, dst e k. Você deve retornar o preço mais barato para viajar de src para dst com no máximo k paradas. Se não houver uma rota que satisfaça essas condições, retorne -1.

![Cheapest Flights Within K Stops](/images/787.jpeg)

## [ 1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/description/)

É fornecido um grafo ponderado não direcionado com n nós (indexados a partir de 0), representado por uma lista de arestas onde edges[i] = [a, b] é uma aresta não direcionada que conecta os nós a e b, com uma probabilidade de sucesso de atravessar essa aresta succProb[i].

Dado dois nós start e end, encontre o caminho com a maior probabilidade de sucesso para ir de start a end e retorne a sua probabilidade de sucesso.

Se não houver um caminho de start a end, retorne 0. A sua resposta será aceita se ela diferir da resposta correta em no máximo 1e-5.

![Path with Maximum Probability](/images/1514.jpeg)

# Instalação

Pré-Requisitos: Os códigos devem ser rodados na própria plataforma do leetcode, tendo em vista o uso de uma classe Solution, bem como o uso correto dos inputs por parte da plataforma.

Caso queira rodar local, é necessário somente chamar o método da classe com os paramêtros condizente com a assinatura de acordo com a linguagem desenvolvida.


# Uso
## Passo 1: Copiar o código
Entre na pasta do exercício específico, clique no arquivo e copie-o.

## Passo 2: Entrar na página do exercício
Ao clicar no título de cada questão presente neste README, você será redirecionado para a página da questão na plataforma LeetCode

## Passo 3: Alterar linguagem
Selecione a linguagem.

## Passo 4: Colar o código
Cole o código copiado no editor.

## Passo 5: Rodar o código
Abaixo do editor de código, clique em Run para executar o código.