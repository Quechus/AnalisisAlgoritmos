#QuickSort -> Terminado
from random import randint, uniform,random

def main():
	print "Quick Sort";	
	# Tamanios del problema
	tamanioProblema = [10, 20, 30, 40, 50, 100, 150 ,200, 250, 300, 350, 400, 450, 500, 1000, 1500, 2000];
	
	for i in range(0, len(tamanioProblema)):
		# numero de operaciones basicas de cada ejecucion
		resultados = [];
		# Se realiza 30 veces la prueba con el tamanio dado y se guarda el numero de op basica
		for j in range(0, 30):
			n = tamanioProblema[i];
			a = llenaLista(n);
			a = quickSort(a);
			resultados.append(a[1]);
			#print "La operacion basica se ejecuto: ", a[1], "\n";
			#print "Lista Ordenada: ", a[0];

		# Se promedia el resultado de las 30 ejecuciones
		prom = promedio(resultados);
		print "----------------------------------";
		print "Tamanio de problema: ", n;
		print "Promedio: ", prom;

	print "\nTermine Quick Sort xD";

def quickSort(lista):
	operacionB=0;
	n = len(lista);
	if(n < 1):
		return lista, operacionB;
	centro = n / 2;
	pivote = lista[centro];
	piv =[pivote];
	lista.pop(centro);
	menores = [];
	mayores = [];

	for i in range(0, (n-1)):
		operacionB+=1;
		if(lista[i] < pivote):
			a=lista[i];
			menores.append(a);
		else:
			a=lista[i];
			mayores.append(a);
			
	resultadoMenores = quickSort(menores);
	resultadoMayores = quickSort(mayores);
	operacionB = operacionB + resultadoMenores[1] + resultadoMayores[1];

	return resultadoMenores[0] + piv + resultadoMayores[0], operacionB;

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