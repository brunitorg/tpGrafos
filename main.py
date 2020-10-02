# iniciar aplicação
import testes
import gerarGrafo
import time
import algoritmos
algoritmo = int(input("Escolha o Algoritmo:\n  "
      "1 - Digkstra\n  "
      "2 - Bellman-Ford\n  "
      "3 - Floyd-Warshall\n"))

s = int(input("Origem: "))
t = int(input("Destino: "))

print("Processando...")

graph = gerarGrafo.criarLista(50,500,1,100)

if algoritmo == 1:
    tempo = time.time()
    dist, pred = algoritmos.dijkstra(graph, s)
    tempo = time.time() - tempo
elif algoritmo == 2:
    tempo = time.time()
    dist, pred = algoritmos.bellmanFord(graph, s)
    tempo = time.time() - tempo
elif algoritmo == 3:
    matriz = gerarGrafo.transformaEmMatriz(graph)
    tempo = time.time()
    dist, pred = algoritmos.floydWarshall(matriz)
    tempo = time.time() - tempo

print("Caminho:", testes.recuperaCaminho(pred, t))
print("Custo: ", dist[len(dist) - 1])
print("Tempo: ", tempo)