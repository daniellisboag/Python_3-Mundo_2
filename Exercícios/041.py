# A conferação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim.
# Até 14 anos: Infantil.
# Até 19 anos: Junior.
# Até 25 anos: Sênior.
# Acima: Master.

from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento

print(f'Quem tem {idade} é classificado como: ', end = '')
if idade <= 9:
   print('Mirim')
elif idade <= 14:
   print('Infantil')
elif idade <= 19:
   print('Junior')
elif idade <= 25:
   print('Sênior')
elif idade > 20:
   print('Master')