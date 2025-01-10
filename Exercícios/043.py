# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

print(f'Seu peso é {peso:.2f}Kg e sua altura é {altura:.2f}. O índice de massa corporal é {imc:.1f}')
if imc < 18.5:
   print('Classificação: Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
   print('Classificação: Peso ideal.')
elif imc >= 25 and imc < 30:
   print('Classificação: Sobrepeso!')
elif imc >= 30 and imc < 40:
   print('Classificação: Obesidade!')
elif imc >= 40:
   print('Classificação: Obesidade mórbida.')