asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []

print("Vamos a revisar tus notas del curso.")

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota obtuviste en {asignatura}? "))
    if nota < 5:
        repetir.append(asignatura)

if repetir:
    print("Tendrás que repetir las siguientes asignaturas:")
    for asig in repetir:
        print(f"- {asig}")
else:
    print("Muy bien, has aprobado todas las asignaturas.")
