from views import trainee_view
from template import trainee_template

def main():
    while True:
        trainee_view.register_trainee_view()

        trainee_view.status_view()
        if not trainee_template.display_confirm_next():
            print("Saliendo del programa. ¡Hasta luego!")
            break
if __name__== "__main__":
    main()
    
        
