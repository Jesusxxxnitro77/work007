import random
import os
import time

# Función para dibujar el dado con asteriscos
def dibujar_dado(numero):
    caras = {
        1: ["     ",
            "  *  ",
            "     "],

        2: ["*    ",
            "     ",
            "    *"],

        3: ["*    ",
            "  *  ",
            "    *"],

        4: ["*   *",
            "     ",
            "*   *"],

        5: ["*   *",
            "  *  ",
            "*   *"],

        6: ["*   *",
            "*   *",
            "*   *"]
    }

    print("-------")
    for linea in caras[numero]:
        print(f"|{linea}|")
    print("-------")

# Simular el dado
dado = random.randint(1, 6)

print(f"\nNúmero en el dado: {dado}\n")
dibujar_dado(dado)
