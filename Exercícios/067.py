# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usúario. O programa será interrompido quando o número solicitado for negativo.

while True:
   tabuada = int(input('Quer ver a tabuada de qual valor? '))
   if tabuada < 0:
      break
   print('-' * 40)
   for c in range(1, 11):
      print(f'{tabuada} x {c} = {tabuada * c}')
   print('-' * 40)

print('Programa de tabuada encerrado. Volte sempre!')