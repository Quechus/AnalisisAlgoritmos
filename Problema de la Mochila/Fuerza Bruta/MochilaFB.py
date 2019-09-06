#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import copy

# Lee el archivo anexo al proyecto y le asigna sus beneficios y volumenes
def leerMatriz_costoBeneficio(NombreArchivo):
	matrizMochila = []
	contador = 0
	with open(NombreArchivo, 'r') as f:
		for line in f:
			line = line.strip()
			if len(line) > 0 :
				contador+=1
				matrizMochila.append( [int(n) for n in line.split()] )

		beneficios = []
		volumenes = []
		for i  in range(contador):
			beneficios.append(matrizMochila[i][0]);
			volumenes.append(matrizMochila[i][1]);
	return  beneficios, volumenes
# Fin metodo Leer Archivo

# Metodo Principal
def Mochila_fuerza_bruta():

	NombreArchivo = 'prueba.txt'
	matriz_mochila = leerMatriz_costoBeneficio(NombreArchivo)
	
	beneficios = matriz_mochila[0]
	volumenes = matriz_mochila[1]

	# Ingresar el volumen de la mochila
	VolMochila = 341045
	# Tamaño de las soluciones
	numObjetos = len(volumenes)
	#Numero de soluciones que genera y las iteraciones que hace
	iteraciones = 50
	numero_soluciones = 10 #Grupo de soluciones que se generan en cada iteracion

	print ("\tLos beneficios son: ", beneficios)
	print ("\tLos volumenes son: ", volumenes)
	print ("\tEl volumen de la mochila es: ", VolMochila)
	print ("");

	#Instancia inicial
	mejor_actual = solucionInicial(numObjetos, volumenes, VolMochila)
	fitness_inicial = calcula_fitness(mejor_actual, beneficios)
	vol_inicial = calcula_volumen(mejor_actual, volumenes)

	print ("\tInstancia inicial - Fitness - Volumen")
	print (mejor_actual, fitness_inicial, vol_inicial, "\n")
	print ("");
	mejor_beneficio_actual = calcula_fitness(mejor_actual, beneficios)
	mejor_volumen_actual = calcula_volumen(mejor_actual, volumenes)
	soluciones = []
	
	for j in range(iteraciones):
		#Generas un grupo de n soluciones
		soluciones = generaSoluciones(mejor_actual, volumenes, VolMochila, numero_soluciones)
		mejor_temporal = get_mejor_solucion(soluciones, beneficios, volumenes, VolMochila)
		
		mejor_beneficio_temporal = calcula_fitness(mejor_temporal, beneficios)
		mejor_volumen_temporal = calcula_volumen(mejor_temporal, volumenes)

		if mejor_beneficio_temporal > mejor_beneficio_actual:
			
			if(mejor_volumen_temporal < VolMochila):
				mejor_actual = mejor_temporal
				mejor_beneficio_actual = mejor_beneficio_temporal
				mejor_volumen_actual = mejor_volumen_temporal
		#Vacia el arreglo soluciones para que, en la proxima iteracion, genere otro nuevo grupo de soluciones
		soluciones = []
	print ("Numero de iteraciones = ",iteraciones)
	print ("\tInstancia MEJOR - Fitness - Volumen")
	print (mejor_actual, mejor_beneficio_actual, mejor_volumen_actual)

	print("\nFin de Fuerza Bruta")		
# Fin de Metodo Principal

# Crea una instancia de tamaño n
def solucionInicial(numObjetos, volumenes, VolMochila):
	instancia = []
	volumen = VolMochila
	while( volumen >= VolMochila):
		instancia = []
		for i in range(numObjetos):
			obj = (random.randint(0,10))/10.0;
			instancia.append(obj)
		volumen = calcula_volumen(instancia, volumenes)
	return instancia

# Calcula el fitness de una solucion
def calcula_fitness(instancia, beneficios):
	n = len(instancia)
	j = 0
	beneficio = 0
	while(j < n):
		beneficio = beneficio + beneficios[j]*instancia[j]
		j = j+1
	return beneficio
#Fin calcula fitness

# Calcula el volumen de una solucion
def calcula_volumen(instancia, volumenes):
	vol = 0
	n = len(volumenes)
	for i in range (n):
			vol = vol + volumenes[i]*instancia[i]
	return vol
# Fin calcula volumen

#genera un grupo de soluciones 
def generaSoluciones(instancia, volumenes, VolMochila, nSoluciones):
	n = len(instancia)
	arr = []
	soluciones =[]
	for i in range(nSoluciones):
		#Elige una posicion aleatoria y le cambia su valor, creando una nueva solucion
		r = random.randint(0, n-1)
		if(instancia[r] < 0.9):
			instancia[r] = round(instancia[r] + 0.1, 1)
		else:
			instancia[r] = round(instancia[r] - 0.1, 1)
		#Copias la instancia generada en un arreglo y este lo pasas a las soluciones generadas
		arr = copy.copy(instancia)
		soluciones.append(arr)
	
	return soluciones
	
		
def get_mejor_solucion(soluciones, beneficios, volumenes, VolMochila):
	mejor = soluciones[0]
	fitness = 0
	for i in soluciones:
		fitness_tmp = calcula_fitness(i, beneficios)
		vol_tmp = calcula_volumen(i, volumenes)
		if(fitness_tmp > fitness):
			if(vol_tmp < VolMochila):
				mejor = i
	return mejor
		
Mochila_fuerza_bruta()