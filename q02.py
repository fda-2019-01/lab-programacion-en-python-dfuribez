##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

FILE = "data.csv"

letras = []

with open(FILE, "r") as f:
    for line in f.readlines():
        letras.append(line.split("\t")[0])

for letra in sorted(set(letras)):
    print("{0},{1}".format(letra, letras.count(letra)))
