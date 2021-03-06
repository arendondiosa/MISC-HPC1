from multiprocessing import Process, Lock, Array
import random
import time
import sys

def CalculadorMatriz(Matriz1, Matriz2, Contador, Tamano_Matriz, resultado, lock):  #Me llega la matriz1 la matriz 2 y el contador que es el numero de la fila que se esta ejecutando en la linea 93
	i=0
	Fila = []
	Acumulador = 0
	while(i < Tamano_Matriz):
		j=0
		Acumulador = 0
		while(j < Tamano_Matriz):
			Acumulador = Acumulador + (Matriz1[Contador][j] * Matriz2[j][i])
			j = j+1
		lock.acquire()
		resultado[Tamano_Matriz*Contador+i]=Acumulador
		lock.release()

		i = i+1

	
if __name__ == '__main__':
	Matriz1 = []
	Matriz2 = []
	Matriz_Resultante = []
	resultado=[]  #matriz global del resultado
	procesos=[]
	filename, Tamano_Matriz, test_iterations = sys.argv 
	Tamano_Matriz = int(Tamano_Matriz)	
	
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

	resultado=list(range(Tamano_Matriz*Tamano_Matriz))
	resultado=Array("i", resultado)
	# print(Matriz1)
	# print(Matriz2)

	total_time = 0

	for i in range(int(test_iterations)):
		Inicio = time.time()

		for i in range(Tamano_Matriz):
			proceso=Process(target=CalculadorMatriz, args=([Matriz1, Matriz2, i, Tamano_Matriz, resultado, Lock()]))
			proceso.start()
			procesos.append(proceso)

		for i in procesos:
			i.join()
		

		Final = time.time()
		Tiempo = Final-Inicio
		total_time += Tiempo

		# print(Matriz_Resultante)
		# print(Tiempo)
	print(total_time / int(test_iterations))



