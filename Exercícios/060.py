# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5x4x3x2x1 = 120

# Resultado utilizando 'for'
fatorial = int(input('Digite um número para calcular seu fatorial: '))
resultado = 1

print(f'Calculando {fatorial}! = ', end = '')

for c in range(fatorial, 0, -1):
   resultado = resultado * c
   if c > 1:
      print(f'{c} x ', end = '')
   else:
      print(f'{c} = ', end = '')
print(resultado)

# Resultado utilizando 'while'
fatorial = int(input('Digite um número para calcular seu fatorial: '))
c = fatorial
resultado = 1

print(f'Calculando {fatorial}! = ', end = '')

while c > 1:
   resultado = resultado * c
   c -= 1
   print(c, end = '')
   print(f' x ' if c > 1 else ' = ', end = '')
print(resultado)