import random
import time

Fila = []
Matriz1 = []
Matriz2 = []
Matriz_Resultante = []

Tamano_Matriz = int(input("Tamano de la matrizes cuadradas: "))

for i in range(Tamano_Matriz):  #Este for me iniciara la matriz1 con ceros sin importar el tamano que tenga la matriz
	Matriz1.append([0]*Tamano_Matriz)

for i in range(0, Tamano_Matriz):  #Estas sentencias for me llenaran la matriz1 con los valores random de 0 a 10 que se especifica en la linea 17
	for j in range(0, Tamano_Matriz):
		numero = random.randrange(0,10)
		Matriz1[i][j] = numero

for i in range(Tamano_Matriz):  #Este for me iniciara la matriz2 con ceros sin importar el tamano que tenga la matriz
	Matriz2.append([0]*Tamano_Matriz)

for i in range(0, Tamano_Matriz):  #Estas sentencias for me llenaran la matriz2 con los valores random de 0 a 10 que se especifica en la linea 25
	for j in range(0, Tamano_Matriz):
		numero = random.randrange(0,10)
		Matriz2[i][j] = numero

print(Matriz1)
print(Matriz2)
#De aqui en adelante se calculara secuencialmente la multiplicacion de la matriz1 por la matriz2
k=0
while(k < Tamano_Matriz):
	i=0
	while(i < Tamano_Matriz):
		j=0
		Acumulador = 0
		while(j < Tamano_Matriz):
			Acumulador = Acumulador + (Matriz1[k][j] * Matriz2[j][i])
			j = j+1
		Fila.append(Acumulador)
		i = i+1
	Matriz_Resultante.append(Fila)
	Fila = []
	k = k+1

print(Matriz_Resultante)
