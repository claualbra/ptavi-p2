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

            op1 = lista_int[0]
            for op2 in lista_int[1:]:
                if lista_calc[0] == "suma":
                    op1 = micalc.plus(op1, op2)
                    result = op1
                elif lista_calc[0] == "resta":
                    op1 = micalc.minus(op1, op2)
                    result = op1
                elif lista_calc[0] == "multiplica":
                    op1 = micalc.mult(op1, op2)
                    result = op1
                elif lista_calc[0] == "divide":
                    if op2 == 0:
                        result = "Division by zero is not allowed"
                        break
                    else:
                        op1 = micalc.div(op1, op2)
                        result = op1
                else:
                    result = 'Op. sólo puede ser suma,resta,mult. o divide.'
        except ValueError:
            result = "Error: Non numerical parameters"

        print(result)
    fd.close()
