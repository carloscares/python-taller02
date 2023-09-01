# Taller 2 - Problema 4
# 20 puntos
#---------------------------------------------------
#Los algoritmos de grafos son un clásico en ciencias
#de computación. Un clásico son los grafos con peso
#en las aristas. En este problema se espera que se
#ingrese un conjunto de aristas de la forma [nodo peso nodo]
#y responda si dado dos nodos en el grafo hay o no
#un camino entre ellos
#----------------------------------------------------
#Ejemplo de entrada 1
''''''''''''''''''''''

u 5 x
q 12 w
w 6 r
s 10 q
r 8 p
u 12 m
y 6 u
x q

salida:
no

Ejemplo de entrada 2

u 5 x
q 12 w
w 6 r
s 10 q
r 8 p
u 12 m
y 6 u
s p

salida:
si
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