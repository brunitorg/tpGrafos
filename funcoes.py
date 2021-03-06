# implementação dos algoritmos solicitados no TP
import random
# Implementação algoritmo dijkstra
# Recebe lista de Adjacencia e origem
# Retorna dist e pred
def dijkstra(grafo, s):

    # chama função para gerar dist e pred
    dist,pred = gerarDistPredLista(len(grafo))

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
        Q.remove(u)

        for tupla in grafo[u]:  # Confere distancia entre adjacentes
            if dist[tupla[0]] > dist[u] + tupla[1]:
                dist[tupla[0]] = dist[u] + tupla[1]
                pred[tupla[0]] = u

    return dist, pred


# Implementação algoritmo BellmanFord
# Recebe lista de Adjacencia e origem
# Retorna dist e pred
def bellmanFord(grafo, s,arestas):

    #chama função para gerar dist e pred
    dist,pred = gerarDistPredLista(len(grafo))

    dist[s] = 0

    for i in range(len(grafo)):
        trocou = False
        for e in arestas:
            if dist[e[1]] > dist[e[0]] + e[2]:
                dist[e[1]] = dist[e[0]] + e[2]
                pred[e[1]] = e[0]
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
            if i == j:  # adciona 0 na diagonal principal de dist
                dist[i][j] = 0
            elif matriz[i][j] != 0:
                dist[i][j] = matriz[i][j] # adiciona o peso a posicao i j na matriz
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


def gerarDistPredLista(tamanho): #gera dist e pred para os algoritmos Dijkstra e BellmanFord
    dist = []
    pred = []
    # Preenche listas dist e pred
    for v in range(tamanho):
        dist.append(float('inf'))
        pred.append(None)

    return dist,pred


# Recupera caminho atravez da matriz de predecessores
def recuperaCaminhoMatriz(pred, s, d):
    walk = [d]
    aux = d

    while aux != s:
        walk.append(pred[s][aux])
        aux = pred[s][aux]

    walk.reverse()

    return walk


# Recupera caminho atravez da lista de predecessores
def recuperaCaminhoLista(pred, s,d):
    walk = []
    aux = d
    while aux != s:
        walk.append(aux)
        aux = pred[aux]
    walk.append(s)
    walk.reverse()
    return walk

def criarGrafoMatriz(vertices, arestas, pesoMin, pesoMax):
    G = [[0 for i in range(vertices)] for i in range(vertices)]
    i = 0
    while i < arestas:
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v and G[u][v] == 0:
            peso = random.randint(pesoMin, pesoMax)
            G[u][v] = peso
            G[v][u] = peso
            i += 1
    return G

def criarGrafoLista(vertices, arestas, pesoMin, pesoMax):
    G = [[] for i in range(vertices)]
    i = 0
    while i < arestas:
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v:
            peso = random.randint(pesoMin, pesoMax)
            aux = 0
            for tupla in G[u]:
                if tupla[0] == v:
                    aux += 1
            if aux == 0:
                G[u].append((v, peso))
                G[v].append((u, peso))
                i += 1
    return G

#utilizada nos testes para converter o grafo de lista de adj para matriz de adj e usar o memso grafo nos 3 algoritmos
def transformaEmMatriz(lista):
    G = [[0 for i in range(len(lista))] for i in range(len(lista))]

    for u in range(len(lista)):
        for (v, w) in lista[u]:
            G[u][v] = w

    return G

#usado para gerar lista de arestas para facilitar a utilização do algoritmo de Bellman-Ford
def getArestas(lista):
    arestas = []
    for i in range(len(lista)):
        for tupla in lista[i]:
            arestas.append((i,tupla[0],tupla[1]))
    return arestas