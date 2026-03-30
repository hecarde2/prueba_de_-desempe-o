#importación
from  servicio import *
from archivos import guardar_csv, cargar_csv
print("Welcome student system")

estudiantes = []
option = 0
#ciclo 
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


    #menú de opciones 
    if option == 1:
        agregar_estudiante(estudiantes)

    if option == 2:
        mostrar_estudiantes(estudiantes)

    if option == 3:
        buscar_estudiante(estudiantes)

    if option == 4:
        actualizar_estudiante(estudiantes)

    if option == 5:
        eliminar_estudiante(estudiantes)

    if option == 6:
        ruta = input("Nombre del archivo .csv: ")

        partes = ruta.split(".")
        #NO PERMITE GUARDAR ARCHIVO QUE NO SEA csv
        if partes[-1] != "csv":
            print("Archivo con formato invalido, formato permitido .csv")
            continue

        guardar_csv(estudiantes, ruta)

    # CARGAR CSV1
    elif option == 7:
        ruta = input("Archivo a cargar: ")

        partes = ruta.split(".")

        if partes[-1] != "csv":
            print("Archivo con formato invalido, formato permitido .csv")
            continue

        inventario = cargar_csv(ruta, estudiantes)

    elif option == 8:
        print("HASTA PRONTO")
        break



