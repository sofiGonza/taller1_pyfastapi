import re

# Capa template: interfaz de usuario por consola para registrar aprendices

def validar_correo(correo):
    """
    Valida que el correo tenga un formato correcto.
    Ejemplo válido: usuario@correo.com
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None


def get_trainee_input():
    # Solicita los datos
    id = int(input("Número de documento: "))
    type_id = input("Tipo de documento (CC/TI/CE): ").strip().upper()
    name = input("Nombre completo: ").strip()
    group_code = int(input("Número de ficha: "))
    program = input("Programa de formación: ").strip()

    # Validación del correo
    while True:
        email = input("Correo electrónico: ").strip()
        if validar_correo(email):
            break
        else:
            print("❌ Correo inválido. Intente nuevamente.")

    return {
        "tipo_doc": type_id,
        "documento": id,
        "nombre": name,
        "correo": email,
        "ficha": group_code,
        "programa": program
    }

#funcion para editar aprendiz por documento
def get_document_to_edit():
    return int(input("\nIngrese el documento del aprendiz a editar: "))

#inicia la funcion para editar aprendiz
def get_updated_trainee(old):

    print("\n=== EDITAR APRENDIZ ===")
    print("Presione Enter para conservar el valor actual.\n")

    # Tipo de documento
    while True:
        tipo = input(f"Tipo de documento [{old['tipo_doc']}]: ").strip().upper()

        if tipo == "":
            tipo = old["tipo_doc"]
            break

        if tipo in ["CC", "TI", "CE"]:
            break

        print("❌ Solo se permite CC, TI o CE.")

    # Nombre
    nombre = input(f"Nombre [{old['nombre']}]: ").strip()
    if nombre == "":
        nombre = old["nombre"]

    # Correo
    while True:
        correo = input(f"Correo [{old['correo']}]: ").strip()

        if correo == "":
            correo = old["correo"]
            break

        if validar_correo(correo):
            break

        print("❌ Correo inválido.")

    # Ficha
    ficha = input(f"Ficha [{old['ficha']}]: ").strip()
    if ficha == "":
        ficha = old["ficha"]
    else:
        ficha = int(ficha)

    # Programa
    programa = input(f"Programa [{old['programa']}]: ").strip()
    if programa == "":
        programa = old["programa"]

    return {
        "tipo_doc": tipo,
        "documento": old["documento"],
        "nombre": nombre,
        "correo": correo,
        "ficha": ficha,
        "programa": programa
    }
# Funciones para mostrar mensajes de éxito o error

def show_edit_success():
    print("\n✅ Aprendiz actualizado correctamente.")


def show_edit_error():
    print("\n❌ No existe un aprendiz con ese documento.")

def show_register_success():
    print("\n✅ Aprendiz registrado correctamente.")


def show_register_error():
    print("\n❌ El documento ya se encuentra registrado.")


def show_all_trainees(trainees):
    print("\n===== APRENDICES REGISTRADOS =====")

    if len(trainees) == 0:
        print("No hay aprendices registrados.")
        return

    for trainee in trainees:
        print("---------------------------")
        print("Tipo Documento:", trainee["tipo_doc"])
        print("Documento:", trainee["documento"])
        print("Nombre:", trainee["nombre"])
        print("Correo:", trainee["correo"])
        print("Ficha:", trainee["ficha"])
        print("Programa:", trainee["programa"])
        
# Funciones para eliminar aprendices
def get_document_to_delete():
    return int(input("\nIngrese el documento del aprendiz a eliminar: "))

# Funciones para mostrar mensajes de éxito o error al eliminar aprendices
def show_delete_success():
    print("\n✅ Aprendiz eliminado correctamente.")


def show_delete_error():
    print("\n❌ No existe un aprendiz con ese documento.")
    
# Funciones para buscar aprendices
def get_search_option():
    print("\n=== BUSCAR APRENDIZ ===")
    print("1. Buscar por nombre")
    print("2. Buscar por ficha")

    return input("Seleccione una opción: ")

# Funciones para obtener los criterios de búsqueda
def get_name_search():
    return input("Ingrese el nombre a buscar: ").strip()


def get_group_search():
    return int(input("Ingrese el número de ficha: "))

# Funciones para mostrar los resultados de búsqueda
def show_search_results(results):

    if len(results) == 0:
        print("\n❌ No se encontraron aprendices.")
        return

    print("\n===== RESULTADOS =====")

    for trainee in results:
        print("----------------------------")
        print("Tipo Documento:", trainee["tipo_doc"])
        print("Documento:", trainee["documento"])
        print("Nombre:", trainee["nombre"])
        print("Correo:", trainee["correo"])
        print("Ficha:", trainee["ficha"])
        print("Programa:", trainee["programa"])

# Funciones para exportar aprendices a CSV
def show_export_success(path):
    print(f"\n✅ Datos exportados correctamente.")
    print(f"📄 Archivo generado: {path}")
    
def show_export_error():
    print("\n❌ No fue posible exportar los datos.")

def display_confirm_next():
    respuesta = input("\n¿Desea registrar otro aprendiz? (S/N): ").strip().upper()
    return respuesta == "S"