resp = 'S'
soma = quant = media = 0

while resp in 'Ss':
  num = int(input('Digite um número: '))
  soma += num
  quant += 1
  media = soma / quant
  resp = str(input('Deseja continuar [S/N]: '))
  
print(f'A média dos {quant} números vale: {media}')