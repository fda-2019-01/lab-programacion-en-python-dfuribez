##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##

import re

EXPRESION = ":(.?\d*)"

with open("data.csv", "r") as f:
    data = [_.strip() for _ in f.readlines()]
    data = [_.split("\t") for _ in data]

    r04 = [[_[0], _[4]] for _ in data]

    for r0, r1 in r04:
        suma = sum( map( int,  re.findall(EXPRESION, r1)) )
        print(f"{r0},{suma}")