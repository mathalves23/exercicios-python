n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 > n2 and n1 > n3:
  maior = n1
elif n2 > n1 and n2 > n3:
  maior = n2
else:
  maior = n3
  
print(f'O maior número é o {maior}')