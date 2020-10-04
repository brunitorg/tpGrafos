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
def floydWarshall(matriz):
    # Cria matrizes dist e prev
    dist = [[float('inf') for i in range(len(matriz))] for j in range(len(matriz))]
    pred = [[None for i in range(len(matriz))] for j in range(len(matriz))]

    # Preenche matrizes dist e pred
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:  # adciona 0 e None na diagonal principal de dist e prev
                dist[i][j] = 0
                pred[i][j] = None
            elif matriz[i][j] > 0:
                dist[i][j] = matriz[i][j]  # adiciona o peso a posicao i j na matriz
                pred[i][j] = i
            else:  # adciona inf e None no restante da matriz
                dist[i][j] = float('inf')
                pred[i][j] = None

    # Aqui a mágica acontece
    for k in range(len(matriz)):  # vertice ponte para caminhos alternativos passando por k
        for i in range(len(matriz)):  # a partir de i
            for j in range(len(matriz)):  # a partir de j
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


# Recupera caminho atravez da matriz de predecessores
def recuperaCaminhoMatriz(pred, s, d):
    walk = [s]
    x = s

    for i in range(len(pred)):
        if pred[x][d] != s and pred[x][d] not in walk:
            walk.append(pred[x][d])
            x = pred[x][d]
            break
    walk.append(d)

    return walk


# Recupera caminho atravez da lista de predecessores
def recuperaCaminhoLista(pred, d):
    caminho = []
    i = d
    while i != None:
        caminho.append(i)
        i = pred[i]
    caminho.reverse()
    return caminho
