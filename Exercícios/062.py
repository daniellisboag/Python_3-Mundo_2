# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.

print('=' * 30)
print('10 termos de uma PA'.center(30))
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(termo, (termo + (10 - 1) * razao) + razao, razao):
   print(f' {c} -> ', end = '')
print('Pausa')

opcao = int(input('Quantos termos a mais você quer mostrar? '))
contador = 10
resultado = c + razao

while opcao != 0:
   contador += opcao
   for i in range(c, c + opcao):
      print(f'{resultado} -> ', end = ' ')
      resultado = resultado + razao
   print('Pausa')
   opcao = int(input('Quantos termos a mais você quer mostrar? '))
print(f'Progressão finalizada com {contador} termos mostrados.')