def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16:
    return f'Com {idade} anos não se vota'
  elif (idade > 16 and idade < 18) or idade > 65:
    return f'Com {idade} anos o voto é facultativo'
  else:
    return f'Com {idade} anos o voto é obrigatório'


ano = int(input('Qual o ano do seu nascimento? '))
print(voto(ano))