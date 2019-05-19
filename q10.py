##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##

import itertools as it 
from operator import itemgetter as ig 

with open("data.csv", "r") as f:
    data = [_.strip() for _ in f.readlines()]
    data = [_.split("\t") for _ in data]

    row4 = [_[4].split(",") for _ in data]
    row4_flat = list(it.chain(*row4))

    row4 = sorted([_.split(":") for _ in row4_flat], key=ig(0))

    for key, group in it.groupby(row4, ig(0)):
        print(f"{key},{len(list(group))}")