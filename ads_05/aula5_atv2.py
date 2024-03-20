print("Calcule o tempo de download de um arquivo em bits")

tamanho = int(input("Digite o tamanho do arquivo (em bits): \n"))
velocidade = float(input("Digite a velocidade da conexão(em bits/segundo): \n"))

minutos = tamanho//velocidade
segundos = tamanho%velocidade
print(f" o tempo que levará: {minutos: .0f} minutos e {segundos} segundos")