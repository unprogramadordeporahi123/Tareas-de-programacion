def revisar_inventario(productos):
    reabastecer = {}
    for id, nombre, cantidad in productos:
        if cantidad < 10:
            reabastecer[id] = nombre
    return reabastecer

inventario = [
    (101, "Cereal", 3),
    (102, "Pizza", 4),
    (103, "Zelda", 5)
]

print("revisar el inventario")