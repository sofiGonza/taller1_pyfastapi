import httpx
import random

API_URL = "https://rickandmortyapi.com/api/character"


async def get_random_character(character_id: int = None):
    """
    Obtiene un personaje de la API de Rick and Morty.
    Si no se especifica un ID, selecciona uno aleatoriamente.
    """

    if character_id is None:
        random_id = random.randint(1, 826)
    else:
        random_id = character_id

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{API_URL}/{random_id}",
                timeout=5.0
            )

            if response.status_code == 200:
                data = response.json()

                return {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "species": data.get("species"),
                    "status": data.get("status"),
                    "image": data.get("image")
                }

    except Exception:
        pass

    return None