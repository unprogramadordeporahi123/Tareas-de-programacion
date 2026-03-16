def frecuencia_palabras(texto, ignoradas):
    # 1. Limpieza y conversión a lista
    palabras = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        if palabra not in ignoradas:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
                
    return frecuencias
ejemplo = "Hey muy buenas a todos guapisimos aqui vegeta 777 en un nuevo directo de planeta vegeta"

bloqueadas = ("hey", "guapisimos", "directo")

print(frecuencia_palabras(ejemplo, bloqueadas))