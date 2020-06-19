
valor_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Quantas horas você trabalha por mês? '))

salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = 0.11 * salario_bruto
desconto_inss = 0.08 * salario_bruto
desconto_sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print('\nO seu salário bruto é de R$ {}'.format(salario_bruto))
print('\nO desconto do Imposto de Renda foi de R$ {}'.format(desconto_ir))
print('\nO desconto do INSS foi de R$ {}'.format(desconto_inss))
print('\nO desconto do sindicato foi de R$ {}'.format(desconto_sindicato))
print('\nO seu salário líquido é de R$ {}'.format(salario_liquido))
