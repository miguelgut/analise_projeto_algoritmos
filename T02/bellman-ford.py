from queue import PriorityQueue
from utils import GrafoBF
import utils

# Função que encontra a menor distância do nó origem (src) até
# todos os demais vértices usando o algoritmo Bellman-Ford. 
def bellmanFord(self, src): 

    # Inicializa todas as distancias da origem aos demais como infinito
    dist = [float("Inf")] * self.v
    dist[src] = 0

    # Um caminho mais curto da origem até qualquer vértice pode
    # ter no máximo |v| - 1 arestas. Senão é um ciclo fechado
    for _ in range(self.v - 1): 

        # Atualiza o valor da distância e o nó pai dos vértices adjacentes 
        # do vértice selecionado. Considera apenas os vértices que estão 
        # ainda na fila
        for u, v, w in self.arestas: 
            if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                    dist[v] = dist[u] + w 

    # Procura por ciclos de peso negativo. O passo acima garante a menor distancia
    # se o grafo não possui ciclos de peso negativo. Se temos um caminho menor, então
    # há um ciclo.
    for u, v, w in self.arestas: 
            if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                    print("Graph contains negative weight cycle")
                    return
    return dist  

def criarGrafo():
    g = GrafoBF(5)
    g.adicionar_aresta(0, 1, 2)
    g.adicionar_aresta(0, 2, 4)
    g.adicionar_aresta(1, 3, 2)
    g.adicionar_aresta(2, 4, 3)
    g.adicionar_aresta(2, 3, 4)
    g.adicionar_aresta(4, 3, -5)
    return g

def main():

    executionTime = []
    start = utils.getTime()
    graph = criarGrafo()
    graph.bellmanFord = bellmanFord
    result = graph.bellmanFord(graph, 0)
    end = utils.getTime()
    executionTime.append([len(result), end-start])

    print("--- %s seconds ---" % (end-start))
    for vertex in range(len(result)):
        print("A distância do vértice 0 ao", vertex, "é", result[vertex])

main()