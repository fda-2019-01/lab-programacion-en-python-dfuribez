##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##

import itertools as it 
from operator import itemgetter as ig 

with open("data.csv", "r") as f:
    data = [_.strip() for _ in f.readlines()]
    data = [_.split("\t") for _ in data]

    for item in data:
        r0 = item[0]
        r3 = item[3].split(",")
        r4 = item[4].split(",")

        print(f"{r0},{len(r3)},{len(r4)}")