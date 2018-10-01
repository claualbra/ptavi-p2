#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv


if __name__ == "__main__":
    micalc = calcoohija.CalculadoraHija
    with open(sys.argv[1]) as csvarchivo:
        fichero = csv.reader(csvarchivo)
        operaciones = {"suma": micalc.plus,
                       "resta": micalc.minus,
                       "multiplica": micalc.mult,
                       "divide": micalc.div}
        for line in fichero:
            try:
                lista_calc = line
                lista_int = list(map(int, line[1:]))

                op1 = lista_int[0]
                for op2 in lista_int[1:]:
                    try:
                        if op2 == 0 and lista_calc[0] == "divide":
                            result = "Division by zero is not allowed"
                            break
                        else:
                            op1 = operaciones[lista_calc[0]](op1, op2)
                            result = op1
                    except KeyError:
                        result = "Sólo puede ser suma,resta,mult. o divide."
            except ValueError:
                result = "Error: Non numerical parameters"

            print(result)
