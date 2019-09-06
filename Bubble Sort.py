#BubbleSort -> Incompleto
from random import randint, uniform,random

def main():
	print "Bubble Sort";	
	# Tamanios del problema
	tamanioProblema = [10, 20, 30, 40, 50, 100, 150 ,200, 250, 300, 350, 400, 450, 500, 1000, 1500, 2000];
	
	for i in range(0, len(tamanioProblema)):
		# numero de operaciones basicas de cada ejecucion
		resultados = [];
		# Se realiza 30 veces la prueba con el tamanio dado y se guarda el numero de op basica
		for j in range(0, 30):
			n = tamanioProblema[i];
			a = llenaLista(n);
			a = bubbleSort(a);
			resultados.append(a[1]);
			#print "La operacion basica se ejecuto: ", a[1], "\n";
			#print "Lista Ordenada: ", a[0];

		# Se promedia el resultado de las 30 ejecuciones
		prom = promedio(resultados);
		print "----------------------------------";
		print "Tamanio de problema: ", n;
		print "Promedio: ", prom;

	print "\nTermine Buuble Sort xD";

def bubbleSort(lista):
	cont = 0;
	tam = len(lista);
	for i in range (0, tam):
		for j in range (0, tam-1):
			if(lista[j+1] < lista[j]):
				temp = lista[j];
				lista[j] = lista[j+1];
				lista[j+1] = temp;
				cont = cont + 3;
	return lista, cont;
#Otros Metodos

def llenaLista(tam):
	lista = [];
	for i in range (0, tam):
		dato = randint(1,9999);
		if(dato not in lista):
			lista.append(dato);
	return lista;

def promedio(opBasicas):
	tam = len(opBasicas);
	suma=0;
	for i in range (0, tam):
		suma = suma + opBasicas[i];
	return suma / tam;

main();