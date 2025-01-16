# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite seu sexo: [M/F] ')

while sexo.upper() != 'M' and sexo.upper() != 'F':
   sexo = input('Dados inválidos. Por favor, informe seu sexo: ')

if sexo.upper() == 'M':
   print('Sexo masculino registrado com sucesso.')
elif sexo.upper() == 'F':
   print('Sexo feminino registrado com sucesso.')

# Ou
sexo = input('Informe seu sexo: [M/F] ').strip()[0]

while sexo not in 'MmFf':
   sexo = input('Dados inválidos. Por favor informe seu sexo: ').strip()[0]

if sexo.upper() == 'M':
   print('Sexo masculino registrado com sucesso.')
elif sexo.upper() == 'F':
   print('Sexo feminino registrado com sucesso.')