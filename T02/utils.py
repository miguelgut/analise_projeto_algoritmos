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

def mochilaPequena():
    return [[60, 100, 120], [10,20,30]]

def mochilaGrande():
    return [[60, 100, 120, 500, 200, 30, 50, 600, 100], [10, 20,  30,  50,  10,  10, 20, 15,  10]]

def getTime():
    return time.time()

def main():
    return

main()