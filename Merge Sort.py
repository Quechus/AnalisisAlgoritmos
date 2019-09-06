#MergeSort -> Incompleto
from random import randint, uniform,random
def main():
	print ("Merge Sort");	
	# Tamanios del problema
	tamanioProblema = [10, 20, 30, 40, 50, 100, 150 ,200, 250, 300, 350, 400, 450, 500, 1000, 1500, 2000];
	
	for i in range(0, len(tamanioProblema)):
		# numero de operaciones basicas de cada ejecucion
		resultados = [];
		# Se realiza 30 veces la prueba con el tamanio dado y se guarda el numero de op basica
		for j in range(0, 30):
			n = tamanioProblema[i];
			a = llenaLista(n);
			a = mergeSort(a);
			resultados.append(a[1]);
			#print "La operacion basica se ejecuto: ", a[1], "\n";
			#print "Lista Ordenada: ", a[0];

		# Se promedia el resultado de las 30 ejecuciones
		prom = promedio(resultados);
		print ("----------------------------------");
		print ("Tamanio de problema: ", n);
		print ("Promedio: ", prom);

	print ("\nTermine Merge Sort xD");


def mergeSort(lista):
	operacionBa=0;
	tam = len(lista);
	izq = [];
	der = [];
	if(tam <= 1):
		return lista, operacionBa;
	else:
		mitad = tam/2;
		izq = mergeSort(lista[0:mitad]);
		der = mergeSort(lista[mitad:tam]);
		merge = mezcla(izq[0], der[0], lista);
		return merge[0], operacionBa + merge[1];

def mezcla(izq, der, lista):
	operacionB = 3;
	i = 0;
	j = 0;
	k = 0;

	while(i < len(izq) and j < len(der) ):
		operacionB +=1;
		if(izq[i] < der[j]):
			lista[k] = izq[i];
			i = i+1;
		else:
			lista[k] = der[j];
			j = j+1;
		k = k+1;
	#fin while1

	while(i < len(izq) ):
		operacionB +=1;
		lista[k] = izq[i];
		i = i+1;
		k = k+1;
	#fin while2

	while(j < len(der) ):
		operacionB +=1;
		lista[k] = der[j];
		j = j+1;
		k = k+1;
	#fin while3
	return lista, operacionB;

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