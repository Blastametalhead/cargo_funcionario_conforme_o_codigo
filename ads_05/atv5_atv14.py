import os 
os.system ('cls') 

print("Programa em que efetua o cálculo de restante do salário após pagamento das contas atrasadas")

salario = float(input("Digite o valor do seu salário:"))
conta1 = float(input("Digite o valor da primeira conta:"))
conta2 = float(input("Digite o valor da segunda conta:"))

total_conta1 = conta1 + conta1 * 2/100
total_conta2 = conta2 + conta2 * 2/100
resto_salario = salario - (total_conta1 + total_conta2)

import os 
os.system ('cls') 
print(f"O valor total das contas, com o acréscimo da multa em 2%. A primeira ficará em R${total_conta1: .2f} e a segunda em, R${total_conta2: .2f}")
print(f"O restante do salário será no valor de R$ {resto_salario: .2f}") 
