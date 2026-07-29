# Base de datos en memoria (lista vacía al inicio)


trainee = []

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
    return True