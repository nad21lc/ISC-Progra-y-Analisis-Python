#Leo elementos de un archivo de texto y elimino los repetidos

fh = open("estructuras-datos/texto.txt")
lst = fh.read().lstrip()
lst = lst.split()
lst.sort()

print(range(len(lst)))
for i in range(len(lst)):
    try:
        if lst[i] == lst[i+1]:
            lst.pop(i)
    except:
        break

print(lst)

