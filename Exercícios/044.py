# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# Em até 2x no cartão: Preço normal.
# 3x ou mais no cartão: 20% de juros.

preço = float(input('Qual o valor da compra? R$'))

print('Fomas de pagamento:')
print('[1] à vista dinheiro / cheque.')
print('[2] à vista no cartão.')
print('[3] até 2x no cartão.')
print('[4] 3x ou mais no cartão.')
escolha = int(input('Qual é a forma de pagamento? '))

if escolha == 1:
   print(f'A compra de R${preço:.2f} terá um desconto de 10% e o total a ser pago será R${preço - (preço * 0.10):.2f}')
elif escolha == 2:
   print(f'A compra de R${preço:.2f} terá um desconto de 5% e o total a ser pago será R${preço - (preço * 0.05):.2f}')
elif escolha == 3:
   print(f'Sua compra será parcelada em 2x de R${preço / 2:.2f}')
   print(f'O valor total da compra será R${preço:.2f}')
elif escolha == 4:
   parcelas = int(input('Quantas parcelas? '))
   print(f'Sua compra será parcelada em {parcelas}x de R${(preço + (preço * 0.20)) / parcelas:.2f} com juros.')
   print(f'A compra de R${preço:.2f} terá uma taxa de 20% de juros e o total a ser pago será R${preço + (preço * 0.20):.2f}')
else:
   print('Opção inválida! Tente novamente.')