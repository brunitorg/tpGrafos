import grafo
import algoritmos
import time

# def testar():
#     grafoA(0, 45, grafo.criarGrafoLista(500,5000, 1, 10))
#     grafoB(0, 49, grafo.criarGrafoLista(50, 1000, 1, 10))
#     grafoC(0, 49, grafo.criarGrafoLista(100, 1000, 1, 10))
#     grafoD(0, 49, grafo.criarGrafoLista(100, 5000, 1, 100))
#     grafoE(0, 49, grafo.criarGrafoLista(500, 5000, 1, 10))
#     grafoF(0, 49, grafo.criarGrafoLista(500, 10000, 1, 100))
#     grafoG(0, 49, grafo.criarGrafoLista(1000, 10000, 1, 100))
#     grafoH(0, 49, grafo.criarGrafoLista(1000, 50000, 1, 10))


def testeDijkstra(s, d, graph):
    print("---------------Dijkstra---------------")
    tempo = time.time()
    dist, pred = algoritmos.dijkstra(graph, s)
    tempo = time.time() - tempo
    caminho = algoritmos.recuperaCaminhoLista(pred, d)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)


def testeBellmanFord(s, d, graph):
    print("\n--------------BelmanFord--------------")
    tempo = time.time()
    dist, pred = algoritmos.bellmanFord(graph, s)
    tempo = time.time() - tempo
    caminho = algoritmos.recuperaCaminhoLista(pred, d)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)


def testeFloydWarshall(s, d, matriz):
    print("\n--------------FloydWarshall--------------")
    tempo = time.time()
    dist, pred = algoritmos.floydWarshall(matriz)
    tempo = time.time() - tempo
    caminho = algoritmos.recuperaCaminhoMatriz(pred, s, d)
    print("Caminho: ", caminho, "\nCusto: ", dist[s][d], "\nTempo: ", tempo)


def grafoA(s, d, graph):  # (50, 500, 1, 100)
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    testeFloydWarshall(s, d, grafo.transformaEmMatriz(graph))


def grafoB(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)


def grafoC(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)


def grafoD(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)


def grafoE(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)


def grafoF(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)


def grafoG(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)


def grafoH(s, d, graph):
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)
