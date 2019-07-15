T = int(input(""))
casos = []

for i in range(T):
  e = int(input(""))
  casos.append(e)

for caso in casos:
  resultado = 0
  for i in range(caso + 1):
    resultado += 3 * i
  print(resultado)
