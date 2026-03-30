def agregar_estudiante(estudiantes):

    nombre = input("Nombre del etsudiante: ")
    
    try:
        id_del_estudiante = int(input("ingrese el id del estudiante: "))
        edad_delestudiante = int(input("ingrese la edad estudiante:  "))
        estado_del_estudiante = input(" Ingrese el estado actual del estudiantes activo/ inactivo: ").strip
        programa = input("Ingrese programa alque pertenece el estudiante: ").strip

    except ValueError:
        print("Datos inválidos")
        return

    if edad_delestudiante < 0 or id_del_estudiante < 0:
        print("Valores negativos no permitidos")

        return
    
    estudiante = {
        "nombre": nombre
        "id": id_del_estudiante
        "estado": estado_del_estudiante
        "programa": programa
    }
    
    estudiantes.append(estudiante)
    print("agregado correctamente")
    
    

    