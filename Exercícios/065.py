# Crie um programa que leia várois números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos, O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

opcao = 'S'
soma = maior = soma_numeros = 0
menor = float('inf') # Valor infinito

while opcao.upper() == 'S':
   numero = int(input('Digite um número: '))
   soma_numeros += numero
   soma += 1

   if numero > maior:
      maior = numero
   if numero < menor:
      menor = numero

   opcao = input('Quer continuar? [S/N] ').strip()[0]

   if opcao.upper() not in 'SN':
      print('Opção inválida. Tente novamente!')
      opcao = 'N'

print(f'Você digitou {soma} números e média foi {(soma_numeros / soma):.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')