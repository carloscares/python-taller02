# Taller 2 - Problema 3
# 20 puntos
#---------------------------------------------------
#Los algoritmos de grafos son un clásico en ciencias
#de computación, y dentro de estos, aquellos que 
#tienen pesos en las aristas. En este problema se espera que se
#ingrese un conjunto de aristas de la forma [nodo peso nodo]
#y responda cuáles son los vecinos de un nodo dado
#al final en orden alfabético
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
x 7 q
u 2 r
u

salida:
['m', 'r', 'x', 'y']

Ejemplo de entrada 2

u 5 x
q 12 w
w 6 r
s 10 q
r 8 p
u 12 m
y 6 u
x 7 q
u 2 r
s

salida:
['q']


Ejemplo de entrada 3

u 5 x
q 12 w
w 6 r
s 10 q
r 8 p
u 12 m
y 6 u
x 7 q
u 2 r
w


salida:
['q', 'r']
'''''''''''''''''''''

nodo = []
x = input().split()
while(len(x)==3):
	nodo+= [[x[0], int(x[1]), x[2]]]
	x = input().split()
source = x[0]
print("\nnodos\n")
print(nodo)
print(source)