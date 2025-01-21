# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# Observação: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-' * 30)
print('Banco Online'.center(30))
print('-' * 30)

valor = int(input('Qual valor você quer sacar? R$'))

if valor >= 50:
   print(f'Total de {valor // 50} de R$50')
   valor = valor % 50
if valor >= 20:
   print(f'Total de {valor // 20} de R$20')
   valor = valor % 20
if valor >= 10:
   print(f'Total de {valor // 10} de R$10')
   valor = valor % 10
if valor >= 1:
   print(f'Total de {valor // 1} de R$1')
   valor = valor % 1
print('Volte sempre ao Banco Online. Tenha um bom dia!')