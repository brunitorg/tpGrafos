import gerarGrafo
import algoritmos
import time


def recuperaCaminhoLista(pred, d):
    caminho = []
    i = d
    while i != None:
        caminho.append(i)
        i = pred[i]
    caminho.reverse()
    return caminho

def recuperaCaminhoMatriz(pred, t):
    caminho = []
    return caminho

# def testar(alg, orig, dest):
# grafoA(alg, orig, dest, gerarGrafo.criarLista(50, 500, 1, 100))
# grafoB(alg, orig, dest, gerarGrafo.criarLista(50, 1000, 1, 10))
# grafoC(alg, orig, dest)
# grafoD(alg, orig, dest)
# grafoE(alg, orig, dest)
# grafoF(alg, orig, dest)
# grafoG(alg, orig, dest)
# grafoH(alg, orig, dest)


def grafoA(a, s, d, graph):
    if (a == 1):
        tempo = time.time()
        dist, pred = algoritmos.dijkstra(graph, s)
        tempo = time.time() - tempo
    elif a == 2:
        tempo = time.time()
        dist, pred = algoritmos.bellmanFord(graph, s)
        tempo = time.time() - tempo
    elif a == 3:
        tempo = time.time()
        matriz = gerarGrafo.transformaEmMatriz(graph)
        dist, pred = algoritmos.floydWarshall(matriz)
        tempo = time.time() - tempo

    print("Caminho:", recuperaCaminhoLista(pred, d))
    print("Custo: ", dist[len(dist) - 1])
    print("Tempo: ", tempo)


def grafoB(a, s, d, graph):
    if (a == 1):
        tempo = time.time()
        dist, pred = algoritmos.dijkstra(graph, s)
        tempo = time.time() - tempo
    elif a == 2:
        tempo = time.time()
        dist, pred = algoritmos.bellmanFord(graph, s)
        tempo = time.time() - tempo
    elif a == 3:
        tempo = time.time()
        matriz = gerarGrafo.transformaEmMatriz(graph)
        dist, pred = algoritmos.floydWarshall(matriz)
        tempo = time.time() - tempo

    print("Caminho:", recuperaCaminhoLista(pred, d))
    print("Custo: ", dist[len(dist) - 1])
    print("Tempo: ", tempo)


def grafoC(alg, s, d):
    grafo = gerarGrafo.criarLista(100, 1000, 1, 10)
    if alg == 0:
        dist, pred = algoritmos.dijkstra(grafo, s)
    elif alg == 1:
        dist, pred = algoritmos.bellmanFord(grafo, s)
    elif alg == 2:
        matriz = gerarGrafo.transformaEmMatriz(grafo)
        dist, pred = algoritmos.floydWarshall(matriz)


def grafoD(alg, s, d):
    grafo = gerarGrafo.criarLista(100, 5000, 1, 100)
    if alg == 0:
        dist, pred = algoritmos.dijkstra(grafo, s)
    elif alg == 1:
        dist, pred = algoritmos.bellmanFord(grafo, s)
    elif alg == 2:
        matriz = gerarGrafo.transformaEmMatriz(grafo)
        dist, pred = algoritmos.floydWarshall(matriz)


def grafoE(alg, s, d):
    grafo = gerarGrafo.criarLista(500, 5000, 1, 10)
    if alg == 0:
        dist, pred = algoritmos.dijkstra(grafo, s)
    elif alg == 1:
        dist, pred = algoritmos.bellmanFord(grafo, s)
    elif alg == 2:
        matriz = gerarGrafo.transformaEmMatriz(grafo)
        dist, pred = algoritmos.floydWarshall(matriz)


def grafoF(alg, s, d):
    grafo = gerarGrafo.criarLista(500, 10000, 1, 100)
    if alg == 0:
        dist, pred = algoritmos.dijkstra(grafo, s)
    elif alg == 1:
        dist, pred = algoritmos.bellmanFord(grafo, s)
    elif alg == 2:
        matriz = gerarGrafo.transformaEmMatriz(grafo)
        dist, pred = algoritmos.floydWarshall(matriz)


def grafoG(alg, s, d):
    grafo = gerarGrafo.criarLista(1000, 10000, 1, 100)
    if alg == 0:
        dist, pred = algoritmos.dijkstra(grafo, s)
    elif alg == 1:
        dist, pred = algoritmos.bellmanFord(grafo, s)
    elif alg == 2:
        matriz = gerarGrafo.transformaEmMatriz(grafo)
        dist, pred = algoritmos.floydWarshall(matriz)


def grafoH(alg, s, d):
    grafo = gerarGrafo.criarLista(1000, 50000, 1, 10)
    if alg == 0:
        dist, pred = algoritmos.dijkstra(grafo, s)
    elif alg == 1:
        dist, pred = algoritmos.bellmanFord(grafo, s)
    elif alg == 2:
        matriz = gerarGrafo.transformaEmMatriz(grafo)
        dist, pred = algoritmos.floydWarshall(matriz)
