# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.

'''print('=' * 30)
print('10 termos de uma PA'.center(30))
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(termo, (termo + (10 - 1) * razao) + razao, razao):
   print(f' {c} -> ', end = '')
print('Fim!')'''

print('=' * 30)
print('10 termos de uma PA'.center(30))
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
conta = 1

while conta <= 10:
   print(f'{termo} -> ', end = '')
   conta += 1
   termo = (termo + razao)
print('Fim!')