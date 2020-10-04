# iniciar aplicação
import testes
import grafo
import time
import algoritmos

vertices = int(input("Número de vértices: "))
arestas = int(input("Número de arestas: "))
pesoMin = int(input("Peso mínimo das arestas: "))
pesoMax = int(input("Peso máxima das arestas: "))


algoritmo = int(input("Escolha o Algoritmo:\n  "
    "1 - Digkstra\n  "
    "2 - Bellman-Ford\n  "
    "3 - Floyd-Warshall\n"))


s = int(input("Origem: "))
t = int(input("Destino: "))


print("Processando...")

if algoritmo == 1:
    print("---------------Dijkstra---------------")
    graph = grafo.criarGrafoLista(vertices,arestas,pesoMin,pesoMax)
    print(graph)
    tempo = time.time()
    dist, pred = algoritmos.dijkstra(graph, s)
    tempo = time.time() - tempo
    caminho = testes.recuperaCaminhoLista(pred, t)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)

elif algoritmo == 2:
    print("\n--------------BelmanFord--------------")
    graph = grafo.criarGrafoLista(vertices,arestas,pesoMin,pesoMax)
    print(graph)
    tempo = time.time()
    dist, pred = algoritmos.bellmanFord(graph, s)
    tempo = time.time() - tempo
    caminho = testes.recuperaCaminhoLista(pred, t)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)

elif algoritmo == 3:
    print("\n--------------FloydWarshall--------------")
    matrix = grafo.criarGrafoMatriz(vertices, arestas, pesoMin, pesoMax)
    print(matrix)
    tempo = time.time()
    dist, pred = algoritmos.floydWarshall(matrix)
    tempo = time.time() - tempo
    caminho = testes.recuperaCaminhoMatriz(pred, s, t)
    print("Caminho: ", caminho, "\nCusto: ", dist[s][t], "\nTempo: ", tempo)


print(":----------------Obrigado----------------: ")