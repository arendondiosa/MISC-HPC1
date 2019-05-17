import threading
import random
import time
import sys

resultado=[]  #matriz global del resultado
def CalculadorMatriz(Matriz1, Matriz2, Contador, Tamano_Matriz):  #Me llega la matriz1 la matriz 2 y el contador que es el numero de la fila que se esta ejecutando en la linea 93
	i=0
	Fila = []
	Acumulador = 0
	while(i < Tamano_Matriz):
		j=0
		Acumulador = 0
		while(j < Tamano_Matriz):
			Acumulador = Acumulador + (Matriz1[Contador][j] * Matriz2[j][i])
			j = j+1
		Fila.append(Acumulador)
		i = i+1

	resultado.append(Fila)


if __name__ == '__main__':
	Matriz1 = []
	Matriz2 = []
	Matriz_Resultante = []

	filename, Tamano_Matriz = sys.argv 
	Tamano_Matriz = int(Tamano_Matriz)
	#De la linea 73 a la linea 84 hace exactamente lo mismo que de las 12 a la 23 no hay diferencias
	for i in range(Tamano_Matriz):
		Matriz1.append([0]*Tamano_Matriz)

	for i in range(0, Tamano_Matriz):
		for j in range(0, Tamano_Matriz):
			numero = random.randrange(0,10)
			Matriz1[i][j] = numero

	for i in range(Tamano_Matriz):
		Matriz2.append([0]*Tamano_Matriz)

	for i in range(0, Tamano_Matriz):
		for j in range(0, Tamano_Matriz):
			numero = random.randrange(0,10)
			Matriz2[i][j] = numero

	# print(Matriz1)
	# print(Matriz2)

for i in range(int(test_iterations)):
	Inicio = time.time()

	for i in range(len(Matriz1)): #va a multiplicar de fila en fila de la matriz1 a las columnas de la matriz2
		Resultado1 = threading.Thread(target=CalculadorMatriz, args=([Matriz1, Matriz2, i, Tamano_Matriz])) #Me guarda las operaciones que me hace los hilos fila por fila de matriz1
		Matriz_Resultante.append(Resultado1) #me guarda cada fila resultante en la matriz final

	for i in Matriz_Resultante:  #Despues de calcularse todas las filas se van a recorrer y se comenzaran la ejecucion de los hilos creados al mismo tiempo
		i.start()

	for i in Matriz_Resultante:  #Me permitira que no haya problemas de ejecucion de los hilos
		i.join()


	Final = time.time()
	Tiempo = Final-Inicio
	total_time += Tiempo

	# print(Matriz_Resultante)
	print(Tiempo)
