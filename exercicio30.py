from random import randint
lista = list()
jogos = list()
print('-=' * 30)
print('     Jogos da Mega Sena     ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0
while tot <= quant:
  cont = 0
  while True:
    num = randint(1, 60)
    if num not in lista:
      lista.append(num)
    if cont >= 6:
      break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
  print(f'Os números sorteados foram {lista} \n')