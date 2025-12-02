#	Definimos clases para Libro, Autor, Usuario, Biblioteca.
#	Define métodos que representen acciones (por ejemplo, Biblioteca podría tener métodos para agregar_libro, prestar_libro, devolver_libro, buscar_libro).
class Biblioteca():
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.libros = []
        self.usuarios = []
        
    def __str__(self):
        return f"Título: {self.nombre}, Autor: {self.nombre}, Estado: {self.ubicacion}"
    
    def ver_libros(self):
        return [libro for libro in self.libros]
        
    def agregar_libro(self,info_libro):
        self.libros.append(info_libro)
        #self.libros.sort(key=lambda libro: libro.nombre)
        return "LIBRO AGREGADO"
        
    def agregar_usuario(self,info_usuario):
        self.usuarios.append(info_usuario)
        
    def buscar_libro(self, libro):
        self.libros.sort(key=lambda libro: libro.nombre)
        l = 0
        r = len(self.libros) - 1
        while l <= r:
            m = (l+r) // 2
            if libro == self.libros[m].nombre:
                return self.libros[m]
            elif libro < self.libros[m].nombre:
                r = m-1
            else:
                l = m+1
        #if l>r:
        return None
    
    def buscar_usuario(self, usuario):
        self.usuarios.sort(key=lambda usuario: usuario.nombre)
        l = 0
        r = len(self.usuarios) - 1
        while l <= r:
            m = (l+r) // 2
            if usuario == self.usuarios[m].nombre:
                return self.usuarios[m]
                    #f"LIBRO -> {self.libros[m].nombre} \nAUTOR -> {self.libros[m].autor} \nESTADO -> {self.libros[m].estado}"
            elif usuario < self.usuarios[m].nombre:
                r = m-1
            else:
                l = m+1
        return None
        
    
    def alquilar_libro(self,libro,usuario):
        resultado_busqueda = self.buscar_libro(libro)
        resultado_usuario = self.buscar_usuario(usuario)
        if resultado_busqueda and resultado_usuario:
            if resultado_busqueda.estado == "ALQUILADO":
                return "El libro ya está alquilado"
            else:
                resultado_busqueda.estado = "ALQUILADO"
                resultado_usuario.libros_retirados.append(resultado_busqueda.nombre)
           
        
    
    def devoler_libro(self,libro,usuario):
        resultado_busqueda = self.buscar_libro(libro)
        resultado_usuario = self.buscar_usuario(usuario)
        if resultado_busqueda and resultado_usuario:
            resultado_busqueda.estado = "LIBRE"
            resultado_usuario.libros_retirados.remove(resultado_busqueda.nombre)

class Usuario():
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.libros_retirados = []
        
    def __str__(self):
        return f"Usuario: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}, Libros retirados: {self.libros_retirados}"
    
    def __repr__(self):
        return f"Usuario(id='{self.id}', nombre='{self.nombre}', direccion='{self.direccion}')"
    
class Autor():
    def __init__(self, id, nombre, libros=[], pais=""):
        self.id = id
        self.nombre = nombre
        self.cant = libros
        self.pais = pais
        
    def __str__(self):
        return f"Autor: {self.id}, Nombre: {self.nombre}, Pais: {self.pais}, Libros escritos: {self.libros}"
    
    
    def __repr__(self):
        return f"Autor(id='{self.id}', nombre='{self.nombre}', pais='{self.pais}')"  
    
class Libro():
    def __init__(self, nombre, autor, estado):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        
        
    def __str__(self):
        return f"Título: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}"
    
    def __repr__(self):
        return f"Libro(nombre='{self.nombre}', autor='{self.autor}', estado='{self.estado}')"
    
#LISTAS DE INFORMACIÓN SIMULADA PARA INSERTAR EN LA BASE DE DATOS Y PODER REALIZAR LAS ACCIONES DEL MENÚ
lista_de_listas_libros = [
    [1, "Cien años de soledad", "Gabriel García Márquez", "libre"],
    [2, "Orgullo y prejuicio", "Jane Austen", "libre"],
    [3, "1984", "George Orwell", "libre"],
    [4, "El Gran Gatsby", "F. Scott Fitzgerald", "libre"],
    [5, "Don Quijote de la Mancha", "Miguel de Cervantes", "libre"],
    [6, "Matar a un ruiseñor", "Harper Lee", "libre"],
    [7, "Crimen y castigo", "Fiódor Dostoyevski", "libre"],
    [8, "El Señor de los Anillos", "J.R.R. Tolkien", "libre"],
    [9, "Harry Potter y la piedra filosofal", "J.K. Rowling", "libre"],
    [10, "El Principito", "Antoine de Saint-Exupéry", "libre"],
    [11, "Los juegos del hambre", "Suzanne Collins", "libre"],
    [12, "El código Da Vinci", "Dan Brown", "libre"],
    [13, "La Odisea", "Homero", "libre"],
    [14, "Frankenstein", "Mary Shelley", "libre"],
    [15, "Drácula", "Bram Stoker", "libre"],
    [16, "El alquimista", "Paulo Coelho", "libre"],
    [17, "Mujercitas", "Louisa May Alcott", "libre"],
    [18, "Sherlock Holmes: Estudio en escarlata", "Arthur Conan Doyle", "libre"],
    [19, "La naranja mecánica", "Anthony Burgess", "libre"],
    [20, "Rebelión en la granja", "George Orwell", "libre"],
    [21, "Libro Genérico 21", "Autor Genérico 21", "libre"],
    [22, "Libro Genérico 22", "Autor Genérico 22", "libre"],
    [23, "Libro Genérico 23", "Autor Genérico 23", "libre"],
    [24, "Libro Genérico 24", "Autor Genérico 24", "libre"],
    [25, "Libro Genérico 25", "Autor Genérico 25", "libre"],
    [26, "Libro Genérico 26", "Autor Genérico 26", "libre"],
    [27, "Libro Genérico 27", "Autor Genérico 27", "libre"],
    [28, "Libro Genérico 28", "Autor Genérico 28", "libre"],
    [29, "Libro Genérico 29", "Autor Genérico 29", "libre"],
    [30, "Libro Genérico 30", "Autor Genérico 30", "libre"],
    [31, "Libro Genérico 31", "Autor Genérico 31", "libre"],
    [32, "Libro Genérico 32", "Autor Genérico 32", "libre"],
    [33, "Libro Genérico 33", "Autor Genérico 33", "libre"],
    [34, "Libro Genérico 34", "Autor Genérico 34", "libre"],
    [35, "Libro Genérico 35", "Autor Genérico 35", "libre"],
    [36, "Libro Genérico 36", "Autor Genérico 36", "libre"],
    [37, "Libro Genérico 37", "Autor Genérico 37", "libre"],
    [38, "Libro Genérico 38", "Autor Genérico 38", "libre"],
    [39, "Libro Genérico 39", "Autor Genérico 39", "libre"],
    [40, "Libro Genérico 40", "Autor Genérico 40", "libre"],
    [41, "Libro Genérico 41", "Autor Genérico 41", "libre"],
    [42, "Libro Genérico 42", "Autor Genérico 42", "libre"],
    [43, "Libro Genérico 43", "Autor Genérico 43", "libre"],
    [44, "Libro Genérico 44", "Autor Genérico 44", "libre"],
    [45, "Libro Genérico 45", "Autor Genérico 45", "libre"],
    [46, "Libro Genérico 46", "Autor Genérico 46", "libre"],
    [47, "Libro Genérico 47", "Autor Genérico 47", "libre"],
    [48, "Libro Genérico 48", "Autor Genérico 48", "libre"],
    [49, "Libro Genérico 49", "Autor Genérico 49", "libre"],
    [50, "Libro Genérico 50", "Autor Genérico 50", "libre"],
    [51, "Libro Genérico 51", "Autor Genérico 51", "libre"],
    [52, "Libro Genérico 52", "Autor Genérico 52", "libre"],
    [53, "Libro Genérico 53", "Autor Genérico 53", "libre"],
    [54, "Libro Genérico 54", "Autor Genérico 54", "libre"],
    [55, "Libro Genérico 55", "Autor Genérico 55", "libre"],
    [56, "Libro Genérico 56", "Autor Genérico 56", "libre"],
    [57, "Libro Genérico 57", "Autor Genérico 57", "libre"],
    [58, "Libro Genérico 58", "Autor Genérico 58", "libre"],
    [59, "Libro Genérico 59", "Autor Genérico 59", "libre"],
    [60, "Libro Genérico 60", "Autor Genérico 60", "libre"],
    [61, "Libro Genérico 61", "Autor Genérico 61", "libre"],
    [62, "Libro Genérico 62", "Autor Genérico 62", "libre"],
    [63, "Libro Genérico 63", "Autor Genérico 63", "libre"],
    [64, "Libro Genérico 64", "Autor Genérico 64", "libre"],
    [65, "Libro Genérico 65", "Autor Genérico 65", "libre"],
    [66, "Libro Genérico 66", "Autor Genérico 66", "libre"],
    [67, "Libro Genérico 67", "Autor Genérico 67", "libre"],
    [68, "Libro Genérico 68", "Autor Genérico 68", "libre"],
    [69, "Libro Genérico 69", "Autor Genérico 69", "libre"],
    [70, "Libro Genérico 70", "Autor Genérico 70", "libre"],
    [71, "Libro Genérico 71", "Autor Genérico 71", "libre"],
    [72, "Libro Genérico 72", "Autor Genérico 72", "libre"],
    [73, "Libro Genérico 73", "Autor Genérico 73", "libre"],
    [74, "Libro Genérico 74", "Autor Genérico 74", "libre"],
    [75, "Libro Genérico 75", "Autor Genérico 75", "libre"],
    [76, "Libro Genérico 76", "Autor Genérico 76", "libre"],
    [77, "Libro Genérico 77", "Autor Genérico 77", "libre"],
    [78, "Libro Genérico 78", "Autor Genérico 78", "libre"],
    [79, "Libro Genérico 79", "Autor Genérico 79", "libre"],
    [80, "Libro Genérico 80", "Autor Genérico 80", "libre"],
    [81, "Libro Genérico 81", "Autor Genérico 81", "libre"],
    [82, "Libro Genérico 82", "Autor Genérico 82", "libre"],
    [83, "Libro Genérico 83", "Autor Genérico 83", "libre"],
    [84, "Libro Genérico 84", "Autor Genérico 84", "libre"],
    [85, "Libro Genérico 85", "Autor Genérico 85", "libre"],
    [86, "Libro Genérico 86", "Autor Genérico 86", "libre"],
    [87, "Libro Genérico 87", "Autor Genérico 87", "libre"],
    [88, "Libro Genérico 88", "Autor Genérico 88", "libre"],
    [89, "Libro Genérico 89", "Autor Genérico 89", "libre"],
    [90, "Libro Genérico 90", "Autor Genérico 90", "libre"],
    [91, "Libro Genérico 91", "Autor Genérico 91", "libre"],
    [92, "Libro Genérico 92", "Autor Genérico 92", "libre"],
    [93, "Libro Genérico 93", "Autor Genérico 93", "libre"],
    [94, "Libro Genérico 94", "Autor Genérico 94", "libre"],
    [95, "Libro Genérico 95", "Autor Genérico 95", "libre"],
    [96, "Libro Genérico 96", "Autor Genérico 96", "libre"],
    [97, "Libro Genérico 97", "Autor Genérico 97", "libre"],
    [98, "Libro Genérico 98", "Autor Genérico 98", "libre"],
    [99, "Libro Genérico 99", "Autor Genérico 99", "libre"],
    [100, "Libro Genérico 100", "Autor Genérico 100", "libre"]
]

lista_usuarios_con_correo = [
    [20000000, 'Ana', 'Pérez', 'Calle Falsa 1', 'ana.perez@email.com'],
    [20000001, 'Carlos', 'López', 'Calle Falsa 2', 'carlos.lopez@example.org'],
    [20000002, 'Sofía', 'Gómez', 'Calle Falsa 3', 'sofia.gomez@mail.net'],
    [20000003, 'Martín', 'Rodríguez', 'Calle Falsa 4', 'martin.rodriguez@domain.co'],
    [20000004, 'Laura', 'Vargas', 'Calle Falsa 5', 'laura.vargas@service.info'],
    [20000005, 'Javier', 'Soto', 'Calle Falsa 6', 'javier.soto@provider.ar'],
    [20000006, 'Valentina', 'Torres', 'Calle Falsa 7', 'valentina.torres@netmail.com'],
    [20000007, 'Gabriel', 'Ruiz', 'Calle Falsa 8', 'gabriel.ruiz@test.org'],
    [20000008, 'Camila', 'Castro', 'Calle Falsa 9', 'camila.castro@email.net'],
    [20000009, 'Pedro', 'Díaz', 'Calle Falsa 10', 'pedro.diaz@sample.co'],
    [20000010, 'Lucía', 'Fernández', 'Calle Falsa 11', 'lucia.fernandez@mail.info'],
    [20000011, 'Marcos', 'Núñez', 'Calle Falsa 12', 'marcos.nunez@domain.ar'],
    [20000012, 'Agustina', 'Flores', 'Calle Falsa 13', 'agustina.flores@netmail.com'],
    [20000013, 'Sebastián', 'Silva', 'Calle Falsa 14', 'sebastian.silva@example.org'],
    [20000014, 'Daniela', 'Romero', 'Calle Falsa 15', 'daniela.romero@service.net'],
    [20000015, 'Nicolás', 'Herrera', 'Calle Falsa 16', 'nicolas.herrera@provider.co'],
    [20000016, 'Emilia', 'Vargas', 'Calle Falsa 17', 'emilia.vargas@test.info'],
    [20000017, 'Facundo', 'Castro', 'Calle Falsa 18', 'facundo.castro@mail.ar'],
    [20000018, 'Renata', 'Díaz', 'Calle Falsa 19', 'renata.diaz@netmail.com'],
    [20000019, 'Joaquín', 'Fernández', 'Calle Falsa 20', 'joaquin.fernandez@sample.org']
]

lista_reservas = [
    [1, 20000005, 87, '2024-07-12', '2024-07-28'],
    [2, 20000012, 34, '2025-03-01', '2025-03-15'],
    [3, 20000001, 56, '2024-11-20', '2024-12-17'],
    [4, 20000018, 12, '2025-09-05', '2025-09-09'],
    [5, 20000009, 2, '2024-02-28', '2024-03-27'],
    [6, 20000015, 91, '2025-05-10', '2025-06-07'],
    [7, 20000003, 45, '2024-09-15', '2024-10-03'],
    [8, 20000019, 78, '2025-01-22', '2025-02-16'],
    [9, 20000007, 19, '2024-05-03', '2024-05-19'],
    [10, 20000011, 62, '2025-11-01', '2025-11-25'],
    [11, 20000002, 25, '2024-12-08', '2025-01-05'],
    [12, 20000016, 98, '2025-07-18', '2025-08-16'],
    [13, 20000006, 3, '2024-03-22', '2024-04-18'],
    [14, 20000013, 51, '2025-02-10', '2025-03-03'],
    [15, 20000008, 81, '2024-10-29', '2024-11-27'],
    [16, 20000017, 7, '2025-08-25', '2025-09-14'],
    [17, 20000004, 40, '2024-06-05', '2024-06-16'],
    [18, 20000010, 68, '2025-04-01', '2025-04-29'],
    [19, 20000014, 15, '2024-01-15', '2024-02-07'],
    [20, 20000000, 95, '2025-12-10', '2026-01-03'],
    [21, 20000019, 22, '2024-08-01', '2024-08-29'],
    [22, 20000007, 59, '2025-06-20', '2025-07-18'],
    [23, 20000012, 88, '2024-04-10', '2024-05-05'],
    [24, 20000002, 30, '2025-03-15', '2025-04-12'],
    [25, 20000016, 4, '2024-11-05', '2024-11-23'],
    [26, 20000005, 71, '2025-09-20', '2025-10-15'],
    [27, 20000010, 18, '2024-07-25', '2024-08-20'],
    [28, 20000000, 65, '2025-01-05', '2025-01-29'],
    [29, 20000014, 99, '2024-05-20', '2024-06-12'],
    [30, 20000003, 28, '2025-11-15', '2025-12-08'],
    [31, 20000018, 48, '2024-09-01', '2024-09-25'],
    [32, 20000006, 84, '2025-07-01', '2025-07-23'],
    [33, 20000011, 11, '2024-02-10', '2024-03-05'],
    [34, 20000001, 54, '2025-04-15', '2025-05-10'],
    [35, 20000015, 37, '2024-12-20', '2025-01-18'],
    [36, 20000009, 75, '2025-08-10', '2025-09-02'],
    [37, 20000004, 21, '2024-03-01', '2024-03-25'],
    [38, 20000017, 61, '2025-02-25', '2025-03-20'],
    [39, 20000013, 92, '2024-10-15', '2024-11-10'],
    [40, 20000008, 33, '2025-05-25', '2025-06-18'],
    [41, 20000019, 42, '2024-06-20', '2024-07-15'],
    [42, 20000007, 79, '2025-01-10', '2025-02-05'],
    [43, 20000012, 1, '2024-08-15', '2024-09-08'],
    [44, 20000002, 58, '2025-10-05', '2025-10-28'],
    [45, 20000016, 85, '2024-04-25', '2024-05-20'],
    [46, 20000005, 14, '2025-03-25', '2025-04-19'],
    [47, 20000010, 49, '2024-11-25', '2024-12-20'],
    [48, 20000000, 72, '2025-09-01', '2025-09-29'],
    [49, 20000014, 29, '2024-07-01', '2024-07-26'],
    [50, 20000003, 66, '2025-01-25', '2025-02-20'],
    [51, 20000018, 93, '2024-05-10', '2024-06-04'],
    [52, 20000006, 36, '2025-11-20', '2025-12-15'],
    [53, 20000011, 6, '2024-09-10', '2024-10-05'],
    [54, 20000001, 43, '2025-07-05', '2025-07-30'],
    [55, 20000015, 82, '2024-02-20', '2024-03-16'],
    [56, 20000009, 17, '2025-04-20', '2025-05-15'],
    [57, 20000004, 52, '2024-12-25', '2025-01-22'],
    [58, 20000017, 89, '2025-08-15', '2025-09-09'],
    [59, 20000013, 24, '2024-06-25', '2024-07-20'],
    [60, 20000008, 69, '2025-02-01', '2025-02-26'],
    [61, 20000019, 39, '2024-10-01', '2024-10-26'],
    [62, 20000007, 76, '2025-05-01', '2025-05-26'],
    [63, 20000012, 9, '2024-03-10', '2024-04-04'],
    [64, 20000002, 46, '2025-11-05', '2025-11-30'],
    [65, 20000016, 86, '2024-07-05', '2024-07-30'],
    [66, 20000005, 23, '2025-09-10', '2025-10-05'],
    [67, 20000010, 63, '2024-01-20', '2024-02-14'],
    [68, 20000000, 31, '2025-06-25', '2025-07-20'],
    [69, 20000014, 70, '2024-08-20', '2024-09-14'],
    [70, 20000003, 16, '2025-04-05', '2025-04-30'],
    [71, 20000018, 53, '2024-12-01', '2024-12-26'],
    [72, 20000006, 96, '2025-08-20', '2025-09-14'],
    [73, 20000011, 26, '2024-04-15', '2024-05-10'],
    [74, 20000001, 67, '2025-02-15', '2025-03-12'],
    [75, 20000015, 41, '2024-11-10', '2024-12-05'],
    [76, 20000009, 77, '2025-05-15', '2025-06-09'],
    [77, 20000004, 8, '2024-09-25', '2024-10-20'],
    [78, 20000017, 47, '2025-03-05', '2025-03-30'],
    [79, 20000013, 83, '2024-07-20', '2024-08-14'],
    [80, 20000008, 20, '2025-01-15', '2025-02-09'],
    [81, 20000019, 57, '2024-05-01', '2024-05-26'],
    [82, 20000007, 90, '2025-10-10', '2025-11-04'],
    [83, 20000012, 32, '2024-02-05', '2024-03-01'],
    [84, 20000002, 64, '2025-06-05', '2025-06-30'],
    [85, 20000016, 13, '2024-12-15', '2025-01-09'],
    [86, 20000005, 50, '2025-08-05', '2025-08-30'],
    [87, 20000010, 80, '2024-04-01', '2024-04-26'],
    [88, 20000000, 5, '2025-02-20', '2025-03-17'],
    [89, 20000014, 38, '2024-10-05', '2024-10-30'],
    [90, 20000003, 73, '2025-05-20', '2025-06-14'],
    [91, 20000018, 27, '2024-06-10', '2024-07-05'],
    [92, 20000006, 60, '2025-12-05', '2026-01-02'],
]



