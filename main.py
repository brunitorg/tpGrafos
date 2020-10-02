# iniciar aplicação
import testes
import grafo
import time
import algoritmos
testes.testar()
# algoritmo = int(input("Escolha o Algoritmo:\n  "
#       "1 - Digkstra\n  "
#       "2 - Bellman-Ford\n  "
#       "3 - Floyd-Warshall\n"))
#
# s = int(input("Origem: "))
# t = int(input("Destino: "))
#
# print("Processando...")
#
# graph = grafo.criarGrafoLista(50, 500, 1, 100)
#
# if algoritmo == 1:
#     tempo = time.time()
#     dist, pred = algoritmos.dijkstra(graph, s)
#     tempo = time.time() - tempo
#     caminho = testes.recuperaCaminhoLista(pred, t)
# elif algoritmo == 2:
#     tempo = time.time()
#     dist, pred = algoritmos.bellmanFord(graph, s)
#     tempo = time.time() - tempo
#     caminho = testes.recuperaCaminhoLista(pred, t)
# elif algoritmo == 3:
#     matriz = grafo.transformaEmMatriz(graph)
#     tempo = time.time()
#     dist, pred = algoritmos.floydWarshall(matriz)
#     tempo = time.time() - tempo
#     print("Dist: ",dist,
#           "\nPred: ",pred)
#
# if algoritmo!=3:
#     print("Caminho:", caminho)
#     print("Custo: ", dist[len(dist) - 1])
# print("Tempo: ", tempo)