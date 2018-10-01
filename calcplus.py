#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == "__main__":
    micalc = calcoohija.CalculadoraHija
    fd = open(sys.argv[1], mode='r', encoding='utf-8')
    for line in fd.readlines():
        try:
            lista_calc = line.split(",")
            lista_int = list(map(int, lista_calc[1:]))

            if lista_calc[0] == "suma":
                suma = 0
                for op2 in lista_int:
                    suma = micalc.plus(suma, op2)
                result = suma
            elif lista_calc[0] == "resta":
                resta = lista_int[0]
                for op2 in lista_int[1:]:
                    resta = micalc.minus(resta, op2)
                result = resta
            elif lista_calc[0] == "multiplica":
                multiplicacion = 1
                for op2 in lista_int:
                    multiplicacion = micalc.mult(multiplicacion, op2)
                result = multiplicacion
            elif lista_calc[0] == "divide":
                division = lista_int[0]
                try:
                    for op2 in lista_int[1:]:
                        division = micalc.div(division, op2)
                    result = division
                except ZeroDivisionError:
                    result = "Division by zero is not allowed"
            else:
                result = 'Op. sólo puede ser suma, resta, multiplica o divide.'
        except ValueError:
            result = "Error: Non numerical parameters"

        print(result)
