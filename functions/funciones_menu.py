
#ESTE MÓDULO CONTIENE LAS FUNCIONES QUE SE USAN EN CADA OPERACIÓN DEL MENÚ PRINCIPAL

#IMPORTAMOS LOS MODULOS NECESARIOS
from funciones import ControlStock
from datetime import datetime, timedelta
import funciones_estadisticas as fm
import os 
import clases as cl
from db import engine

#FUNCIÓN PARA LISTAR, LE PASAMOS UNA OPCIÓN, SI ES U, LISTA LOS USUARIOS, SI ES L, LISTA LOS LIBROS.
def listar(opcion):
            if opcion.lower() == "u":
                usuarios = ControlStock("","Usuarios")
                lista_obj_usuarios = []
                for usuario in usuarios.read():
                    objeto = cl.Usuario(usuario[0], usuario[1], usuario[2], usuario[3],usuario[4])
                    lista_obj_usuarios.append(objeto)
                return lista_obj_usuarios
                    
            elif opcion.lower() == "l":
                libros = ControlStock("","Libros")
                lista_obj_libros = []
                for libro in libros.read():
                    objeto = cl.Libro(libro[1], libro[2], libro[3])
                    lista_obj_libros.append(objeto)
                return lista_obj_libros
 
#FUNCIÓN PARA CREAR UN USUARIO, CON LOS INPUTS NECESARIOS VAMOS INGRESANDO LOS DATOS SOLICITADOS 
# Y LUEGO USA LA CLASE CONTROLSTOCK PARA INSERTARLO EN LA BASE DE DATOS.                                   
def crear_usuario():
        print("\tCREACIÓN DE USUARIO\n")
        dni = input("Ingrese el DNI del usuario -> ")
        nombre = input("Nombre del usuario -> ")
        apellido = input("Apellido del usuario -> ")
        direccion = input("Dirección -> ")
        correo = input("Correo electrónico -> ")
        datos = (dni, nombre, apellido, direccion, correo)
        usuario_nuevo = ControlStock("","Usuarios")
        if usuario_nuevo.insert(datos):
            return f"Usuario ingresado -> {datos}"
        else:
            return "Ocurrió un error."         

#FUNCIÓN PARA AGREGAR UN LIBRO, CON LOS INPUTS NECESARIOS VAMOS INGRESANDO LOS DATOS SOLICITADOS 
# Y LUEGO USA LA CLASE CONTROLSTOCK PARA INSERTARLO EN LA BASE DE DATOS.       
def agregar_libro():
            print("\tAGREGANDO UN NUEVO LIBRO AL CATÁLOGO\n")
            libros = ControlStock("", "libros")
            id = len(libros.read()) + 1
            nombre_libro = input("Nombre del libro -> ")
            autor = input("Autor -> ")
            estado = input("Estado -> ")
            datos = (id, nombre_libro.capitalize(), autor.capitalize(), estado)
            if libros.insert(datos):
                return f"Libro agregado -> {datos}"
            else:
                return "Ocurrió un error."
 
#FUNCIÓN PARA RESERVAR UN LIBRO, SE INGRESAN LOS DATOS DEL LIBRO A SOLICITAR, SE VERIFICA QUE EL LIBRO NO ESTÉ ALQUILADO
# SI ESTÁ, SE CORTA LA EJECUCIÓN Y RETORNA UN MENSAJE DICIENDO QUE YA ESTÁ ALQUILADO, SINO CONTINUA, ACTUALIZA EL ESTADO DEL LIBRO A 'alquilado'
# Y LUEGO CREA LA RESERVA.       
def reservar_libros():
    print("\tRESERVA DE LIBROS\n")
    
    crear_reserva = ControlStock("", "reservas")
    linea = len(crear_reserva.read()) + 1
    libro_reserva = input("Ingrese el libro a reservar -> ")
    usuario = input("Ingrese el DNI del usuario -> ")
    fecha = datetime.now().date()
    devolucion = fecha + timedelta(days=15)

    verificar_estado = ControlStock("Libro", "libros")
    busqueda = verificar_estado.search_product(libro_reserva)

    if busqueda:
        libro = cl.Libro(busqueda[1], busqueda[2], busqueda[3])
        if libro.estado == 'alquilado':
            return f"EL LIBRO '{libro_reserva}' YA ESTÁ RESERVADO"

        try:
            with engine.begin() as conn:
                # UPDATE STATE
                update_query = f"UPDATE libros SET Estado = 'alquilado' WHERE Libro = '{libro_reserva}'"
                conn.exec_driver_sql(update_query)

                # GET BOOK ID
                id_query = f"SELECT ID_Libro FROM libros WHERE Libro = '{libro_reserva}'"
                id_libro = conn.exec_driver_sql(id_query).fetchone()

                datos = (linea, usuario, id_libro[0], fecha, devolucion)

                if crear_reserva.insert(datos):
                    reserva = cl.Reserva(linea, usuario, id_libro[0], str(fecha), str(devolucion))
                    return f"Alquiler realizado -> {reserva}"

        except Exception as e:
            return f"Ocurrió un error: {e}"

    else:
        return "NO SE HA ENCONTRADO EL LIBRO"
  
#FUNCIÓN PARA DEVOLVER UN LIBRO, SE SOLICITA EL NOMBRE DEL MISMO Y EL DNI DEL USUARIO, LUEGO SE MODIFICA EL ESTADO A 'libre' Y SE RETORNA
# UN MENSAJE DICIENDO QUE EL LIBRO SE DEVOLVIÓ               
def devolver_libros():
    print("\tDEVOLUCIÓN DE LIBROS\n")
    libro_reserva = input("Ingrese el libro devuelto -> ")
    usuario = input("Ingrese el DNI del usuario -> ")

    try:
        with engine.begin() as conn:
            query = f"UPDATE libros SET Estado = 'libre' WHERE Libro = '{libro_reserva}'"
            conn.exec_driver_sql(query)
            return f"EL LIBRO {libro_reserva} HA SIDO DEVUELTO"

    except Exception as e:
        return f"Ocurrió un error: {e}"
 
#FUNCIÓN PARA ELIMINAR UN LIBRO DEL CATÁLOGO, SE SOLICITA EL NOMBRE DEL MISMO Y SE RETORNA
# UN MENSAJE DICIENDO QUE EL LIBRO SE ELIMINÓ           
def eliminar_libros():
            print("\tELIMINAR LIBROS DEL LISTADO\n")
            libro_reserva = input("Ingrese el libro a eliminar -> ")
            eliminar = ControlStock("Libro","libros")
            if eliminar.delete(libro_reserva):
                return f"EL LIBRO {libro_reserva} HA SIDO ELIMINADO DEL CATÁLOGO"

#FUNCIÓN PARA ELIMINAR UN USUARIO DEL LISTADO, SE SOLICITA EL DNI DEL MISMO Y SE RETORNA
# UN MENSAJE DICIENDO QUE EL USUARIO SE ELIMINÓ       
def eliminar_usuario():
            print("\tELIMINAR USUARIOS DEL LISTADO\n")
            usuario = input("Ingrese el DNI del usuaio a eliminar -> ")
            eliminar = ControlStock("DNI_Usuario","usuarios")
            if eliminar.delete(usuario):
                return f"EL USUARIO {usuario} HA SIDO ELIMINADO DEL LISTADO"

#FUNCIÓN DEL MENÚ DE ESTADÍSTICAS, CUANDO SE ELIJE ESTA OPCIÓN SE ABRE UN MENÚ INDICANDO QUE INFORMACIÓN QUEREMOS VER
# SEGÚN LA OPCIÓN  ELEGIDA, LLAMA A LA FUNCIÓN QUE CORRESPONDE DEL MÓDULO DE funciones_estadisticas        
def estadisticas():
        print("\tMENÚ DE DATOS ESTADÍSTICOS\n¿Qué desea ver?\n1 - Libros más alquilados\n2 - Meses con mayores alquileres históricamente\n3 - Usuarios que más alquileres realizaron\n4 - Reservas 2024\n5 - Reservas 2025\n6 - Comparar reservas del 2024 y 2025\n")
        
        opcion = input("-> ")
        match opcion:
            case "1":
                fm.libros_mas_alquilados()
                os.system('cls')
            case "2":
                fm.meses_mas_alquilados()
                os.system('cls')
            case "3":
                fm.usuarios_alquilados()
                os.system('cls')
            case "4":
                fm.ver_2024()
                os.system('cls')
            case "5":
                fm.ver_2025()
                os.system('cls')
            case "6":
                fm.comparar_years()
                os.system('cls')
            case "s":
                os.system('cls')
                return "s"
 
#FUNCIÓN PARA VER LAS RESERVAS ACTUALES, SI NO HAY RESERVAS ACTUALES, DEVUELVE UN MENSAJE INFORMÁNDOLO.
def ver_reservas():
    print("\tRESERVAS ACTUALES\n")
    try:
        with engine.connect() as conn:
            fecha = datetime.now().date()
            fecha_string = fecha.strftime('%Y-%m-%d')

            query = f"SELECT * FROM reservas WHERE Fecha_devolucion >= '{fecha_string}'"
            result = conn.exec_driver_sql(query).fetchall()
            if len(result) == 0:
                return "No hay reservas en este momento."
            reservas = []
            for fila in result:
                reserva_obj = cl.Reserva(
                    fila[0],   # id_reserva
                    fila[2],   # id_libro
                    fila[1],   # dni
                    str(fila[3]),  # fecha_salida
                    str(fila[4])   # devolucion
                )
                reservas.append(reserva_obj)

            return reservas

    except Exception as e:
        return f"Ocurrió un error: {e}"

#FUNCIÓN PARA SALIR DEL SISTEMA, PREGUNTA SI DE VERDAD DESEA SALIR, SI ES ASÍ IMPRIME UN MENSAJE Y CORTA LA EJECUCIÓN        
def salir():
            #PREGUNTAR SI DE VERDAD DESEA SALIR, CREAR VARIABLE PARA TRABAJAR CON ESA VERIFICACION
            print("\tSALIENDO DEL SISTEMA\n      ¿DE VERDAD DESEA SALIR?\n\t       (S/N)")
            opcion = input(" -> ")
            if opcion.lower() == "s":
                os.system('cls')
                print("\tSALIENDO DEL SISTEMA, HASTA LUEGO")
                return opcion
            else:
                os.system('cls')
                return "n"
