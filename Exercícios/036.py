# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor do imovel? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))

if casa / (anos * 12) <= salario * 0.30:
   print('Parabéns! Seu empréstimo foi aprovado.')
   print(f'O valor da casa é R${casa :.2f}, você irá pagar R${casa / (anos * 12) :.2f} por mês, por {anos} anos.')
else:
   print(f'O empréstimo foi reprovado. Pois o valor da prestação é R${casa / (anos * 12) :.2f} e não pode exceder 30% do seu salário.')
   print(f'30% do seu salário é R${salario * 0.30 :.2f}')