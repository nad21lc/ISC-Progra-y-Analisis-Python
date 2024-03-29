# Use the file name mbox-short.txt as the file name
fh = open("estructuras-datos/texto.txt")
cont = 0
number = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        line = line.rstrip()
        cont += 1
        number += float(line[19:])
        print(number)
    
print("Average spam confidence:", number/cont)
