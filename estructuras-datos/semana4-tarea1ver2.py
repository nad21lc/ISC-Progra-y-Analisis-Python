#Leo elementos de un archivo de texto, elimino los repetidos y ordeno

fh = open("estructuras-datos/texto.txt")
tempList = fh.read().split()

myList = list()

for element in tempList:
    if element not in myList:
        myList.append(element)
    
myList.sort()
print(myList)