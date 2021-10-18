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

grafo.add_aresta("a","d",peso=1)
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

def busca_Largura(G, v):
    G.get_vertice(v).d = 0
    G.get_vertice(v).prede = Vertice("não possui, ele é a Raiz")
    estado_da_fila = []
    estado_da_visitados = []
    visitados, fila = [], [v]
    while True:
        #print(fila)
        if not fila:
            estado_da_fila.append(fila.copy())
            estado_da_visitados.append(visitados.copy())
            break
        estado_da_fila.append(fila.copy())
        vertice = fila.pop(0)
        if vertice not in visitados:
            estado_da_visitados.append(visitados.copy())
            visitados.append(vertice)
            for  i in G.get_vertice(vertice).vizinhos:
                if i.vertice2 not in fila and i.vertice2 not in visitados:
                    G.get_vertice(i.vertice2).prede = G.get_vertice(vertice)
                    G.get_vertice(i.vertice2).d = G.get_vertice(vertice).d + 1
                    fila.append(i.vertice2)
    return estado_da_visitados, estado_da_fila
"""
visitados, fila = busca_Largura(grafo, "a")
print("Estado da lista de vertices finalizados em cada interação:")
for i in visitados :
    print(i)

print("Estado da fila de vertices encontrados em cada interação:")
for i in fila:
    print(i)
"""
#print(grafo.get_aresta("h", "i").peso)

def atualizar_lista(G, explorados, prioridade):
    prioridade = []
    for v in G.lista_adjacencia:
        if(v.id not in explorados):
            prioridade.append((v.d, v.id))
    return prioridade

def dijkstra(G, v):
    explorados = []
    estado_explorados = []
    estado_prioridade = []
    for i in G.lista_adjacencia:
        i.d = math.inf
    start = G.get_vertice(v)
    start.d = 0
    prioridade = [(n.d, n.id) for n in G.lista_adjacencia]
    heapq.heapify(prioridade)
    while(True):
        #print(prioridade)
        estado_explorados.append(explorados.copy())
        estado_prioridade.append(prioridade.copy())
        if not prioridade:
            break
        vert = heapq.heappop(prioridade)[1]
        u = G.get_vertice(vert)
        explorados.append(u.id)
        for vi in u.vizinhos:
            dv = G.get_vertice(vi.vertice2).d
            if(G.get_vertice(vi.vertice2).d > (u.d + G.get_aresta(u.id, vi.vertice2).peso)):
                u.visitado = True
                G.get_vertice(vi.vertice2).d = u.d + G.get_aresta(u.id, vi.vertice2).peso
                G.get_vertice(vi.vertice2).prede = u
                prioridade = atualizar_lista(G, explorados, prioridade)
                heapq.heapify(prioridade)
    return estado_explorados,estado_prioridade
#dijkstra(grafo, "a")

print("Resulatdo Busca em Largura:")
visitados, fila = busca_Largura(grafo, "a")
print("Estado da lista de vertices finalizados em cada interação:")
for i in visitados :
    print(i)

print()
print("Estado da fila de vertices encontrados em cada interação:")
for i in fila:
    print(i)

print("Abaixo extão listados os vertice e seus predecessor, e adistancia. Com isso podemos montar um arvore onde o predecessor é pai do vertice")
for v in grafo.lista_adjacencia:
    print(v.id, "predecessor:",v.prede.id," | " ,"distancia: ", v.d)

print()
print("**************************************************************************************************************************")
print()

print("Resulatdo algoritmo de dijkstra:")
visitados, fila = dijkstra(grafo, "a")
print("Estado da lista de vertices finalizados em cada interação:")
for i in visitados :
    print(i)

print()
print("Estado da fila de prioridades de vertices encontrados em cada interação:")
print("inf significa infinito, em cada interação é feito o relaxamento para encontar a menor distancia.")

for i in fila:
    print(i)

print("Abaixo extão listados os vertice e seus predecessor, e adistancia. Com isso podemos montar um arvore onde o predecessor é pai do vertice")
for v in grafo.lista_adjacencia:
    print(v.id, "predecessor:",v.prede.id," | " ,"distancia: ", v.d)