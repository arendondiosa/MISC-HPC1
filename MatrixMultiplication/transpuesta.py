import random
import time
import sys

def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

Fila = []
Matriz1 = []
Matriz2 = []
Matriz2T = []
Matriz_Resultante = []

filename, Tamano_Matriz, test_iterations = sys.argv 
Tamano_Matriz = int(Tamano_Matriz)

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

#Matriz1=[[6, 1], [1, 4]]
#Matriz2=[[3, 7], [9, 2]] 

#print(Matriz1)
#print(Matriz2)
#print("hola")
Matriz2=trans(Matriz2)
#print(Matriz2)

#print("hola")
#De aqui en adelante se calculara secuencialmente la multiplicacion de la matriz1 por la matriz2

total_time = 0

for i in range(int(test_iterations)):
	Inicio = time.time()
	k=0
	while(k < Tamano_Matriz):
		i=0
		while(i < Tamano_Matriz):
			j=0
			Acumulador = 0
			while(j < Tamano_Matriz):
				Acumulador = Acumulador + (Matriz1[k][j] * Matriz2[i][j])
				#Acumulador = Acumulador + (Matriz1[k][j] * Matriz2[j][i])
				j = j+1
			Fila.append(Acumulador)
			i = i+1
		Matriz_Resultante.append(Fila)
		Fila = []
		k = k+1

	Final = time.time()
	Tiempo = Final-Inicio
	total_time += Tiempo

	#print(Matriz_Resultante)
#print(Matriz_Resultante)
	# print(Tiempo)
print(total_time / int(test_iterations))