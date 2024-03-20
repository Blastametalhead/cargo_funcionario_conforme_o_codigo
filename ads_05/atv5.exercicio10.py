print("Calcule quanto sobrará a ração de dois gatos em 5 dias...")
peso_kg =float(input("Digite o peso em kg da ração: "))
gato1 =float(input("Digite o peso em gramas de quanto o primeiro gato consome: "))
gato2 =float(input("Digite o peso em gramas de quanto o segundo gato consome: "))
consumo = (gato1+gato2)*5
resta = peso_kg*1000 - consumo

print(f"A quantidade de ração que restará em gramas em 5 dias é : {resta}")