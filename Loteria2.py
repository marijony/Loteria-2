import random

extracciones = 0
import random
continuar = ""

extracciones = 0
numero_jugado = ""


def premio_gordo():
    return str(random.randint(0,99999)).zfill(5)

while continuar != "N":
    while True:
        numero_jugado = input("¿Qué número deseas jugar con un maximo de 5 cifras?: ")
        if numero_jugado.isnumeric() and (int(numero_jugado) > 0 and int(numero_jugado) < 100000):
            break
        print("Número no válido. Inténtalo de nuevo.")

    while premio_gordo() != str(numero_jugado).zfill(5):
        extracciones += 1

    print("---------------------------")
    print("Jugaste con el número {0}.".format(str(numero_jugado).zfill(5)))
    print("Has logrado el premio gordo tras {0} sorteos".format(extracciones))
    print("A razón de 3€ por semana, te has gastado {0:,}€ y has tardado {1:.2f} años en acertar.".format(3 * extracciones, extracciones / 52))

    continuar = input ("Quieres jugar otra vez (S/N)?: ").upper()
print("Ha sido un placer hasta otra. ")