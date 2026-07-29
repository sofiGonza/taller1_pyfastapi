#capa template: interfaz de usuario por consola para registrar aprendices

def get_trainee_input():
    #solicita los datos 
    id =input("Numero de documento:").strip()
    type_id=input("Tipo de documento (CC/TI/CE): ").strip()
    name=input("Nombre completo: ").strip()
    group_code=input("Numero de ficha:").strip()
    program= input("Programa de fomación: ").strip()

    return{
        "tipo_doc" : type_id,
        "documento": id,
        "nombre":name,
        "ficha": group_code,
        "Programa": program
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
        print("Tipo Documento:", trainee["type_document"])
        print("Documento:", trainee["id"])
        print("Nombre:", trainee["name"])

        print("Ficha:", trainee["group_code"])
        print("Programa:", trainee["program"])
        
def display_confirm_next():
    respuesta = input("\n¿Desea registrar otro aprendiz? (S/N): ").strip().upper()
    return respuesta == "S"