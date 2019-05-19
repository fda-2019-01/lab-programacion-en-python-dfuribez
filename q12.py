##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##

import itertools as it 
from operator import itemgetter

with open("data.csv", "r") as f:
    data = [_.strip() for _ in f.readlines()]
    data = [_.split("\t") for _ in data]

    r13 = [[_[1],  _[3].split(",")] for _ in data]
    letras = sorted(set(it.chain(*[_[1] for _ in r13])))

    for letra in letras:
        suma = sum([int(_[0]) for _ in r13 if letra in _[1]])
        print(f"{letra},{suma}")