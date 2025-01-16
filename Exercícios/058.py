# Melhore o jogo do desagio 028 onde o computador vai 'pensar' em um número de 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

soma = 1
computador = randint(0, 10)

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
numero = int(input('Qual é o seu palpite? '))

while computador != numero:
   if computador > numero:
      print('Mais... Tente mais uma vez.')
      soma += 1
      numero = int(input('Qual é o seu palpite? '))
   else:
      print('Menos... Tente mais uma vez.')
      soma += 1
      numero = int(input('Qual é o seu palpite? '))
print(f'Acertou com {soma} tentativas. Parabéns!')