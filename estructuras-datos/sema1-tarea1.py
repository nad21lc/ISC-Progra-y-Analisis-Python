
text = "X-DSPAM-Confidence:    0.8475"
extract = text.find("0")
number = float(text[extract:])
print(number)

#Slicing Strings
# print(s[0:4]) - Desde 0 hasta 4 - 1
# print(s[:7]) - Desde inicio hasta 7 - 1
# print(s[7:]) - Desde 7 hasta el fin
# print(s[:]) - todo

#Uso de "IN"
# fruits = "banana"
# "n" in fruit
# outpud: True

#Stripping Whitespace
# cadena.lstrip() = quita espacios blanco al inicio
# cadena.rstrip() = quita los espacios blancos al final
# cadena.strip() = quita tanto a la derecha como izquierda