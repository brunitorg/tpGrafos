# iniciar aplicação
import funcoes
import sys
import time

# Recebe valores para criar grafo
vertices = int(input("Número de vértices: "))
arestas = int(input("Número de arestas: "))
pesoMin = int(input("Peso mínimo das arestas: "))
pesoMax = int(input("Peso máxima das arestas: "))
if vertices <= 0 or arestas <= 0 or pesoMin <= 0 or pesoMax <= 0:
    sys.exit("Valores devem ser maiores que 0!")

imprimir = int(input("Deseja imprimir o grafo? 1 - Sim // 0 - Não: "))

# Recebe o algoritmo a ser usado
algoritmo = int(input("Escolha o Algoritmo:\n  1 - Digkstra\n  2 - Bellman-Ford\n  3 - Floyd-Warshall\n"))
if algoritmo <= 0 or algoritmo > 3:
    sys.exit("Algoritmo inválido!")

# Recebe vertice origem e destino para o caminho mínimo
s = int(input("Origem: "))
if s < 0:
    sys.exit("Origem deve ser maior ou igual a 0!")

t = int(input("Destino: "))
if t >= vertices or t < 0 or t == s:
    sys.exit("Destino menor que origem ou maior que número de vertices do grafo!")

print("Processando...")

if algoritmo == 1:
    graph = funcoes.criarGrafoLista(vertices, arestas, pesoMin, pesoMax)
    if imprimir == 1:
        print(graph)
    print("---------------Dijkstra---------------")
    tempo = time.time()
    dist, pred = funcoes.dijkstra(graph, s)
    tempo = time.time() - tempo
    caminho = funcoes.recuperaCaminhoLista(pred, s, t)
    print("Origem: ", s, "\nDestino: ", t, "\nCaminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)

elif algoritmo == 2:
    graph = funcoes.criarGrafoLista(vertices, arestas, pesoMin, pesoMax)
    if imprimir == 1:
        print(graph)
    print("\n--------------BelmanFord--------------")
    tempo = time.time()
    dist, pred = funcoes.bellmanFord(graph, s)
    tempo = time.time() - tempo
    caminho = funcoes.recuperaCaminhoLista(pred, s, t)
    print("Origem: ", s, "\nDestino: ", t, "\nCaminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)

elif algoritmo == 3:
    matrix = funcoes.criarGrafoMatriz(vertices, arestas, pesoMin, pesoMax)
    if imprimir == 1:
        print(matrix)
    print("\n--------------FloydWarshall--------------")
    tempo = time.time()
    dist, pred = funcoes.floydWarshall(matrix)
    tempo = time.time() - tempo
    caminho = funcoes.recuperaCaminhoMatriz(pred, s, t)
    print("Origem: ", s, "\nDestino: ", t, "\nCaminho: ", caminho, "\nCusto: ", dist[s][t], "\nTempo: ", tempo)

print(":----------------Obrigado----------------: ")
