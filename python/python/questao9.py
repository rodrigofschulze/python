horas = float(input("Qual valor você ganha por horas?"))
horas_trabalhadas = float(input("Quantas horas você trabalhou?"))
salario_trabalho = horas * horas_trabalhadas
desconto =  salario_trabalho * 0.11
salario_liquido = salario_trabalho - desconto
print(f"Seu salário final é {salario_liquido}")