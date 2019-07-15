from datetime import date
import math

T = int(input(""))
casos = []

for i in range(T):
  e = input("")
  casos.append(e)

for i in casos:
  dates = i.split(" ")
  d1 = dates[0].split("-")
  d2 = dates[1].split("-") 

  d1 = date(2019, int(d1[1]), int(d1[0]))
  d2 = date(2019, int(d2[1]), int(d2[0]))

  if d1 == d2:
    resultado = 0
  else: 
    resultado = d1 - d2
    resultado = int(str(resultado).split(",")[0].split(" ")[0])
    if resultado < 0:
      resultado =- resultado

  print(resultado)