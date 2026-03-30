
from  servicio import *
print("Welcome student system")

estudiantes = []
option = 0
    
while option != 8:
    mostrar_menu()

    try:
        option = int(input("Ingrese una opción (1-8): "))

        if option < 1 or option > 8:
            print("Opción fuera de rango.")
            continue

    except ValueError:
        print("Debe ingresar un número.")
        continue


#AGREGAR UN ESTUDIANTE
    if option == 1:
        agregar_estudiante(estudiantes)

    if option == 2:
        mostrar_estudiantes(estudiantes)

    if option == 3:
        buscar_estudiante(estudiantes)

    if option == 4:
        actualizar_estudiante(estudiantes)



