# Taller 2 - Problema 5
# 20 puntos
#---------------------------------------------------
#Los algoritmos de grafos son un clásico en ciencias
#de computación, y dentro de estos, aquellos que 
#tienen pesos en las aristas. En este problema se espera que se
#ingrese un conjunto de aristas de la forma [nodo peso nodo]
#y responda el camino más corto entre dos nodos. El 
#camino más corto debe ser reportado como tupla y
#se sugiere que use el algoritmo de Dijkstra explicado en
# https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/
#
#----------------------------------------------------
#Ejemplo de entrada 1
''''''''''''''''''''''

u 5 x
q 12 w
w 6 r
s 10 q
x 2 s
r 8 p
m 3 y
u 12 m
y 6 u
s r

salida:
('s', 'x', 'u', 'r')
9


'''''''''''''''''''''''

nodo = []
x = input().split()
while(len(x)==3):
	nodo+= [[x[0], int(x[1]), x[2]]]
	x = input().split()
source = x[0]
target = x[1]
print("\nnodos\n")
print(nodo)
print("camino entre "+source+" hasta "+target)