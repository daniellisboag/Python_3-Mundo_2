# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().split()
inverter = ''.join(frase).upper()

print(f'O inverso de {inverter} é {inverter[::-1]}')

if inverter == inverter[::-1]:
   print('Temos um palíndromo!')
else:
   print('A frase digitada não é um palíndromo!')

#Ou
frase = input('Digite uma frase: ').strip().split()
juntar = ''.join(frase).upper()
inverter = ''

for inverso in range(len(juntar) - 1, -1, -1):
   inverter += juntar[inverso]
print(f'O inverso de {juntar} é {inverter}')

if inverter == juntar:
   print('Temos um palíndromo!')
else:
   print('A frase digitada não é um palíndromo!')