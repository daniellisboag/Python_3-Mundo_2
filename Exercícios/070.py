# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$1000.
# c) Qual é o nome do produto mais barato.

total_compra = mais_mil = 0
mais_barato = float('inf')
produto_barato = ''

print('-' * 30)
print('Loja super barato'.center(30))
print('-' * 30)

while True:
   produto = input('Nome do produto: ')
   preco = float(input('Preço: R$'))
   opcao = ' '
   total_compra += preco
   while opcao not in 'SN':
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if int(preco) > 1000:
      mais_mil += 1
   if preco < mais_barato:
      produto_barato = produto
      mais_barato = preco
   if opcao == 'N':
      break
print(f'{' Fim do programa ':-^30}')
print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {produto_barato} que custa R${mais_barato:.2f}')