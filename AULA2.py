# num1 = int(input("Insira um número inteiro: "))
# num2 = int(input("Insira um número inteiro: "))
#
# # print(num1+num2)
# d = True
# print(type(d))
#
# nome = "Pietro"
# print(type(nome))

# print
# (10**3)print(10//3)


nota = 8
media = 7
aprovado = nota>=media
print(aprovado)

# # Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
# num1 = int(input("Insira um número inteiro: "))
# num2 = int(input("Insira um número inteiro: "))
# print(num1+num2)

# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
valorMetro = float(input("Insira um valor em metros: "))
valorMetro = valorMetro * 1000
print("Seu valor em milímetros é igual a: ",valorMetro)

# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total
# em segundos.
dia = int(input("Insira uma quantidade de dias: "))
horas = int(input("Insira uma quantidade de horas: "))
minutos = int(input("Insira uma quantidade de minutos: "))
segundos = int(input("Insira uma quantidade de segundos: "))

dia = dia * 86400
horas = horas * 3600
minutos = minutos * 60
print (dia+horas+minutos+segundos)