import json
import os
# Base de datos en memoria (lista vacía al inicio)
#Base de datos en archivo json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATABASE_FILE = os.path.join(DATA_DIR, "trainee.json")
trainee = []
def ensure_data_file_exists():
   if os.path.exists(DATABASE_FILE):
           os.makedirs(os.path.dirname(DATABASE_FILE), exist_ok=True)
           with open(DATABASE_FILE,"w",encoding="utf-8") as file:
               json.dump([],file) #Inicializa con una lista vacia
               
def load_data():
    """Carga los datos de aprendices desde el archivo JSON."""
    global trainee

    # Crear la carpeta data si no existe
    os.makedirs(DATA_DIR, exist_ok=True)

    # Crear el archivo si no existe
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        trainee = []
        return

    # Leer los datos
    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            trainee = json.load(file)
    except json.JSONDecodeError:
        trainee = []
    
def save_data():
    """Guarda los datos de aprendices en el archivo JSON."""
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(trainee, file, indent=4, ensure_ascii=False)
        
def get_all():
    """Obtiene todos los aprendices"""
    return trainee


def search_by_document(document):
    """Buscar un aprendiz por número de documento"""
    for a in trainee:
        if a["documento"] == document:
            return a
    return None


def register_trainee(new_trainee):
    """Registrar un nuevo aprendiz"""
    if search_by_document(new_trainee["documento"]):
        return False
    trainee.append(new_trainee)
    save_data()
    return True
#Funcion para editar aprendiz
def update_trainee(document, new_data):
    """
    Actualiza la información de un aprendiz.
    """
    for i, trainee_data in enumerate(trainee):
        if trainee_data["documento"] == document:
            trainee[i] = new_data
            save_data()
            return True
    return False
#funcion para eliminar aprendiz
def delete_trainee(document):
    """
    Elimina un aprendiz por número de documento.
    """
    for trainee_data in trainee:
        if trainee_data["documento"] == document:
            trainee.remove(trainee_data)
            save_data()
            return True
    return False

#funcion para buscar aprendiz por nombre
def search_by_name(name):
    """
    Busca aprendices por nombre.
    """
    results = []

    for trainee_data in trainee:
        if name.lower() in trainee_data["nombre"].lower():
            results.append(trainee_data)

    return results

#funcion para buscar aprendiz por ficha
def search_by_group(group_code):
    """
    Busca aprendices por número de ficha.
    """
    results = []

    for trainee_data in trainee:
        if trainee_data["ficha"] == group_code:
            results.append(trainee_data)

    return results