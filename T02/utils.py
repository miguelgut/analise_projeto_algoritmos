import numpy as np
import pandas as pd
import time


class GrafoDijkstra:

    def __init__(self, num_vertices):
        self.v = num_vertices
        self.arestas = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visitado = []

    def adicionar_aresta(self, u, v, weight):
        self.arestas[u][v] = weight
        self.arestas[v][u] = weight

class GrafoBF:

    def __init__(self, num_vertices):
        self.v = num_vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, weight):
        self.arestas.append([u,v,weight])

# def generateRandom(min, max, n):
#     randnums = np.random.default_rng().integers(low=min, high=max, size=n)
#     return randnums

# def generateTestUnits(min, max, units):
#     n = 10

#     for i in range(2, units+1):
#         listGen = generateRandom(min, max, n)
#         filename =  "datasets/" + str(i) + "_" + f"{n:,}"
#         saveDataFrame(listGen, filename)
#         if (i >= 5):
#             n = 2*n
#         else:
#             n = 10*n

# def saveDataFrame(myList, filename):
#     my_df = pd.DataFrame(myList)
#     my_df.to_csv(filename + ".csv", index=False, header=False)

# def createFiles():
#     generateTestUnits(1, 999, 11)

# def getFile(filename):
#     filename =  "datasets/" + filename
#     return pd.read_csv(filename + ".csv").values.tolist()

# def getFiles():
#     n = 10

#     for i in range(2, 12):
#         filename =  "datasets/" + str(i) + "_" + f"{n:,}"
#         yield pd.read_csv(filename + ".csv").values.tolist()
        
#         if (i >= 5):
#             n = 2*n
#         else:
#             n = 10*n

def getTime():
    return time.time()

def main():
    return

main()