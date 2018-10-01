#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def mult(op1, op2):
        """ Function to multiply the operands. Ops have to be ints """
        return op1 * op2

    def div(op1, op2):
        """ Function to split the operands """
        return op1 / op2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = CalculadoraHija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = CalculadoraHija.minus(operando1, operando2)
    elif sys.argv[2] == "divide":
        try:
            result = CalculadoraHija.div(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
    elif sys.argv[2] == "multiplica":
        result = CalculadoraHija.mult(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
