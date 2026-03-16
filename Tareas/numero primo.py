import math

def numero_primo(primo):
    if primo < 2:
        return False
    for i in range(2, int(math.sqrt(primo)) + 1):
        if primo % i == 0:
            return False
    return True

numero = 17
if numero_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")