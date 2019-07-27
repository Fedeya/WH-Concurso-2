
arboles = input("")
mensaje = "KO"

if len(arboles) < 100000:
  for i in range(len(arboles)):
    if i != 0 and arboles[0] == "Y":
      if arboles[i] == "Y":
        if arboles[i-1] != ".":
          mensaje = "KO"
          break
        else:
          mensaje = "OK" 
      if arboles[i] == "*":
        if arboles[i-1] != "Y":
          mensaje = "KO"
          break
        try:
          if arboles[i+1] != ".":
            mensaje = "KO"
            break
        except:
          mensaje = "KO"
        else:
          mensaje = "OK"
      if arboles[i] == ".":
        if arboles[i-1] == "*" or arboles[i-1] == "Y":
          mensaje = "OK"
        else:
          mensaje = "KO"
    elif i == 0 and arboles[0] == "*" and len(arboles) == 1:
      mensaje = "OK"
      break
        

print(mensaje)
