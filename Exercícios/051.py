# Desenvolva um programa que leia o primeiro termo e a razão de um PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('10 termos de uma PA'.center(30))
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(termo, (termo + (10 - 1) * razao) + razao, razao):
   print(f' {c} -> ', end = '')
print('Fim!')