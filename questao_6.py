"""

6) Faça um programa que leia 5 números e informe o maior número

"""

maior_num = float("-inf")

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    
    if num > maior_num:
        maior_num = num

print(f"O maior número é: {maior_num}")
