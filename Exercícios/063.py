# Escreva um programa que leia um número 'n' inteiro qualquer e mostre
# na tela os 'n' primeiros elementos de uma sequência de fibonacci.
# Exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# Utilizando 'for'
print('=' * 40)
print('Sequência de fibonacci'.center(40))
print('=' * 40)

opcao = int(input('Quantos termos você quer mostrar? '))
print('0 -> ', end = '')

valor_1 = 0
valor_2 = 1
valor_3 = valor_1 + valor_2

for c in range(1, opcao):
   print(f'{valor_3} -> ', end = '')
   valor_1 = valor_2 + valor_1
   valor_2 = valor_3
   valor_3 = valor_1
print('Fim!')

# Utilizando 'while'
print('=' * 40)
print('Sequência de fibonacci'.center(40))
print('=' * 40)

opcao = int(input('Quantos termos você quer mostrar? '))

valor_1 = 0
valor_2 = 1
print(f'{valor_1} -> {valor_2}', end = '')
contagem = 3

while contagem <= opcao:
   valor_3 = valor_1 + valor_2
   print(f' -> {valor_3}', end = '')
   valor_1 = valor_2
   valor_2 = valor_3
   contagem += 1
print(' -> Fim!')