def agregar_estudiante(estudiantes):
    #agregar al estudiante con los datos de este 

    nombre = input("Nombre completo del etsudiante: ")
    #el try por si hay algún error lo encasule 
    try:
        id_del_estudiante = int(input("ingrese el id del estudiante: "))
        edad_delestudiante = int(input("ingrese la edad estudiante:  "))

    except ValueError:
        print("Datos inválidos")
        return
    
    estado_del_estudiante = input(" Ingrese el estado actual del estudiantes activo/ inactivo: ").strip()
    programa = input("Ingrese programa alque pertenece el estudiante: ").strip()
# edad del estudiante mayor a 0
# id del estudiante mayor a 0, el 0 como id no es valido

    if edad_delestudiante < 0 or id_del_estudiante < 0:
        print("Valores negativos no permitidos")

        return
# guardar datos del estudiante
    estudiante = {
        "nombre": nombre,
        "id": id_del_estudiante,
        "edad": edad_delestudiante,
        "estado": estado_del_estudiante,
        "programa": programa
    }
    
    estudiantes.append(estudiante)
    print("agregado correctamente")


    
def mostrar_menu():
 print("\n========= MENÚ ESTUDIANTES =========")
 print("1. Registrar nuevos estudiantes.")
 print("2. Consultar la lista de estudiantes.")
 print("3. Buscar un estudiante por el nombre")
 print("4.Actualizar la información de un estudiante.")
 print("5. Eliminar estudiantes.")
 print("6. Guardar csv")
 print("7. Cargar csv")
 print("8. Salir")



def mostrar_estudiantes(estudiantes):

    if not estudiantes:
        print("No hay estudiantes registrados")
        return

    print("\n ESTUDIANTES")
    for p in estudiantes:
        print(f"{p['nombre']} | {p['id']} | {p['edad']} | {p['estado']} | {p['programa']}")

    
def buscar_estudiante(estudiantes):

    nombre = input("ingrese el nombre completo del estudiante, como lo registro:  ").strip()

    for p in estudiantes:
        if p["nombre"].lower() == nombre.lower():
            print("estudiante encontrado: ")
            print(p)
            return

    print("estudiante no encontrado")


    # ACTUALIZAR ESTUDIANTE

def actualizar_estudiante(estudiantes):
    print("tenga encuenta que los datos se actualizan todos")

    nombre = input("Nombre del estudiante a actualizar / escriba no si ya no desea, lo regresa al menú principal: ").strip()

    for p in estudiantes:
        if p["nombre"].lower() == nombre.lower():

            try:
                id_del_estudiante = int(input("Nuevo id del estudiante: "))
                edad_delestudiante = int(input("Nueva edad del estudiante: "))
            except ValueError:
                print("Datos inválidos")
                return

            if id_del_estudiante < 0 or edad_delestudiante < 0:
                print("Valores negativos no permitidos")
                return

            p["id"] = id_del_estudiante
            p["edad"] = edad_delestudiante

            print("datos actualizados")
            return

    print("estudiante no encontrado o salio de la actualización de datos")

    # ELIMINAR ESTUDIANTE
def eliminar_estudiante(estudiantes):

    nombre = input("nombre completo del estudiante que desea eliminar: ").strip()

    for p in estudiantes:
        if p["nombre"].lower() == nombre.lower():
            estudiantes.remove(p)
            print("Estudiante eliminado")
            return

    print("No se encontro estudiante")





