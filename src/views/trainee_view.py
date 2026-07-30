from models import trainee_model
from template import trainee_template


#funcion para inicializar los datos de la aplicacion
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
 
 #funcion para editar aprendiz       
def edit_trainee_view():

    document = trainee_template.get_document_to_edit()

    trainee = trainee_model.search_by_document(document)

    if trainee is None:
        trainee_template.show_edit_error()
        return

    updated = trainee_template.get_updated_trainee(trainee)

    trainee_model.update_trainee(document, updated)

    trainee_template.show_edit_success()
    
 #funcion para eliminar aprendiz   
def delete_trainee_view():

    document = trainee_template.get_document_to_delete()

    if trainee_model.delete_trainee(document):
        trainee_template.show_delete_success()
    else:
        trainee_template.show_delete_error()
        
# funcion para buscar aprendiz
def search_trainee_view():

    option = trainee_template.get_search_option()

    if option == "1":

        name = trainee_template.get_name_search()

        results = trainee_model.search_by_name(name)

        trainee_template.show_search_results(results)

    elif option == "2":

        group = trainee_template.get_group_search()

        results = trainee_model.search_by_group(group)

        trainee_template.show_search_results(results)

    else:
        print("\n❌ Opción inválida.")

#funcion para exportar aprendices a CSV
def export_csv_view():

    try:
        path = trainee_model.export_to_csv()
        trainee_template.show_export_success(path)

    except Exception:
        trainee_template.show_export_error()