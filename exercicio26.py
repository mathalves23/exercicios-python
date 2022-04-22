lista = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']

while True:
  num = int(input('Digite um número de 0 a 10: '))
  if 0 < num < 10:
    break
  else: 
    print('Número inválido')
    
print(f'Você digitou o número {lista[num]}')