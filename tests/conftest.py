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
    Genera un producto unico para evitar conflictos entre ejecuciones de pruebas.
    
    """
    return {
        "name": f"Producto QA {uuid.uuid4()}",
        "price": 100,
        "stock": 10
    }

@pytest.fixture
def producto_creado(base_url, producto_valido):

    """
    Setup: Crea un producto antes del test.

    Teardown: Elimina el producto al finalizar
    
    """
    response = requests.post(f"{base_url}/api/products", json=producto_valido)

    assert response.status_code == 201, (
        f"No se pudo crear un producto para el fixture."
        f"Status: {response.status_code}"
    )

    producto = response.json()

    yield producto

    #Teardown

    if producto.get("id"):
        requests.delete(f"{base_url}/api/products/{producto['id']}")



@pytest.fixture
def producto_actualizado():

     """
    PayLoad valido para pruebas de actualizacion
    
    """
     
     return {
         "name": "Producto Actualizado",
         "price": 150,
         "stock": 20
     }


@pytest.fixture
def id_inexistente():

     """
    ID que deberia no existir

    """
     return 99999