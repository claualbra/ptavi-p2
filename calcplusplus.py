#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

class Calculadora():
	def plus(lista_int):
		""" Function to sum the operands. Ops have to be ints """
		return sum(lista_int)

	def minus(lista_int):
		""" Function to substract the operands """
		resta = lista_int[0]
		for i in lista_int[1:]:
			resta -= i
		return resta

class CalculadoraHija(Calculadora):
	def mult(lista_int):
		""" Function to multiply the operands. Ops have to be ints """
		multiplicacion = 1
		for i in lista_int:
			multiplicacion *= i
		return multiplicacion

	def div(lista_int):
		""" Function to split the operands """
		division = lista_int[0]
		for i in lista_int[1:]:
			division /= i
		return division


if __name__ == "__main__":
	with open(sys.argv[1]) as csvarchivo:
		fichero = csv.reader(csvarchivo)
		for line in fichero:
			lista_calc = line
			lista_int = list(map(int, line[1:]))

			if lista_calc[0] == "suma":
				result = CalculadoraHija.plus(lista_int)
			elif lista_calc[0] == "resta":
				result = CalculadoraHija.minus(lista_int)
			elif lista_calc[0] == "multiplica":
				result = CalculadoraHija.mult(lista_int)
			elif lista_calc[0] == "divide":
				try:
					result = CalculadoraHija.div(lista_int)
				except ZeroDivisionError:
					result = "Division by zero is not allowed"
			else:
				result = 'Operación sólo puede ser sumar o restar.'
		
			print(result)
