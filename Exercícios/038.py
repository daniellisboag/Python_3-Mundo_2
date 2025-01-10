# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior.
# O segundo valor é maior.
# Não existe valor maior, os dois são iguais.

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

if primeiro > segundo:
   print(f'O primeiro valor: {primeiro} é maior que o segundo valor: {segundo}')
elif segundo > primeiro:
   print(f'O segundo valor: {segundo} é maior que o primeiro valor: {primeiro}')
elif primeiro == segundo:
   print(f'Não existe valor maior.\nO primeiro valor: {primeiro} é igual ao segundo valor: {segundo}')