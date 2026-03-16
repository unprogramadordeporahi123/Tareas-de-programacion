def filtrar_pares(numeros):
    for numeros in range(21):
        if numeros % 2 == 0:
            print(f"{numeros} es un numero par, saltando a la siguiente iteracion")
            continue
        print(f"{numeros} es impar xd")
filtrar_pares(20)

print("ya se acabaron los numeros xd")