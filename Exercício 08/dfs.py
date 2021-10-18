import heapq
import math
class Vertice:
    def __init__(self, no) :
        self.d = math.inf
        self.id = no
        self.vizinhos = []
        self.prede = self
        self.visitado = False
    def add_vizinhos(self, vertice, peso = 0):
        aresta = Aresta(self.id, vertice, peso)
        self.vizinhos.append(aresta)
    def get_id(self):
        return self.id
    def get_vizinho(self, v):
        for i in self.vizinhos:
            if v == i.vertice2:
                return i
        return None

class Aresta:
    def __init__(self, v1, v2, peso = 0):
        self.vertice1 = v1
        self.vertice2 = v2
        self.peso = peso

class Grafo():
    def __init__(self):
        self.lista_adjacencia = []

    def add_vertice(self, no):
        self.lista_adjacencia.append(Vertice(no))

    def get_vertice(self, no):
        for i in self.lista_adjacencia:
            if(i.get_id() == no):
                return i
        return None

    def add_aresta(self, v1, v2, peso=0):
        self.get_vertice(v1).add_vizinhos(v2, peso)
        self.get_vertice(v2).add_vizinhos(v1, peso)
    
    def get_aresta(self, v1, v2):
        return self.get_vertice(v1).get_vizinho(v2)

grafo = Grafo()

grafo.add_vertice("a")
grafo.add_vertice("b")
grafo.add_vertice("c")
grafo.add_vertice("d")
grafo.add_vertice("e")
grafo.add_vertice("f")
grafo.add_vertice("g")
grafo.add_vertice("h")
grafo.add_vertice("i")
grafo.add_vertice("j")
grafo.add_vertice("k")
grafo.add_vertice("l")

grafo.add_aresta("a","d",)
grafo.add_aresta("a","c",peso=1)
grafo.add_aresta("b","d",peso=9)
grafo.add_aresta("b","e",peso=8)
grafo.add_aresta("b","f",peso=3)
grafo.add_aresta("c","e",peso=2)
grafo.add_aresta("d","g",peso=5)
grafo.add_aresta("d","h",peso=4)
grafo.add_aresta("d","j",peso=8)
grafo.add_aresta("f","j",peso=5)
grafo.add_aresta("g","h",peso=7)
grafo.add_aresta("g","i",peso=1)
grafo.add_aresta("h","i",peso=6)
grafo.add_aresta("h","j",peso=2)


