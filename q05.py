##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##

import itertools as it 
from operator import itemgetter as ig


with open("data.csv", "r") as f:
    data = [_.strip() for _ in f.readlines()]
    data = [_.split("\t") for _ in data]

    row = sorted(data, key=ig(0))
    for key, group in it.groupby(row, ig(0)):
        group = list(group)
        row2 = [_[1] for _ in group]
        print(f"{key},{max(row2)},{min(row2)}")
