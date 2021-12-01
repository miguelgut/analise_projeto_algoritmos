class Grafo:

    def __init__(self, num_vertices):
        self.v = num_vertices
        self.arestas = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visitado = []

    def adicionar_aresta(self, u, v, weight):
        self.arestas[u][v] = weight
        self.arestas[v][u] = weight