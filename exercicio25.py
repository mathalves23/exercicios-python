from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitoria = 0

while True:
  print('=-' * 20)
  user = int(input('Digite um valor: '))
  escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()
  pc = randint(0, 10)
  soma = user + pc
  parimpar = 'P'

  print('--' * 20)
  print(f'Você escolheu {user} e o computador escolheu {pc}. A soma vale {soma}')
  print('--' * 20)

  if soma % 2 == 0:
    parimpar = 'P'
  else:
    parimpar = 'I'

  if escolha == parimpar:
    vitoria += 1
    print('Você VENCEU!!')
    print('Vamos jogar novamente...')
  else:
    print('Você PERDEU!')
    print('=-' * 20)
    print(f'GAME OVER! Você venceu {vitoria} vezes.')
    break