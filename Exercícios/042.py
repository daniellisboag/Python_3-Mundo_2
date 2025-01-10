# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais.
# Isósceles: Dois lados iguais.
# Escaleno: Todos os lados diferentes.

comprimento1 = float(input('Digite o primeiro comprimento: '))
comprimento2 = float(input('Digite o segundo comprimento: '))
comprimento3 = float(input('Digite o terceiro comprimento: '))

if (comprimento1 + comprimento2 > comprimento3) and (comprimento1 + comprimento3 > comprimento2) and (comprimento2 + comprimento3 > comprimento1):
   print('Os comprimentos podem formar um triângulo do tipo ', end = '')
   if comprimento1 == comprimento2 and comprimento2 == comprimento3:
      print('equilátero: todos os lados iguais.')
   elif comprimento1 == comprimento2 or comprimento1 == comprimento3 or comprimento2 == comprimento3:
      print('isósceles: dois lados iguais.')
   elif comprimento1 != comprimento2 and comprimento1 != comprimento3 and comprimento2 != comprimento3:
      print('escaleno: todos os lados diferentes.')
else:
   print('Os comprimentos não podem formar um triângulo!')