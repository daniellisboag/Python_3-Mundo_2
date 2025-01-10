# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado.
# Média entre 5.0 e 6.9: Recuperação.
# Média 7.0 ou superior: Aprovado.

primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
media = (primeira + segunda) / 2

if media < 5.0:
   print(f'A média entre {primeira :.1f} e {segunda :.1f} é igual a {media :.1f} e foi reprovado.')
elif media >= 5.0 and media < 7.0:
   print(f'A média entre {primeira :.1f} e {segunda :.1f} é igual a {media :.1f} e precisa de recuperação.')
elif media >= 7.0:
   print(f'A média entre {primeira :.1f} e {segunda :.1f} é igual a {media :.1f} e foi aprovado.')