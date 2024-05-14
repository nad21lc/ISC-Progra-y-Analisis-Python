#Imprima la suma de todos los digitos encontrados en el archivo de text

import re

txt = open("regex_sum_1999164.txt")

numbers = []
sum = 0

for line in txt:
    line = line.rstrip()
    number = re.findall(r"[0-9]+", line)
    
    for n in number:
        if n.isdigit():
            numbers.append(int(n))


for number in numbers:
    sum += number

print(sum)