import os 
os.system ('cls') 
print("O programa que calcula o peso do usuário")

peso = float(input("Digite o seu peso atual (em quilos):"))

peso_a_ganhar = peso + peso *15/100
peso_a_perder = peso - peso * 20/100

import os 
os.system ('cls') 
print(f"O seu peso, ao ganhar 15 quilos, ficará em: {peso_a_ganhar: .0f} kg")
print(f"O seu peso, ao perder 20 quilos, ficará em: {peso_a_perder: .0f} kg")

