import pytest
from src.models import trainee_model


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Fixture que se ejecuta antes y después de cada prueba.
    Garantiza que la lista de aprendices esté vacía.
    """
    trainee_model.trainee.clear()

    yield

    trainee_model.trainee.clear()


# ==========================================
# PRUEBA 1: REGISTRO EXITOSO
# ==========================================

def test_register_trainee_success():

    # Arrange
    new_trainee = {
        "tipo_doc": "CC",
        "documento": 123456,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    }

    # Act
    result = trainee_model.register_trainee(new_trainee)

    # Assert
    assert result is True
    assert len(trainee_model.trainee) == 1
    assert trainee_model.trainee[0] == new_trainee


# ==========================================
# PRUEBA 2: DOCUMENTO DUPLICADO
# ==========================================

def test_register_trainee_duplicate():

    # Arrange
    trainee = {
        "tipo_doc": "CC",
        "documento": 123456,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    }

    trainee_model.trainee.append(trainee)

    # Act
    result = trainee_model.register_trainee(trainee)

    # Assert
    assert result is False
    assert len(trainee_model.trainee) == 1


# ==========================================
# PRUEBA 3: BUSCAR DOCUMENTO EXISTENTE
# ==========================================

def test_search_by_document_found():

    # Arrange
    trainee = {
        "tipo_doc": "CC",
        "documento": 123456,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    }

    trainee_model.trainee.append(trainee)

    # Act
    result = trainee_model.search_by_document(123456)

    # Assert
    assert result == trainee


# ==========================================
# PRUEBA 4: BUSCAR DOCUMENTO INEXISTENTE
# ==========================================

def test_search_by_document_not_found():

    # Arrange
    document = 999999

    # Act
    result = trainee_model.search_by_document(document)

    # Assert
    assert result is None


# ==========================================
# PRUEBA 5: ACTUALIZAR APRENDIZ
# ==========================================

def test_update_trainee():

    # Arrange
    trainee = {
        "tipo_doc": "CC",
        "documento": 123456,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    }

    trainee_model.trainee.append(trainee)

    updated = {
        "tipo_doc": "CC",
        "documento": 123456,
        "nombre": "Juan David Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876502,
        "programa": "ADSO"
    }

    # Act
    result = trainee_model.update_trainee(123456, updated)

    # Assert
    assert result is True
    assert trainee_model.trainee[0]["nombre"] == "Juan David Perez"
    assert trainee_model.trainee[0]["ficha"] == 2876502


# ==========================================
# PRUEBA 6: ELIMINAR APRENDIZ
# ==========================================

def test_delete_trainee():

    # Arrange
    trainee = {
        "tipo_doc": "CC",
        "documento": 123456,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    }

    trainee_model.trainee.append(trainee)

    # Act
    result = trainee_model.delete_trainee(123456)

    # Assert
    assert result is True
    assert len(trainee_model.trainee) == 0


# ==========================================
# PRUEBA 7: BUSCAR POR NOMBRE
# ==========================================

def test_search_by_name():

    # Arrange
    trainee_model.trainee.append({
        "tipo_doc": "CC",
        "documento": 1,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 100,
        "programa": "ADSO"
    })

    trainee_model.trainee.append({
        "tipo_doc": "CC",
        "documento": 2,
        "nombre": "Maria Lopez",
        "correo": "maria@gmail.com",
        "ficha": 200,
        "programa": "ADSO"
    })

    # Act
    result = trainee_model.search_by_name("Juan")

    # Assert
    assert len(result) == 1
    assert result[0]["nombre"] == "Juan Perez"


# ==========================================
# PRUEBA 8: BUSCAR POR FICHA
# ==========================================

def test_search_by_group():

    # Arrange
    trainee_model.trainee.append({
        "tipo_doc": "CC",
        "documento": 1,
        "nombre": "Juan Perez",
        "correo": "juan@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    })

    trainee_model.trainee.append({
        "tipo_doc": "CC",
        "documento": 2,
        "nombre": "Maria Lopez",
        "correo": "maria@gmail.com",
        "ficha": 2876501,
        "programa": "ADSO"
    })

    # Act
    result = trainee_model.search_by_group(2876501)

    # Assert
    assert len(result) == 2
    assert result[0]["ficha"] == 2876501
    assert result[1]["ficha"] == 2876501