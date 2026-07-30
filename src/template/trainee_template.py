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


def display_confirm_next():
    respuesta = input("\n¿Desea registrar otro aprendiz? (S/N): ").strip().upper()
    return respuesta == "S"