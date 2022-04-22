from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
  print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
  print(f'Ainda faltam {18 - idade} anos para o alistamento')
else:
  print(f'Você deveria ter se alistado há {idade - 18} anos.')