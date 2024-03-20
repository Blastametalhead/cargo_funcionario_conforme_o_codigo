import os 
os.system ('cls') 

print("O cálculo de quanta potência será necessária para o cômodo construído, por metros quadrados:")

largura = int(input("Digite a largura do cômodo (em metros):"))
comprimento = int(input("Digite o comprimento do cômodo (em metros):"))

area = largura * comprimento 
potencia = area * 18

import os 
os.system ('cls') 

print(f"Com base nos valores informados, a área construída é de{area: .2f} e a potência necessária a ser instalada neste cômodo é de{potencia: .2f} watts")
