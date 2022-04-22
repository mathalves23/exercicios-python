velocidade = float(input('Qual é a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
  print('Você foi multado!')
  print(f'A multa será no valor de R$ {multa}')
else:
  print('Boa viagem!')