jogador = str(input('Digite o nome do jogador: '))
gols = int(input('Quantos gol ele fez? '))

def ficha(a, b):
  print(f'O jogador {a} fez {b} gol(s) no campeonato.')
  

ficha(jogador, gols)