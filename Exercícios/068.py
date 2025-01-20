# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

soma = 0

print('-' * 30)
print('Vamos jogar par ou ímpar'.center(30))
print('-' * 30)

while True:
   computador = randint(0, 10)
   numero = int(input('Digite um valor: '))
   opcao = ' '
   while opcao not in 'PI':
      opcao = input('Par ou ímpar? [P/I] ').strip().upper()[0]
   print('-' * 60)
   print(f'Você jogou {numero} e o computador {computador}. Total de {numero + computador} deu', 'par' if (numero + computador) % 2 == 0 else 'ímpar')
   print('-' * 60)
   if (numero + computador) % 2 == 0 and opcao == 'P':
      soma += 1
      print('Você venceu!\nVamos jogar novamente...')
      print('-' * 60)
   elif (numero + computador) % 2 != 0 and opcao == 'I':
      soma += 1
      print('Você venceu!\nVamos jogar novamente...')
      print('-' * 60)
   else:
      print('Você perdeu!')
      print(f'Game over. Você venceu {soma} vezes!')
      break