# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contagem = quantidade = soma = 0

while contagem != 999:
   numero = int(input('Digite um número [999 para parar]: '))
   contagem = numero
   if contagem != 999:
      quantidade += 1
      soma += numero
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}.')