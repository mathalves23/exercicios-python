from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))
computador = randint(0, 5)
if jogador == computador:
  print(f'ACERTOU! Nós dois pensamos no número {computador}!')
else:
  print(f'ERROU! Você pensou no número {jogador} e eu pensei no número {computador}!')
