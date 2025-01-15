# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# O nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

count_m = 0
count_idade_m = 0
media = 0
h_velho = ''

for contagem in range(1, 5):
   print(f'----- {contagem}° Pessoa -----')
   nome = input('Nome: ').strip()
   idade = int(input('Idade: '))
   sexo = input('Sexo [M/F]: ').strip()
   media = media + idade 
   if sexo.upper() == 'M' and idade > count_idade_m:
      h_velho = nome
      count_idade_m = idade
   if sexo.upper() == 'F' and idade < 20:
      count_m += 1

print(f'A média de idade do grupo é de {media / 4} anos.')
print(f'O homem mais velho tem {count_idade_m} anos e se chama {h_velho}.')
print(f'Ao todo são {count_m} mulheres com menos de 20 anos.')