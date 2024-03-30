handle = open("estructuras-datos/texto2.txt")
counts = dict()
max = 0
name = ""

for line in handle:
    if not line.startswith("From "):
        continue
    tempList = line.split()
    counts[tempList[1]] = counts.get(tempList[1], 0) + 1

for keys, value in counts.items():
    if value >= max:
        max = value
        name = keys
        
print(name, max)