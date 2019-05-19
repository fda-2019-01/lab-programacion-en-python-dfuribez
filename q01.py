##
## Imprima la suma de la segunda columna.
##

FILE = "data.csv"

suma = 0

with open(FILE, "r") as f:
    for line in f.readlines():
        suma += int(line.split("\t")[1])

print(suma)