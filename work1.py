nombre = []
edad = []
salario = []

while True:
    n = input("Nombre: ")
    e = input("Edad: ")
    s = input("Salario: ")

    nombre.append(n)
    edad.append(e)
    salario.append(s)

    continuar = input("¿Deseas ingresar otra persona? (s/n): ").lower()
    if continuar != 's':
        break

print("Nombres:", nombre)
print("Edades:", edad)
print("Salarios:", salario)