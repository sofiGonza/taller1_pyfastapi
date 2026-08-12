#Importamos asynccontextmanager 
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from services.rick_morty_api import get_random_character
from views import trainee_view


#importamos el modelo del aprendiz
from models import trainee_model
from schemas import trainee_schema

#creamos el ciclo de vida de la aplicación y se elimina el on-event
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Ejecuta las tareas necesarias al iniciar la aplicación.
    """
    trainee_model.load_data()

    yield

    """
    Aquí se pueden colocar tareas para ejecutar
    cuando la aplicación se cierre.
    """

app = FastAPI(
    title="Rick and Morty Consumer API",
    description="API simple con FastAPI para consumir la API de Rick & Morty",
    version="1.0.0"
)


@app.get("/", tags=["Api de rick and morty"])
def home():
    """
    Endpoint principal de la API.
    """
    return {
        "message": "Bienvenido a la API de Rick & Morty con FastAPI. Visita /docs para ver la documentación interactiva."
    }


@app.get("/character/random", tags=["Api de rick and morty"])
async def read_random_character():
    """
    Obtiene un personaje aleatorio.
    """

    character = await get_random_character()

    if not character or "error" in character:
        raise HTTPException(
            status_code=500,
            detail="No se pudo obtener el personaje de la API externa."
        )

    return character


@app.get("/character/{character_id}", tags=["Api de rick and morty"])
async def read_character_by_id(character_id: int):
    """
    Obtiene un personaje por su ID.
    """

    if character_id < 1 or character_id > 826:
        raise HTTPException(
            status_code=400,
            detail="El ID del personaje debe estar entre 1 y 826."
        )

    character = await get_random_character(character_id=character_id)

    if not character or "error" in character:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró el personaje con ID {character_id}."
        )

    return character


def main():
    """
    Ejecuta el menú del CRUD de aprendices.
    """
    trainee_view.main_menu_controller()


if __name__ == "__main__":
    main()

# ============================================================
# ENDPOINTS PARA OBTENER INFORMACIÓN DE LOS APRENDICES
# ============================================================

# ============================================================
# OBTENER TODOS LOS APRENDICES
# ============================================================
 
@app.get("/trainees", tags=["trainees"])
def get_all_trainees():
    """
    Endpoint para obtener todos los aprendices registrados.
    """
    return trainee_model.get_all()

# ============================================================
# REGISTRAR APRENDIZ
# ============================================================

@app.post("/trainees", tags=["trainees"])
def create_trainee(trainee: trainee_schema.TraineeBase):
    """
    Registra un nuevo aprendiz.
    """

    # Verificar si el documento ya existe
    existing_trainee = trainee_model.search_by_document(
        trainee.documento
    )

    if existing_trainee:
        raise HTTPException(
            status_code=409,
            detail="El documento ya está registrado."
        )

    # Convertir el modelo Pydantic a diccionario
    trainee_data = trainee.model_dump()

    # Registrar el aprendiz
    registered = trainee_model.register_trainee(trainee_data)

    if not registered:
        raise HTTPException(
            status_code=400,
            detail="No fue posible registrar el aprendiz."
        )

    return {
        "message": "Aprendiz registrado correctamente.",
        "trainee": trainee_data
    }


# ============================================================
# EDITAR APRENDIZ
# ============================================================

@app.put("/trainees/{documento}", tags=["trainees"])
def update_trainee(
    documento: str,
    trainee: trainee_schema.TraineeBase
):
    """
    Modifica los datos de un aprendiz existente.
    """

    # Buscar el aprendiz
    existing_trainee = trainee_model.search_by_document(
        documento
    )

    if existing_trainee is None:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró un aprendiz con documento {documento}."
        )

    # Convertir los datos recibidos a diccionario
    updated_data = trainee.model_dump()

    # Actualizar aprendiz
    updated = trainee_model.update_trainee(
        documento,
        updated_data
    )

    if not updated:
        raise HTTPException(
            status_code=400,
            detail="No fue posible actualizar el aprendiz."
        )

    return {
        "message": "Aprendiz actualizado correctamente.",
        "trainee": updated_data
    }


# ============================================================
# ELIMINAR APRENDIZ
# ============================================================

@app.delete("/trainees/{documento}", tags=["trainees"])
def delete_trainee(documento: str):
    """
    Elimina un aprendiz existente mediante su documento.
    """

    # Verificar que el aprendiz exista
    existing_trainee = trainee_model.search_by_document(
        documento
    )

    if existing_trainee is None:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró un aprendiz con documento {documento}."
        )

    # Eliminar aprendiz
    deleted = trainee_model.delete_trainee(documento)

    if not deleted:
        raise HTTPException(
            status_code=400,
            detail="No fue posible eliminar el aprendiz."
        )

    return {
        "message": "Aprendiz eliminado correctamente.",
        "documento": documento
    }
# ============================================================
# GET - BUSCAR POR NOMBRE
# ============================================================

@app.get("/trainees/search/name/{nombre}", tags=["trainees"])
def search_trainee_by_name(nombre: str):
    """
    Busca aprendices por nombre.
    """

    results = trainee_model.search_by_name(nombre)

    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron aprendices con el nombre '{nombre}'."
        )

    return results


# ============================================================
# GET - BUSCAR POR FICHA
# ============================================================

@app.get("/trainees/search/group/{ficha}", tags=["trainees"])
def search_trainee_by_group(ficha: str):
    """
    Busca aprendices por número de ficha.
    """

    results = trainee_model.search_by_group(ficha)

    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron aprendices de la ficha '{ficha}'."
        )

    return results


# ============================================================
# GET - EXPORTAR A CSV
# ============================================================

@app.get("/trainees/export/csv", tags=["trainees"])
def export_trainees_csv():
    """
    Exporta la lista de aprendices a un archivo CSV.
    """

    try:

        path = trainee_model.export_to_csv()

        return FileResponse(
            path=path,
            media_type="text/csv",
            filename="trainee.csv"
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="No fue posible exportar los aprendices a CSV."
        )


# ============================================================
# MENÚ DEL CRUD POR CONSOLA
# ============================================================

def main():
    """
    Ejecuta el menú del CRUD de aprendices.
    """
    trainee_view.main_menu_controller()
