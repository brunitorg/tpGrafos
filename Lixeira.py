import algoritmos
import time
import grafo

G = [
    [(1,6),(2,2)],
    [(2,3),(3,1),(4,3)],
    [(1,2),(3,5)],
    [(4,3)],
    []
]

G2 = [
    [(1,1)],
    [(0,4),(2,2),(3,3)],
    [(3,3),(4,3)],
    [(1,1),(4,4)],
    [(0,5),(1,1)]
]
matriz = [
    [0,6,2,0],
    [3,0,7,5],
    [0,2,0,1],
    [0,0,4,0],
]

#dist,pred = Algoritmos.Dijkstra(G,0)
#print("Distancia: ",dist,"\nPredecessor: ",pred)
inicio = time.time()
#dist,pred = Algoritmos.BellmanFord(G,0)
#print("Distancia: ",dist,"\nPredecessor: ",pred)
fim = time()

inicio = time.time()
dist,pred = algoritmos.floydWarshall(matriz)
fim = time.time()

print("Tempo: ",fim-inicio)
print("Distancia")
for i in range(len(dist)):
    print(dist[i])

print("Predecessor")
for i in range(len(pred)):
    print(pred[i])

#Grafos aleatorios

G = [[0 for i in range(numv)] for i in range(numv)]
        print(G)
        i = 0
        while i < nume:
            u = random.randint(0, numv - 1)
            v = random.randint(0, numv - 1)
            if u != v and G[u][v] == 0:
                G[u][v] = 1
                G[v][u] = 1
                i += 1
        return G


inicio = time.time()
dist,pred = Algoritmos.bellmanFord(G,0)
fim = time.time() - inicio
print("Normal")
print("Dist:\n",dist,"\nPred:\n",pred,"\nTempo: ",fim)


inicio = time.time()
dist,pred = Algoritmos.bellmanComGet(G,0)
fim = time.time() - inicio
print("Com Get")
print("Dist:\n",dist,"\nPred:\n",pred,"\nlalala: ",fim)