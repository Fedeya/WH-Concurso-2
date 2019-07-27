def vampiro(n):
  numeros = range(10**(n//2 - 1), 10**(n//2))
  for i in numeros:
    for x in numeros:
      V, X, Y = str(i*x), str(i), str(x)
      if X[-1] + Y[-1] != '00' and sorted(V) == sorted(X+Y):
        yield i*x

T = int(input())
casos = []

for i in range(T):
  numero = input("")
  casos.append(numero)

for caso in casos:
  vampiros = sorted(set(vampiro(4)))
  if int(caso) in vampiros:
    print("SI")
  else:
    print("NO")