def categorizar_edades(edades):
    for edades in range(100):
     if edades < 0:
      print("Edad no válida")
     elif edades <= 17:
       print(f"Tienes {edades}  eres un menor de edad")
     elif edades <= 30:
      print(f"Tienes {edades} eres un adulto")
     elif edades <= 64:
      print(f"Tienes{edades} eres un anciano xd")
    else:
      print("pues listo xd")
categorizar_edades(99)