# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
soma = 0

for contagem in range(1, numero + 1):
   if numero % contagem == 0:
      print('\033[34m', end = ' ')
      soma += 1
   else:
      print('\033[m', end = ' ')
   print(f'{contagem}\033[m', end = ' ')
print(f'\nO número {numero} foi divisível {soma} vezes.')

if soma == 2:
   print('É um número primo.')
else:
   print('Não é um número primo!')