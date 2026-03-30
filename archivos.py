# GUARDAR INVENTARIO EN CSV


def guardar_csv(estudiantes, ruta, incluir_header=True):

    # MIRAMOS SI EL INVENTARIO ESTA VACIO 
    if not estudiantes:
        print(" No hay etsudiantes para guardar en el registro")
        return
    
    #PREVENCIÓN DE ERRORES 
    
    try:
        # ABRIR ARCHIVO EN ESCRITURA
        with open(ruta, "w", encoding="utf-8") as archivo:

            # ENCABEZADO
            if incluir_header:
                archivo.write("nombre,id,edad,estado,programa\n")

            # Escribir estudiantes
            for estudiante in estudiantes:
                linea = f"{estudiante ["nombre"]}, {estudiante['id']},{estudiante['edad']}, {estudiante['estado']},{estudiante['programa']}\n"
                archivo.write(linea)

        print(f" Estudiantes guardado en: {ruta}")

    except PermissionError:
        print(" Error: No tienes permisos para escribir en esa ubicación.")

    except Exception as e:
        print(" Error al guardar el archivo:", e)


# Cargar estudiantes 
def cargar_csv(ruta, estudiantes_actuales):

    estudiantes_subidos = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

            # VALIDACIÓN DEL ENCABEZADO
            encabezado = lineas[0].strip()
            print (encabezado)
            if encabezado != "nombre,id,edad,estado,programa":
                return estudiantes_actuales

            # RECORRE Y LEE LAS LINEAS
            for linea in lineas[1:]:

                datos = linea.strip().split(",")

                # VALIDA LAS COLUMNAS
                if len(datos) != 5:
                    filas_invalidas += 1
                    continue

                try:
                    nombre = datos[0]
                    id = int(datos[1])
                    edad = int(datos[2])
                    estado = datos[3]
                    programa = datos[4]

                    # VALIDACIÓN DE NEGATIVOS 
                    if id < 0 or edad < 0:
                        filas_invalidas += 1
                        continue

                    estudiante = {
                        "nombre": nombre,
                        "id": id,
                        "edad": edad,
                        "estado":estado,
                        "programa": programa
                    }

                    estudiantes_subidos.append(estudiante)

                except ValueError:
                    filas_invalidas += 1 




        # USUARIO ESCOGE SI SOBRESCRIBIR
        opcion = input("¿Sobrescribir inventario actual? (S/N): ").upper()

        
        # REEMPLAZAR INVENTARIO SI OPCION = S
        
        if opcion == "S":
            estudiantes_actuales = estudiantes_subidos
            accion = "Reemplazo total"

        # FUSIONAR INVENTARIO
   
        else:
            accion = "Fusión"

            for nuevo in estudiantes_subidos:

                encontrado = False

                for actual in estudiantes_actuales:
                    if actual["nombre"].lower() == nuevo["nombre"].lower():

                        # política:
                        # id nuevo y edad actulizada
                        actual["id"] = nuevo["id"]
                        actual["edad"] = nuevo["edad"]

                        encontrado = True
                        break

                if not encontrado:
                    estudiantes_actuales.append(nuevo)

       
        print("\n Carga finalizada")
        print("Productos cargados:", len(estudiantes_subidos))
        print("Filas inválidas omitidas:", filas_invalidas)
        print("Acción realizada:", accion)

        return estudiantes_actuales

    # MENSAJE DE ERRORES
    except FileNotFoundError:
        print(" Archivo no encontrado.")
        return estudiantes_actuales

    except UnicodeDecodeError:
        print(" Error de codificación del archivo.")
        return estudiantes_actuales

    except Exception as e:
        print(" Error inesperado:", e)
        return estudiantes_actuales
               