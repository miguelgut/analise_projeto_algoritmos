from queue import PriorityQueue
from utils import GrafoDijkstra
import utils

def dijkstra(self, start_vertex):
    D = {v:float('inf') for v in range(self.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        self.visitado.append(current_vertex)

        for neighbor in range(self.v):
            if self.arestas[current_vertex][neighbor] != -1:
                distance = self.arestas[current_vertex][neighbor]
                if neighbor not in self.visitado:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

def criarGrafo():
    g = GrafoDijkstra(9)
    g.adicionar_aresta(0, 1, 4)
    g.adicionar_aresta(0, 6, 7)
    g.adicionar_aresta(1, 6, 11)
    g.adicionar_aresta(1, 7, 20)
    g.adicionar_aresta(1, 2, 9)
    g.adicionar_aresta(2, 3, 6)
    g.adicionar_aresta(2, 4, 2)
    g.adicionar_aresta(3, 4, 10)
    g.adicionar_aresta(3, 5, 5)
    g.adicionar_aresta(4, 5, 15)
    g.adicionar_aresta(4, 7, 1)
    g.adicionar_aresta(4, 8, 5)
    g.adicionar_aresta(5, 8, 12)
    g.adicionar_aresta(6, 7, 1)
    g.adicionar_aresta(7, 8, 3) 
    return g

def criarGrafoGrande():
    g = GrafoDijkstra(30)
    g.adicionar_aresta(0, 1, 4)
    g.adicionar_aresta(0, 6, 7)
    g.adicionar_aresta(1, 6, 11)
    g.adicionar_aresta(1, 7, 20)
    g.adicionar_aresta(1, 2, 9)
    g.adicionar_aresta(2, 3, 6)
    g.adicionar_aresta(2, 4, 2)
    g.adicionar_aresta(3, 4, 10)
    g.adicionar_aresta(3, 5, 5)
    g.adicionar_aresta(4, 5, 15)
    g.adicionar_aresta(4, 7, 1)
    g.adicionar_aresta(4, 8, 5)
    g.adicionar_aresta(5, 8, 12)
    g.adicionar_aresta(6, 7, 1)
    g.adicionar_aresta(7, 8, 3) 
    
    return g

def main():

    executionTime = []
    start = utils.getTime()
    graph = criarGrafo()
    graph.dijkstra = dijkstra

    result = graph.dijkstra(graph, 0)

    end = utils.getTime()
    executionTime.append([len(result), end-start])

    print("--- %s seconds ---" % (end-start))

    for vertex in range(len(result)):
        print("A distância do vértice 0 ao", vertex, "é", result[vertex])

main()