import os
import uuid
import pytest
import requests


@pytest.fixture(scope="session")
def base_url():

    """
    Se obtiene la URL base desde la variable de entorno.
    
    """

    return os.getenv("API_BASE_URL", "http://localhost:8080")


@pytest.fixture
def producto_valido():

    """
    Genra un producto unico para evitar conflictos entre ejecuciones de pruebas.
    
    """
    return {
        "name": f"Producto QA {uuid.uuid4()}",
        "price": 100,
        "stock": 10
    }

@pytest.fixture
def crear_producto(base_url, producto_valido):
    response = requests.post(f"{base_url}/api/products", json=producto_valido)
    producto = response.json()

    yield producto

    if "id" in producto:
        requests.delete(f"{base_url}/api/products/{producto['id']}")