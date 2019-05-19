##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

import itertools as it 
from operator import itemgetter as ig

with open("data.csv", "r") as f:
    data = [_.strip() for _ in f.readlines()]
    data = [_.split("\t") for _ in data]

    fechas = sorted([_[2].split("-") for _ in data], key=ig(1))

    for key, group in it.groupby(fechas, ig(1)):
        print(f"{key},{len( list( group ) )}")