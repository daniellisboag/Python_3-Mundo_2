# Crie um programa que mostre na tela todos o números pares que estão no intervalo entre 1 e 50.

for contagem in range(1, 51):
   if contagem % 2 == 0:
      print(contagem, end = ', ')
print('Fim!')

# Ou
for contagem in range(2, 51, 2):
   print(contagem, end = ', ')
print('Fim!')