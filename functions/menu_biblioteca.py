
#ESTE ES EL ARCHIVO QUE CONTIENE EL MENU PRINCIPAL


#IMPORTAMOS EL MÓDULO OS Y FUNCIONES_MENU CUYAS FUNCIONES USAMOS SEGÚN LO QUE INGRESA EL USUARIO
import os
from funciones_menu import *

#DEFINIMOS LA VARIABLE SEGUIR, LA CUAL INDICARÁ SI EL USUARIO QUIERE SEGUIR USANDO EL SISTEMA O CERRALO, MIENTRAS SEA DISTINTA DE 'n' SE EJECUTARÁ
#EL BUCLE QUE CONTIENE TODAS LAS OPCIONES Y FUNCIONES
seguir = ""

#COMPRUEBA SI EL USUARIO QUIERE CONTINUAR, LA PRIMERA VEZ COMO SEGUIR NO TIENE NINGÚN VALOR, SE VA A EJECUTAR
while seguir.lower() != "n":
    
    #MOSTRAMOS EN PANTALLA UN MENSAJE DE BIENVENIDA JUNTO A TODAS LAS OPCIONES Y UNA FLECHA INDICANDO QUE INGRESE LA OPCIÓN EN ENSE LUGAR
    print("""\t   BIENVENIDO AL SISTEMA\n      ¿QUE OPERACIÓN DESEA RELAIZAR?\n\t1 -> Listar Libros/Usuarios\n\t2 -> Crear un nuevo usuario\n\t3 -> Agregar libro al stock\n\t4 -> Reservar libro\n\t5 -> Devolver libro\n\t6 -> Eliminar libro del listado\n\t7 -> Eliminar usuario\n\t8 -> Ver estadísticas\n\t9 -> Ver reservas actuales\n\t10 -> Salir""")

    #LA VARIABLE OPCIÓN ES LA FELCHA MENCIONADA ARRIBA Y SEGÚN ESTA OPCIÓN CREAMOS UN MATCH/CASE 
    operacion = input("\n -> ")
    
    #LIMPIAMOS LA CONSOLA
    os.system('cls')
    
    #SEGÚN OPERACIÓN
    match operacion:
        
        #SI ES 1, PREGUNTAMOS SI QUIERE LISTAR LIBROS O USUARIOS
        case "1":
            #EL USUARIO INGRESA QUE QUIERE LISTAR
            ver = input("¿Desea ver el listado de libros o usuarios? L/U -> ")
            
            #MIENTRAS LO QUE SE QUIERE LISTAR SEA DISTINTO DE 's' SE PREGUNTARÁ AL USUARIO QUE QUIERE LISTAR
            #ESTE BUCLE SIRVE PARA MANTENERNOS EN ESTA SECCIÓN DEL SISTEMA, SI INGRESA s en vez de L o U
            #INTERPRETAMOS QUE EL USUARIO QUIERE VOLVER AL MENÚ
            while ver != "s":
                #SI SE INGRESA 'L', LISTAMOS LOS LIBBROS
                if ver.lower() == 'l':
                    for libro in listar('l'):
                        print(libro)
                    ver = input("\n¿Desea ver el listado de libros o usuarios? L/U -> ")
                    
                #SI SE INGRESA 'U', LISTAMOS LOS USUARIOS
                elif ver.lower() == 'u':
                    print("\t\tUSUARIOS AFILIADOS")
                    for usuario in listar('u'):
                        print(usuario)
                    ver = input("\n¿Desea ver el listado de libros o usuarios? L/U -> ")
                
                #SI NO SE INGRESÓ 'L', 'U', 's', SIGNIFICA QUE ES UNA OPCIÓN INCORRECTA POR LO TANTO MOSTRAMOS LAS OPCIONES DISPONIBLES
                else:
                    print("Opción incorrecta, ingrese L (Libros), U (Usuarios) o s (volver al menú principal)")
                    ver = input("\n¿Desea ver el listado de libros o usuarios? L/U -> ")
                #SIEMPRE PREGUNTAMOS QUE SE DESEA LISTAR AL FINALIZAR UN LISTADO PARA VER SI EL USUARIO QUIERE REGRESAR O NO
            
            #LIMPIAMOS LA CONSOLA Y VOLVEMOS AL MENÚ PRINCIPAL, YA ESTAMOS FUERA DEL BUCLE ACÁ
            os.system('cls')
                
                    
        #SI ES 2, CREAMOS UN USUARIO         
        case "2":
            #CREAMOS VOLVER, QUE NOS AYUDA A EJECUTAR LA CREACIÓN DE UN USUARIO LAS VECES QUE SE QUIERA
            volver = ""
            while volver.lower() != "s":
                print(crear_usuario())
                #PREGUNTAMOS SI SE DESEA REGRESAR O NO
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
                #LIMPIAMOS PANTALLA
                os.system('cls')
            
        #SI ES 3, SE AGREGA UN LIBRO AL STOCK
        case "3":
            #ESTA OPCIÓN TRABAJA IGUAL QUE LA CREACIÓN DE USUARIOS PERO PIDE DATOS DE UN LIBRO EN VEZ DE UN USUARIO
            volver = ""
            while volver.lower() != "s":
                print(agregar_libro())
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
                #LIMPIAMOS PANTALLA
                os.system('cls')
        
        #SI ES 4, SE GUARDAN LAS RESERVAS DE UN LIBRO, TRABAJA IGUAL QUE EL CASO 2 Y 3 PERO CON DATOS DE RESERVA
        case "4":
            volver = ""
            while volver.lower() != "s":
                print(reservar_libros())
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
                os.system('cls')
            
        
        #SI ES 5, SE REGISTRA LA DEVOLUCIÓN DE UN LIBRO, TRABAJA IGUAL QUE LOS 3 CASOS ANTERIORES PERO PIDE DATOS DE DEVOLUCIÓN (LIBRO Y DNI DE USUARIO)
        case "5":
            volver = ""
            while volver.lower() != "s":
                print(devolver_libros())
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
                os.system('cls')
        
        #SI ES 6, ELIMINAMOS UN LIBRO DEL STOCK, LO DEMÁS IGUAL A LOS ANTERIORES, PIDE EL NOMBRE DEL LIBRO A ELIMINAR
        case "6":
            volver = ""
            while volver.lower() != "s":
                print(eliminar_libros())
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
                os.system('cls')
            
        #SI ES 7, SE ELIMINA A UN USUARIO DE LA BASE, PIDE EL DNI DEL USUARIO
        case "7":
            volver = ""
            while volver.lower() != "s":
                print(eliminar_usuario())
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
                os.system('cls')
            
        #SI ES 8, SE ABRE UN MENÚ CON LAS ESTADÍSTICAS QUE SE PUEDEN CONSULTAR, MIENTRAS QUE LA FUNCIÓN DE ESTADÍSTICAS NO DEVUWLVA 's', SE SEGUIRÁ MOSTRANDO EL MENÚ DE ESTADÍSTICAS
        case "8":
            volver = ""
            while estadisticas() != "s":
                estadisticas()
            
        #SI ES 9, LISTAMOS TODAS LAS RESERVAS ACTUALES
        case "9":
            volver = ""
            while volver.lower() != "s":
                resultado = ver_reservas()
                if not isinstance(resultado, list):
                    print("No hay reservas actuales")
                else:
                    for reserva in ver_reservas():
                        print(reserva)
                volver = input("¿Desea regresar al Menú? (S/N) -> ")
        
        #SI ES 10 Y LA FUNCIÓN SALIR DEVUELVE 's', SE CAMBIA EL VALOR DE LA VARIABLE CREADA AL PRINCIPIO LA CUAL SIRVE PARA QUE EL BUCLE SIGA A 'n' Y ESTO CUMPLE LA CONDICIÓN
        #PARA QUE EL BUCLE FINALICE Y SE SALGA DEL SISTEMA.
        case "10":
            if salir() == "s":
                seguir = "n"