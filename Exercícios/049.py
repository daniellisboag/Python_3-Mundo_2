# Refaça o desafio 009, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número para ver sua tabuada: '))

for contagem in range(1, 11):
   print(f'{numero} x {contagem} = {numero * contagem}')