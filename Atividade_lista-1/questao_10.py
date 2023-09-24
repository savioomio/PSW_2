"""

10) Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça: 
    a. Mostre a quantidade de valores que foram lidos; 
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
    c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 

"""

notas = []

while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

quantidade_notas = len(notas)

# a
print(f"Foram lidos {quantidade_notas} valores.")

# b
print("Valores informados na ordem original:", " ".join(map(str, notas)))

# c
print("Valores informados na ordem inversa:")

for nota in reversed(notas):
    print(nota)
