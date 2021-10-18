import heapq
import math
from UnionFind import UnionFind 


class Vertice:
    def __init__(self, no) :
        self.d = math.inf
        self.id = no
        self.vizinhos = []
        self.num_vizinhos = 0
        self.prede = self
        self.visitado = False
        self.encontrado = False

    def add_vizinhos(self, vertice, peso = 0):
        self.num_vizinhos = self.num_vizinhos + 1
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

    def add_vertice(self, vertice):
        self.lista_adjacencia.append(Vertice(vertice))

    def get_vertice(self, vertice):
        for i in self.lista_adjacencia:
            if(i.get_id() == vertice):
                return i
        return None

    def add_aresta(self, vertice_v, vertice_u, peso=0):
        self.get_vertice(vertice_v).add_vizinhos(vertice_u, peso)
        self.get_vertice(vertice_v).add_vizinhos(vertice_u, peso)

    def add_aresta_orientada(self, Vertice_origem, vertice_destino, peso = 0):
        self.get_vertice(Vertice_origem).add_vizinhos(vertice_destino, peso)

    def get_aresta(self, vertice_v, vertice_u):
        return self.get_vertice(vertice_v).get_vizinho(vertice_u)

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

def busca_Profundaidade(G, v):
    G.get_vertice(v).d = 0
    G.get_vertice(v).prede = Vertice("Nulo")
    finalizados , encontrados = [], [v]
    while True:
        if not encontrados:
            break
        vertice = encontrados.pop()
        #print(G.get_vertice(vertice).id)
        print()
        for i in G.get_vertice(vertice).vizinhos:
            if i.vertice2 not in encontrados and i.vertice2 not in finalizados:
                encontrados.append(i.vertice2)
        finalizados.append(vertice)
    return finalizados 

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
"""
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
"""
digrafo = Grafo()
digrafo.add_vertice("a")
digrafo.add_vertice("b")
digrafo.add_vertice("c")
digrafo.add_vertice("d")
digrafo.add_vertice("e")
digrafo.add_vertice("f")
digrafo.add_vertice("g")
digrafo.add_vertice("h")
digrafo.add_vertice("i")
digrafo.add_vertice("j")
digrafo.add_vertice("k")
digrafo.add_vertice("l")

digrafo.add_aresta_orientada("a","b")
digrafo.add_aresta_orientada("a","d")
digrafo.add_aresta_orientada("a","e")
digrafo.add_aresta_orientada("a","h")
digrafo.add_aresta_orientada("b","e")
digrafo.add_aresta_orientada("c","i")
digrafo.add_aresta_orientada("d","f")
digrafo.add_aresta_orientada("d","l")
digrafo.add_aresta_orientada("e","b")
digrafo.add_aresta_orientada("e","k")
digrafo.add_aresta_orientada("e","i")
digrafo.add_aresta_orientada("f","h")
digrafo.add_aresta_orientada("g","h")
digrafo.add_aresta_orientada("g","j")
digrafo.add_aresta_orientada("h","l")
digrafo.add_aresta_orientada("j","a")
digrafo.add_aresta_orientada("j","f")
digrafo.add_aresta_orientada("k","e")
digrafo.add_aresta_orientada("l","d")
digrafo.add_aresta_orientada("l","k")

digrafo_T = Grafo()
digrafo_T.add_vertice("a")
digrafo_T.add_vertice("b")
digrafo_T.add_vertice("c")
digrafo_T.add_vertice("d")
digrafo_T.add_vertice("e")
digrafo_T.add_vertice("f")
digrafo_T.add_vertice("g")
digrafo_T.add_vertice("h")
digrafo_T.add_vertice("i")
digrafo_T.add_vertice("j")
digrafo_T.add_vertice("k")
digrafo_T.add_vertice("l")

digrafo_T.add_aresta_orientada("b","a")
digrafo_T.add_aresta_orientada("d","a")
digrafo_T.add_aresta_orientada("e","a")
digrafo_T.add_aresta_orientada("h","a")
digrafo_T.add_aresta_orientada("e","b")
digrafo_T.add_aresta_orientada("i","c")
digrafo_T.add_aresta_orientada("f","d")
digrafo_T.add_aresta_orientada("l","d")
digrafo_T.add_aresta_orientada("b","e")
digrafo_T.add_aresta_orientada("k","e")
digrafo_T.add_aresta_orientada("i","e")
digrafo_T.add_aresta_orientada("h","f")
digrafo_T.add_aresta_orientada("h","g")
digrafo_T.add_aresta_orientada("j","g")
digrafo_T.add_aresta_orientada("l","h")
digrafo_T.add_aresta_orientada("a","j")
digrafo_T.add_aresta_orientada("f","j")
digrafo_T.add_aresta_orientada("e","k")
digrafo_T.add_aresta_orientada("d","l")
digrafo_T.add_aresta_orientada("k", "l")

def bf(G, v):
    for i in G.lista_adjacencia:
        i.encontrado = False
    p = []
    encontrado = [v]
    finalizado = []
    p.append((v, 0))
    G.get_vertice(v).encontrado = True
    while(True):
        if not p:
            break
        #print(p)
        u, i = p.pop()
        if u not in finalizado:
            finalizado.append(u)
        visinhos = G.get_vertice(u).vizinhos
        if G.get_vertice(u).num_vizinhos >= i+1:
            p.append((u, i+1))
            visinho = visinhos[i].vertice2
            if G.get_vertice(visinho).encontrado == False:
                G.get_vertice(visinho).encontrado = True
                encontrado.append(visinho)
                G.get_vertice(visinho).prede = G.get_vertice(u)
                p.append((visinho, 0))
    return encontrado


def compomentes_conexas(G):
    S = UnionFind()
    for v in G.lista_adjacencia:
        S.add(v.id)
    for v in G.lista_adjacencia:
        for u in G.lista_adjacencia:
            if(u.id != v.id):
                lu = bf(G, u.id)
                lv = bf(G, v.id)
                if(lu[0] in lv and lv[0] in lu and not S.connected(v.id, u.id)):
                    S.union(v.id, u.id)
    return S.components()
componentes = compomentes_conexas(digrafo)

print(componentes)