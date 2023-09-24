"""

6) Faça um programa que leia 5 números e informe o maior número

"""

maior_num = float("-inf")

# Leia 5 números
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    
    # Verifique se o número lido é maior do que o maior número atual
    if num > maior_num:
        maior_num = num

# Exiba o maior número
print(f"O maior número é: {maior_num}")
