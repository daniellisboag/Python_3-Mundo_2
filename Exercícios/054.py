# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.

from datetime import date

velho = 0
novo = 0

for contagem in range(1, 8):
   ano = int(input(f'Em que ano a {contagem}° pessoa nasceu? '))
   idade = date.today().year - ano
   if idade >= 21:
      velho += 1
   else:
      novo += 1

print(f'Ao todo tivemos {velho} pessoas maiores de idade.')
print(f'E também tivemos {novo} pessoas menos de idade.')