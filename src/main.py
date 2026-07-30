from views import trainee_view
from template import trainee_template

def main():

    trainee_view.init_app_data()

    while True:

        print("\n===== MENU =====")
        print("1. Registrar aprendiz ✏️")
        print("2. Listar aprendices 📋")
        print("3. Editar aprendiz 📝")
        print("4. Eliminar aprendiz ❌")
        print("5. Buscar aprendiz 🔍")
        print("6. Exportar a CSV 📤")
        print("7. Salir 🚪")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            trainee_view.register_trainee_view()

        elif opcion == "2":
            trainee_view.status_view()

        elif opcion == "3":
            trainee_view.edit_trainee_view()

        elif opcion == "4":
            trainee_view.delete_trainee_view()

        elif opcion == "5":
            trainee_view.search_trainee_view()

        elif opcion == "6":
            trainee_view.export_csv_view()

        elif opcion == "7":
            print("Saliendo del programa ¡Hasta luego!")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
    