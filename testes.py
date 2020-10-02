import grafo
import algoritmos
import time

def testar():
    grafoA(0, 6, grafo.criarGrafoLista(50, 500, 1, 100))
    # grafoA(0, 49, grafo.criarGrafoLista(50, 500, 1, 100))
    #grafoB(0, 49, grafo.criarGrafoLista(50, 1000, 1, 10))
    # grafoC(0, 49, grafo.criarGrafoLista(100, 1000, 1, 10))
    # grafoD(0, 49, grafo.criarGrafoLista(100, 5000, 1, 100))
    # grafoE(0, 49, grafo.criarGrafoLista(500, 5000, 1, 10))
    # grafoF(0, 49, grafo.criarGrafoLista(500, 10000, 1, 100))
    # grafoG(0, 49, grafo.criarGrafoLista(1000, 10000, 1, 100))
    # grafoH(0, 49, grafo.criarGrafoLista(1000, 50000, 1, 10))


def recuperaCaminhoMatriz(pred, s,d):
    caminho = []
    caminho.append(s)

    i=s
    while pred[s][d] != s:
        caminho.append(pred[i][d])
        i = pred[i][d]
    caminho.append(d)

    return caminho

def recuperaCaminhoLista(pred, d):
    caminho = []
    i = d
    while i != None:
        caminho.append(i)
        i = pred[i]
    caminho.reverse()
    return caminho


def testeDijkstra(s, d, graph):
    print("---------------Dijkstra---------------")
    tempo = time.time()
    dist, pred = algoritmos.dijkstra(graph, s)
    tempo = time.time() - tempo
    caminho = recuperaCaminhoLista(pred,d)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)


def testeBellmanFord(s, d, graph):
    print("\n--------------BelmanFord--------------")
    tempo = time.time()
    dist, pred = algoritmos.bellmanFord(graph, s)
    tempo = time.time() - tempo
    caminho = recuperaCaminhoLista(pred, d)
    print("Caminho: ", caminho, "\nCusto: ", dist[len(dist) - 1], "\nTempo: ", tempo)


def testeFloydWarshall(s, d, matriz):
    print("\n--------------FloydWarshall--------------")
    tempo = time.time()
    dist, pred = algoritmos.floydWarshall(matriz)
    tempo = time.time() - tempo
    caminho = recuperaCaminhoMatriz(pred,s,d)
    print("Caminho: ", caminho, "\nCusto: ", dist[s][d], "\nTempo: ", tempo)

def grafoA(s, d, graph): #(50, 500, 1, 100)
    testeDijkstra(s, d, graph)

    testeBellmanFord(s, d, graph)

    matriz = grafo.transformaEmMatriz(graph)
    testeFloydWarshall(s, d, matriz)

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