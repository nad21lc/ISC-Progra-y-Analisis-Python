handle = open("estructuras-datos/texto2.txt")

tempList = list()
counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    tempList = line[5].split(":")
    counts[tempList[0]] = counts.get(tempList[0], 0) + 1
    
tempList.clear()

for key,value in counts.items():
    tempList.append((key, value))

tempList = sorted(tempList)

for v, k in tempList:
    print(v, k)
