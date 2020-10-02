# implementação dos algoritmos solicitados no TP

# Implementação algoritmo dijkstra
# Recebe lista de Adjacencia e origem
# Retorna dist e pred
def dijkstra(grafo, s):
    dist = []
    pred = []
    # Preenche listas dist e pred
    for v in range(len(grafo)):  # Preenche dist e pred
        dist.append(float('inf'))
        pred.append(None)

    dist[s] = 0

    Q = [i for i in range(len(grafo))]  # Preenche lista auxiliar Q

    while Q:  # Enquanto existir arestas faça
        menor = float('inf')
        u = -1
        for v in Q:
            if dist[v] < menor:
                menor = dist[v]
                u = v
        if u == -1:
            break

        adjacentes = grafo[u]
        Q.remove(u)

        if len(adjacentes):
            for tupla in adjacentes:  # Confere distancia entre adjacentes
                if dist[tupla[0]] > dist[u] + tupla[1]:
                    dist[tupla[0]] = dist[u] + tupla[1]
                    pred[tupla[0]] = u

    return dist, pred


# Implementação algoritmo BellmanFord
# Recebe lista de Adjacencia e origem
# Retorna dist e pred
def bellmanFord(grafo, s):
    dist = []
    pred = []
    # Preenche listas dist e pred
    for v in range(len(grafo)):
        dist.append(float('inf'))
        pred.append(None)

    dist[s] = 0

    for i in range(len(grafo)):
        trocou = False
        for vertice in range(len(grafo)):
            if grafo[vertice]:
                for tupla in grafo[vertice]:
                    if dist[tupla[0]] > dist[vertice] + tupla[1]:
                        dist[tupla[0]] = dist[vertice] + tupla[1]
                        pred[tupla[0]] = vertice
                        trocou = True

        if not trocou:
            break

    return dist, pred


# Implementação algoritmo Floyd-Warshall
# Recebe matriz de Adjacencia e origem
# Retorna matrizes dist e pred
def floydWarshall(grafo):
    # Cria matrizes dist e prev
    dist = [[float('inf') for i in range(len(grafo))] for j in range(len(grafo))]
    pred = [[None for i in range(len(grafo))] for j in range(len(grafo))]

    # Preenche matrizes dist e pred
    for i in range(len(grafo)):
        for j in range(len(grafo)):
            if i == j:  # adciona 0 e None na diagonal principal de dist e prev
                dist[i][j] = 0
                pred[i][j] = None
            elif grafo[i][j] > 0:
                dist[i][j] = grafo[i][j]  # adiciona o peso a posicao i j na matriz
                pred[i][j] = i
            else:  # adciona inf e None no restante da matriz
                dist[i][j] = float('inf')
                pred[i][j] = None

    for k in range(len(grafo)):  # vertice ponte para caminhos alternativos passando por k
        for i in range(len(grafo)):  # a partir de i
            for j in range(len(grafo)):  # a partir de j
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred
