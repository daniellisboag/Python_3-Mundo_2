# 1
for c in range(1, 10):
   print(c)
print('Fim')

# 2
c = 1

while c < 10:
   print(c)
   c += 1
print('Fim')

# 3
n = 1

while n != 0:
   n = int(input('Digite um valor: '))
print('Fim')

# 4
r = 'S'

while r.upper() == 'S':
   n = int(input('Digite um valor: '))
   r = input('Quer continuar? [S/N] ')
print('Fim')

# 5
n = 1
par = impar = 0

while n != 0:
   n = int(input('Digite um valor: '))
   if n != 0:
      if n % 2 == 0:
         par += 1
      else:
         impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')

# 1 - Loop infinito
contador = 1

while True:
   print(contador, end = ' ')
   contador += 1

# 2
numero = soma = 0
while numero != 999:
   numero = int(input('Digite um número: '))
   if numero == 999:
      break
   soma += numero
print(f'A soma vale {soma}')