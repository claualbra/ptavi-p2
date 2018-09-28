#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

with open('calculadora.txt') as fichero:
	for line in fichero:
		lista_calc= line.split(",")
		op1 = list(map(int, lista_calc[1:]))
		
		
		if lista_calc[0] == "resta":
			resta i in op1:
				a = i+1
				resta = resta - i
				print(i)

			
		
