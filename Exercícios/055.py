# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menos peso lidos.

maior = 0
menor = float('inf')

for contagem in range(1, 6):
   peso = float(input(f'Digite o peso da {contagem}° pessoa: '))
   if peso > maior:
      maior = peso
   if peso < menor:
      menor = peso
   
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')