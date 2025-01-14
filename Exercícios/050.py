# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
conta = 0
for contagem in range(1, 7):
   numero = int(input(f'Digite o {contagem}° número: '))
   if numero % 2 == 0:
      soma = soma + numero
      conta = conta + 1
print(f'Você informou {conta} números pares e a soma foi {soma}')