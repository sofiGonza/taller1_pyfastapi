from models import trainee_model
from template import trainee_template

def init_app_data():
    """Inicializa los datos de la aplicacion, creando la tabla de aprendices si no existe"""
    trainee_model.load_data()

def register_trainee_view():
    data = trainee_template.get_trainee_input()

    if trainee_model.register_trainee(data):
        trainee_template.show_register_success()
    else:
        trainee_template.show_register_error()


def status_view():
    """Muestra el estado actual de los aprendices registrados"""

    trainees = trainee_model.get_all()

    if len(trainees) == 0:
        print("\nNo hay aprendices registrados.")
        return

    print("\n=== APRENDICES REGISTRADOS ===")

    for trainee in trainees:
        print(trainee)