sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
  sexo = str(input('Dados inválidos. Por favor, informe seu seu sexo [M/F]: ')).strip().upper()[0]

if sexo == 'F':
  print(f'Sexo feminino registrado com sucesso.')
  
else:
  print(f'Sexo masculino registrado com sucesso.')