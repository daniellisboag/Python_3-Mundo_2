# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano = int(input('Ano de nascimento: '))
data_atual = datetime.now().year

print(f'Quem nasceu em {ano} tem {data_atual - ano} anos em {data_atual}.')
if data_atual - ano < 18:
   print(f'Ainda faltam {18 - (data_atual - ano)} anos para o alistamento.')
   print(f'Você vai se alistar no ano: {data_atual + (18 - (data_atual - ano))}')
elif data_atual - ano > 18:
   print(f'Quem nasceu nesse ano deveria ter se alistado em {data_atual + (18 - (data_atual - ano))}')
elif data_atual - ano == 18:
   print(f'E está no ano de alistamento.')