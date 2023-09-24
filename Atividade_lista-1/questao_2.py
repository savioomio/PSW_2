"""
2) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
usando este link (em minutos).

"""

a_mb = float(input("Digite o tamanho do arquivo em MB: "))
v_rede = float(input("Digite a velocidade da Internet em Mbps: "))

a_bs = a_mb * 8 * 1024 * 1024  
tempo_d = a_bs / (v_rede * 60)  

print(f"O tempo aproximado de download do arquivo é de {tempo_d:.2} minutos.")
