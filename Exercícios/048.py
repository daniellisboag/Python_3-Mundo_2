# Faça um programa que calcule todos os números ímpares que são múltiplos
# de três e que se escontram no intervalo 1 até 500.

soma = 0
valores = 0
for contagem in range(1, 501):
   if contagem % 2 == 1:
      if contagem % 3 == 0:
         valores = valores + 1
         soma = soma + contagem
print(f'A soma de todos os {valores} valores solicitados é {soma}')