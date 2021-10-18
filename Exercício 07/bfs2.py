#BFS - Algoritmo para Busca em Largura
 
#importa a biblioteca para poder criar uma lista
from collections import defaultdict 
 
#classe para criação do grafo direcionado e que usa representação de lista de adjacência
class Graph: 
 
    #constroi a função que ira criar a lista 
   def __init__(self): 
 
        #Quando você cria um defaultdict, fornece uma função usada para criar valores, nesse caso criou-se a lista
        self.graph = defaultdict(list) 
 
    #função que adiciona os vértices no grafo
   def addEdge(self,u,v): 
        self.graph[u].append(v) 
 
    #função para imprimir a BFS do grafo, recebe o primeiro nó a ser visitado 
   def BFS(self, s): 
      visited = [False] * (len(self.graph)) 
      queue = [] 
      queue.append(s) 
      visited[s] = True
      while queue: 
         s = queue.pop(0) 
         print(s, " ") 
         for i in self.graph[s]: 
            #print(visited[i])
            if visited[i] == False: 
               queue.append(i) 
               visited[i] = True
 
# Criação do grafo
g = Graph() 
g.addEdge(1, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 5) 
g.addEdge(2, 6)
g.addEdge(3, 4) 
g.addEdge(5, 6)
g.addEdge(5, 7)  
g.addEdge(6, 7)
g.addEdge(6, 8)   
g.addEdge(7, 8) 
 
 
print ("Segue a execução do BFS, começando pelo vértice 1")
g.BFS(1) 
 
# Este código é contribuição de: Neelam Yadav