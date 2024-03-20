print("calculo de reajuste de 15% do saldo")
saldo = float(input("Digite o saldo: "))

rejauste = (saldo* 0.015) + saldo

print(f"O novo saldo com rejuste ficaria: R${rejauste: .2f} ")