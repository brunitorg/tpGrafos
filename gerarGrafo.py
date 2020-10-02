import random

def criarMatriz(vertices, arestas, pesoMin, pesoMax):
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


def criarLista(vertices, arestas, pesoMin, pesoMax):
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

def transformaEmMatriz(lista):
    G = [[0 for i in range(len(lista))] for i in range(len(lista))]

    for u in range(len(lista)):
        for (v,w) in lista[u]:
            G[u][v] = w

    return G