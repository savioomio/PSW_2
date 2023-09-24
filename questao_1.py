"""

1) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7 (h = altura)
    c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
    
"""

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite 'M' para masculino e 'F' para feminino: ")

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
    exit() 

peso_atual = float(input("Digite seu peso atual em quilogramas: "))

if peso_atual < peso_ideal:
    print("Você está abaixo do peso ideal.")
elif peso_atual > peso_ideal:
    print("Você está acima do peso ideal.")
else:
    print("Você está no peso ideal.")
