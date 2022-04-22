resp = 'S'
numeros = list()
while True:
  valor = int(input('Digite um valor: '))
  if valor not in numeros:
    numeros.append(valor)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado. Não vou adicionar.')
  resp = str(input('Quer continuar? [S/N] ')).upper()
  if resp == 'N':
    break
  elif resp not in 'SN':
    print('Resposta inválida.')
    while resp not in 'SN':
      resp = str(input('Quer continuar? [S/N] ')).upper()
      if resp not in 'SN':
        print('Resposta inválida.')
      elif resp == 'N':
        break

print(f'Você digitou os valores {numeros}')
