# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


#  Реализация aaaaabbbcccc -> 5a3b4c
with open('file.txt', 'r') as data:
    literal_exp = data.read()
data.close()
print(literal_exp)
count = 1
polynominal = ''
for i in range(1, len(literal_exp)):
    if literal_exp[i] == literal_exp[i - 1]:
        count += 1
    else:
        polynominal += f"{count}{literal_exp[i - 1]}"
        count = 1
polynominal += f"{count}{literal_exp[i]}"
data = open('total.txt', 'w')
data.writelines(polynominal)
data.close()

# Реализация 5a3b4c -> aaaaabbbcccc
with open('total.txt', 'r') as data:
    polynominal_exp = data.read()
data.close()
print(polynominal_exp)
count = 0
expression = ''
i = 0
for i in range(len(polynominal_exp)):
    if polynominal_exp[i].isdigit():
        count = count * 10 + int(polynominal_exp[i])
    else:
        expression += count * polynominal_exp[i]
        count = 0
print(expression)
