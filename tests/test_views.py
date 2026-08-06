import pytest
from unittest.mock import patch
from src.views import trainee_view


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Se ejecuta antes y después de cada prueba.
    """
    yield


# ==========================
# REGISTRO EXITOSO
# ==========================

@patch("src.template.trainee_template.show_register_success")
@patch("src.models.trainee_model.register_trainee")
@patch("src.template.trainee_template.get_trainee_input")
def test_register_trainee_view_success(
    mock_input,
    mock_register,
    mock_success
):

    # Arrange
    trainee_data = {
        "tipo_doc": "CC",
        "documento": 12345,
        "nombre": "Juan Perez",
        "correo": "juan@sena.edu.co",
        "ficha": 2671234,
        "programa": "ADSO",
    }

    mock_input.return_value = trainee_data
    mock_register.return_value = True

    # Act
    trainee_view.register_trainee_view()

    # Assert
    mock_input.assert_called_once()
    mock_register.assert_called_once_with(trainee_data)
    mock_success.assert_called_once()


# ==========================
# REGISTRO DUPLICADO
# ==========================

@patch("src.template.trainee_template.show_register_error")
@patch("src.models.trainee_model.register_trainee")
@patch("src.template.trainee_template.get_trainee_input")
def test_register_trainee_view_duplicate(
    mock_input,
    mock_register,
    mock_error
):

    # Arrange
    trainee_data = {
        "tipo_doc": "CC",
        "documento": 12345,
        "nombre": "Juan Perez",
        "correo": "juan@sena.edu.co",
        "ficha": 2671234,
        "programa": "ADSO",
    }

    mock_input.return_value = trainee_data
    mock_register.return_value = False

    # Act
    trainee_view.register_trainee_view()

    # Assert
    mock_input.assert_called_once()
    mock_register.assert_called_once_with(trainee_data)
    mock_error.assert_called_once()


# ==========================
# LISTAR APRENDICES
# ==========================

@patch("builtins.print")
@patch("src.models.trainee_model.get_all")
def test_status_view(
    mock_get_all,
    mock_print
):

    # Arrange
    trainees = [
        {
            "tipo_doc": "CC",
            "documento": 1,
            "nombre": "Ana",
            "correo": "ana@gmail.com",
            "ficha": 2876501,
            "programa": "ADSO"
        },
        {
            "tipo_doc": "CC",
            "documento": 2,
            "nombre": "Carlos",
            "correo": "carlos@gmail.com",
            "ficha": 2876502,
            "programa": "ADSO"
        }
    ]

    mock_get_all.return_value = trainees

    # Act
    trainee_view.status_view()

    # Assert
    mock_get_all.assert_called_once()