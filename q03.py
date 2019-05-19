##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

import itertools as it
from operator import itemgetter as ig

with open("data.csv", "r") as f:
    data = f.readlines()
    data = [_.strip() for _ in data]

    lines = [_.split("\t") for _ in data]
    # print(lines[0])

    for key, group in it.groupby(sorted( lines, key=ig(0) ), ig(0)):
        suma = 0
        suma += sum( int(_[1]) for _ in group)
        print(f"{key},{suma}")