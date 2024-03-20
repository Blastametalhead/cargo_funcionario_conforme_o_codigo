print("Calculo do salário e horas trabahadas juntamente com o  imposto de 3% ")
salario = float(input("Digite o salário: "))
num_horas = int(input("Digite o número de horas trabalhadas: "))

valor_ht = salario/2
sal_bruto = valor_ht*num_horas
imposto= sal_bruto * (3/100)
sal_receber = sal_bruto-imposto

print(f'Valor da hora trabalhada: {valor_ht: .2f} \n Salário Bruto: R${sal_bruto: .2f} \n imposto de 3%: R${imposto: .2f} \n Salário a receber: R${sal_receber: .2f} ')
