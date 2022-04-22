n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = 0
while option != 5:
  option = int(input('\n[ 1 ] somar \n [ 2 ] multiplicar \n [ 3 ] maior \n [ 4 ] novos números \n [ 5 ] sair do programa \n >>>> Qual é a sua opção? '))
  if option == 1:
    print(f'\nA soma de {n1} e {n2} vale {n1 + n2}')
  elif option == 2:
    print(f'\nA multiplicação de {n1} e {n2} vale {n1 * n2}')
  elif option == 3:
    if n1 > n2:
      print(f'\nO maior número é {n1}')
    elif n2 > n1:
      print(f'\nO maior número é {n2}')
    else:
      print('\nOs números são iguais')
  elif option == 4:
    n1 = int(input('\nPrimeiro valor: '))
    n2 = int(input('Segundo valor: '))
  elif option == 5:
    break
  else:
    print('NÚMERO INVÁLIDO! Digite uma opção válida.')