class Alumno:
    nombre = None
    apellido = None
    fecha_nacimiento = None
    dni = None
    tutor = None
    notas = []
    faltas = 0
    amonestaciones = 0

    @staticmethod
    def agregar_nota(nota):
        Alumno.notas.append(nota)

    @staticmethod
    def registrar_falta():
        Alumno.faltas += 1

    @staticmethod
    def recibir_amonestacion():
        Alumno.amonestaciones += 1

    @staticmethod
    def mostrar_datos():
        print("Nombre:", Alumno.nombre)
        print("Apellido:", Alumno.apellido)
        print("Fecha de Nacimiento:", Alumno.fecha_nacimiento)
        print("DNI:", Alumno.dni)
        print("Tutor:", Alumno.tutor)
        print("Notas:", Alumno.notas)
        print("Cantidad de Faltas:", Alumno.faltas)
        print("Cantidad de Amonestaciones:", Alumno.amonestaciones)


class Escuela:
    alumnos = []

    @staticmethod
    def agregar_alumno(alumno):
        Escuela.alumnos.append(alumno)

    @staticmethod
    def buscar_alumno_por_dni(dni):
        for alumno in Escuela.alumnos:
            if alumno.dni == dni:
                return alumno
        return None


# Uso del programa:

# Crear una instancia de la escuela
escuela = Escuela()

# Agregar alumnos a la escuela
alumno1 = Alumno()
alumno1.nombre = "Juan"
alumno1.apellido = "Perez"
alumno1.fecha_nacimiento = "2005-08-15"
alumno1.dni = "12345678"
alumno1.tutor = "Ana Martinez"

alumno2 = Alumno()
alumno2.nombre = "Maria"
alumno2.apellido = "Gomez"
alumno2.fecha_nacimiento = "2006-03-20"
alumno2.dni = "87654321"
alumno2.tutor = "Carlos Rodriguez"

Escuela.agregar_alumno(alumno1)
Escuela.agregar_alumno(alumno2)

# Registrar notas, faltas y amonestaciones para un alumno específico
Alumno.agregar_nota(9)
Alumno.agregar_nota(8)
Alumno.registrar_falta()
Alumno.recibir_amonestacion()

# Mostrar los datos de un alumno por DNI
alumno_buscado = Escuela.buscar_alumno_por_dni("12345678")
if alumno_buscado:
    Alumno.mostrar_datos()
else:
    print("Alumno no encontrado")
    

