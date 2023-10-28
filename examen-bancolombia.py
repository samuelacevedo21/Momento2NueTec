class Empleado:
    def __init__(self, id, nombre, apellido, cargo, area, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.salario = salario

class Nomina:
    def __init__(self, empleado, deducciones):
        self.empleado = empleado
        self.deducciones = deducciones
        self.auxilio_transporte = 0

    def calcular_salario_neto(self):
        if self.empleado.salario <= 2000000:
            self.auxilio_transporte = 117000
        salario_neto = self.empleado.salario - self.deducciones + self.auxilio_transporte
        return salario_neto

empleados = {}
nominas = []

def registrar_empleado():
    id = input("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    area = input("Ingrese el área del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    empleado = Empleado(id, nombre, apellido, cargo, area, salario)
    empleados[id] = empleado

def iniciar_sesion():
    id = input("Ingrese su ID de empleado: ")
    area = input("Ingrese su área: ")

    if id in empleados and area == "Recursos Humanos" == "":
        return True
    else:
        print("Error: El ID o el área no coinciden.")
        return False

def ingresar_nomina():
    if iniciar_sesion():
        id_empleado = input("Ingrese el ID del empleado para registrar la nómina: ")
        if id_empleado in empleados:
            deducciones = float(input("Ingrese las deducciones del empleado: "))
            nomina = Nomina(empleados[id_empleado], deducciones)
            nominas.append(nomina)
            print("Nómina registrada con éxito.")
        else:
            print("Error: El ID del empleado no existe.")

def buscar_colilla_nomina():
    id_empleado = input("Ingrese el ID del empleado para buscar la colilla de nómina: ")
    for nomina in nominas:
        if nomina.empleado.id == id_empleado:
            salario_neto = nomina.calcular_salario_neto()
            print(f"Colilla de Nómina para {nomina.empleado.nombre} {nomina.empleado.apellido}:")
            print(f"Salario Bruto: {nomina.empleado.salario}")
            print(f"Deducciones: {nomina.deducciones}")
            print(f"Auxilio de Transporte: {nomina.auxilio_transporte}")
            print(f"Salario Neto: {salario_neto}")
            return
    print("Error: El empleado no tiene una colilla de nómina registrada.")

while True:
    print("\nMenú Principal:")
    print("1. Registrar Empleado")
    print("2. Iniciar Sesión")
    print("3. Ingresar Nómina")
    print("4. Buscar Colilla de Nómina")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_empleado()
    elif opcion == "2":
        if iniciar_sesion():
            print("Sesión iniciada con éxito.")
    elif opcion == "3":
        ingresar_nomina()
    elif opcion == "4":
        buscar_colilla_nomina()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
