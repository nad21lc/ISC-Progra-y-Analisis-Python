# Use words.txt as the file name
file = open("estructuras-datos/texto.txt")

text = file.read().rstrip()
print(text.upper())

#imprima en mayus y corte las lineas en blanco