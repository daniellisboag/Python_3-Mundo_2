# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar no final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

soma_homens = soma_mulheres = soma_idade = 0

while True:
   print('-' * 40)
   print('Cadastre uma pessoa'.center(40))
   print('-' * 40)
   idade = int(input('Idade: '))
   sexo = ' '
   while sexo not in 'MF':
      sexo = input('Sexo: [M/F] ').strip().upper()[0]
   print('-' * 40)
   if idade > 18:
      soma_idade += 1
   if sexo == 'M':
      soma_homens += 1
   if sexo == 'F' and idade < 20:
      soma_mulheres += 1
   opcao = ' '
   while opcao not in 'SN':
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      print(f'Total de pessoa com mais de 18 anos: {soma_idade}')
      print(f'Ao todo temos {soma_homens} homen(s) cadastrados.')
      print(f'E temos {soma_mulheres} mulhere(s) com menos de 20 anos.')
      break