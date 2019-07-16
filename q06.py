##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5

buffer = dict()

with open("data.csv", "r") as f:
    q = [line.split()[4] for line in f.readlines()]
    for i in q:
        splitted = i.split(",")
        for j in splitted:
            key, value = j.split(":")

            if key in buffer:
                buffer[key].append(int(value))
            else:
                buffer[key] = [int(value)]

for i in sorted(buffer):
    print(f"{i},{min(buffer[i])},{max(buffer[i])}")

