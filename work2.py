c = 1
persona = []

while c <= 5:
    n = input("Nombre: ")
    e = input("Edad: ")
    s = input("Salario: ")

    datos = {
        "nombre": n,
        "edad": e,
        "salario": s
    }

    persona.append(datos)
    c += 1

print(persona)