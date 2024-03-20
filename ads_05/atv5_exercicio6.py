print("Conversão de segundos em minutos e minutos em segundos")
segundos = int(input("Digite os segundos: \n"))

minutos = segundos//60
segundos_2 = segundos%60

print(f"{minutos} minutos e {segundos_2} segundos")
