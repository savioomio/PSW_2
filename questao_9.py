"""

9) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

"""

vt = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número real: "))
    vt.append(num) 

print("Números na ordem inversa:")
for num in reversed(vt):
    print(num)
