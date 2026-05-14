# Evaluación Final POA
# Jesus Giovanny Garcia Ortiz
# Matriz con datos: [ID Cliente, Duracion en segundos, Eventos clics]

sesiones = [
    [1, 290, 12],
    [2, 45, 2],
    [3, 120, 9],
    [4, 150, 15],
    [5, 36, 1]
]

# Funcion para clasificar el compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Informe final
print("INFORME DE COMPROMISO DE CLIENTES")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente,
          "- Clasificacion:", clasificacion)