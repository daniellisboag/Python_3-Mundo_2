# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 Para binário.
# 2 Para Octal.
# 3 Para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('Escolha uma das conversões abaixo:')
print('[1] Binário.')
print('[2] Octal.')
print('[3] Hexadecimal.')
conversao = int(input('Qual será a base para conversão? '))

if conversao == 1:
   print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif conversao == 2:
   print(f'O número {numero} convertido para octal é {oct(numero)[2:]}')
elif conversao == 3:
   print(f'O número {numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
   print('Opção inválida. Tente novamente!')