#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
	def plus(op1):
		""" Function to sum the operands. Ops have to be ints """
		return sum(op1)

	def minus(op1):
		""" Function to substract the operands """
		resta = op1[0]
		for i in op1[1:]:
			resta -= i
		return resta

class CalculadoraHija(Calculadora):
	def mult(op1):
		""" Function to multiply the operands. Ops have to be ints """
		multiplicacion = 1
		for i in op1:
			multiplicacion *= i
		return multiplicacion

	def div(op1):
		""" Function to split the operands """
		division = op1[0]
		for i in op1[1:]:
			division /= i
		return division



with open('calculadora.txt') as fichero:
	for line in fichero:
		lista_calc= line.split(",")
		op1 = list(map(int, lista_calc[1:]))

		if lista_calc[0] == "suma":
			result = CalculadoraHija.plus(op1)
		elif lista_calc[0] == "resta":
			result = CalculadoraHija.minus(op1)
		elif lista_calc[0] == "multiplica":
			result = CalculadoraHija.mult(op1)
		elif lista_calc[0] == "divide":
			try:
				result = CalculadoraHija.div(op1)
			except ZeroDivisionError:
				sys.exit("Division by zero is not allowed")
		else:
			sys.exit('Operación sólo puede ser sumar o restar.')
		
		print(result)
