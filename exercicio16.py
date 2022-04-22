valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do salário ? R$ '))
anos = int(input('Quantos anos ele vai pagar? '))
prestacao = valor / (anos * 12)
print(f'Para pagar uma casa de R$ {valor :.2f} em {anos}, a prestação será de R$ {prestacao :.2f}')

if prestacao > (salario * 0.30):
  print('O empréstimo foi NEGADO.')
else:
  print('Empréstimo APROVADO.')