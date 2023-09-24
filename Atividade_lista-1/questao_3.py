"""

3) Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

lista_n = [num1, num2, num3]

lista_n.sort(reverse=True)

print("Números em ordem decrescente:", lista_n)