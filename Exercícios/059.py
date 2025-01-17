# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

primeiro = float(input('Primeiro valor: '))
segundo = float(input('Segundo valor: '))
opcao = 0

while not opcao == 5:
   print('\n[1] Somar')
   print('[2] Multiplicar')
   print('[3] Maior')
   print('[4] Novo números')
   print('[5] Sair do programa')
   opcao = int(input('Qual é a sua opção? '))
   if opcao == 1:
      print(f'A soma de \033[34m{primeiro:.0f} \033[0me \033[34m{segundo:.0f} \033[0mé \033[32m{(primeiro + segundo):.0f}\033[0m')
   elif opcao == 2:
      print(f'A multiplicação de \033[34m{primeiro:.0f} \033[0me \033[34m{segundo:.0f} \033[0mé \033[32m{(primeiro * segundo):.0f}\033[0m')
   elif opcao == 3:
      print(f'O maior número é \033[32m{max(primeiro, segundo):.0f}\033[0m')
   elif opcao == 4:
      primeiro = float(input('Primeiro valor: '))
      segundo = float(input('Segundo valor: '))
   elif opcao == 5:
      print('Finalizando...')
   else:
      print('Opção inválida. Tente novamente!')
print('Fim do programa')