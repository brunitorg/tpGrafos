# iniciar aplicação
import testes
import grafo
import time
import algoritmos
import sys

#Recebe valores para criar grafo
vertices = int(input("Número de vértices: "))
arestas = int(input("Número de arestas: "))
pesoMin = int(input("Peso mínimo das arestas: "))
pesoMax = int(input("Peso máxima das arestas: "))
if vertices <= 0 or arestas <= 0 or pesoMin <=0 or pesoMax<=0:
    sys.exit("Valores devem ser maiores que 0!")

#Recebe o algoritmo a ser usado
algoritmo = int(input("Escolha o Algoritmo:\n  1 - Digkstra\n  2 - Bellman-Ford\n  3 - Floyd-Warshall\n"))
if algoritmo <= 0 or algoritmo > 3:
    sys.exit("Algoritmo inválido!")

#Recebe vertice origem e destino para o caminho mínimo
s = int(input("Origem: "))
if s < 0:
    sys.exit("Origem deve ser maior ou igual a 0!")

t = int(input("Destino: "))
if t >= vertices or t <= s:
    sys.exit("Destino menor que origem ou maior que número de vertices do grafo!")


print("Processando...")


if algoritmo == 1:
    print("---------------Dijkstra---------------")
    graph = grafo.criarGrafoLista(vertices,arestas,pesoMin,pesoMax)
    print(graph)
    tempo = time.time()
    dist, pred = algoritmos.dijkstra(graph, s)
    tempo = time.time() - tempo
    caminho = algoritmos.recuperaCaminhoLista(pred, t)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)

elif algoritmo == 2:
    print("\n--------------BelmanFord--------------")
    graph = grafo.criarGrafoLista(vertices,arestas,pesoMin,pesoMax)
    print(graph)
    tempo = time.time()
    dist, pred = algoritmos.bellmanFord(graph, s)
    tempo = time.time() - tempo
    caminho = algoritmos.recuperaCaminhoLista(pred, t)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)

elif algoritmo == 3:
    print("\n--------------FloydWarshall--------------")
    matrix = grafo.criarGrafoMatriz(vertices, arestas, pesoMin, pesoMax)
    print(matrix)
    tempo = time.time()
    dist, pred = algoritmos.floydWarshall(matrix)
    tempo = time.time() - tempo
    caminho = algoritmos.recuperaCaminhoMatriz(pred, s, t)
    print(pred)
    print("Caminho: ", caminho, "\nCusto: ", dist[s][t], "\nTempo: ", tempo)


print(":----------------Obrigado----------------: ")