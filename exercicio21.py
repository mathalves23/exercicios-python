soma = 0
c = 0
for c in range(0, 6):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    soma += 1
    
print(f'A soma dos números vale: {soma}')