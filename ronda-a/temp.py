import numpy as np

T = int(input(""))
casos = []
matriz = []
matrices = []

for i in range(T):
  cantMatrices = int(input(""))
  if 0 < cantMatrices <= 50:
    for x in range(cantMatrices):
      e = input("")
      casos.append(e)

for caso in casos:
  caso = caso.split(" ")
  matriz.append(caso)
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] == "0":
        matriz[i][j] = ""
  for i in range(len(matriz)):
    matrices.append(matriz)
  matriz.clear()

# matrizUpper = np.tril(matriz)
# matrizLower = np.triu(matriz)

print(matrices)

