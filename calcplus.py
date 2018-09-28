#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
	def plus(op1):
		""" Function to sum the operands. Ops have to be ints """
		return sum(op1)

	def minus(op1):
		""" Function to substract the operands """
		resta = 0
		for i in op1:
			resta -= i
		return resta


with open('calculadora.txt') as fichero:
	for line in fichero:
		lista_calc= line.split(",")
		op1 = list(map(int, lista_calc[1:]))

		if lista_calc[0] == "suma":
			result = Calculadora.plus(op1)
		elif lista_calc[0] == "resta":
			result = Calculadora.minus(op1)
		else:
			sys.exit('Operación sólo puede ser sumar o restar.')
		
		print(result)
