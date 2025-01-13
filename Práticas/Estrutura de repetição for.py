# Contagem
for c in range(0, 6):
   print(c)
print('Fim')

# Contagem de trás pra frente
for c in range(6, 0, -1):
   print(c)

# Pula de dois em dois
for c in range(0, 7, 2):
   print(c)

# Escolha um número
numero = int(input('Digite um número: '))

for c in range(0, numero + 1):
   print(c)

# Início, fim, passo
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim + 1, passo):
   print(c)

# Soma
soma = 0

for c in range(0, 4):
   numero = int(input('Digite um número: '))
   soma = soma + numero # soma += numero
print(f'A soma é {soma}')