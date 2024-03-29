#Leo elementos de una lista, elimina los repetidos y ordena

fh = open("estructuras-datos/texto.txt")
tempList = fh.read().split()

myList = list()

for element in tempList:
    if element not in myList:
        myList.append(element)
    
myList.sort()
print(myList)