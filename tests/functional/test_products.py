import requests

# --------------------------------------------------------- GET TEST ------------------------------------------------------------------

def test_listar_productos(base_url):

    # Arrange
    url = f"{base_url}/api/products"

    #Act

    response = requests.get(url)

    #Assert
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obtener_producto_existente(base_url, producto_creado):

    # Arrange

    producto_id = producto_creado["id"]
    url = f"{base_url}/api/products/{producto_id}"
    
    #Act

    response = requests.get(url)

    #Assert

    assert response.status_code == 200
    data = response.json()
    assert data ["id"] == producto_id
    assert data["name"] == producto_creado["name"]

def test_obtener_producto_inexistente(base_url, id_inexistente):

    # Arrange

    url = f"{base_url}/api/products/{id_inexistente}"
    
    #Act

    response = requests.get(url)

    #Assert

    assert response.status_code == 404

def test_obtener_producto_id_invalido(base_url):
    # Arrange

    url = f"{base_url}/api/products/abc"
    
    #Act

    response = requests.get(url)

    #Assert

    assert response.status_code == 400

# --------------------------------------------------------- POST TEST ------------------------------------------------------------------


def test_crear_producto_exitoso(base_url, producto_valido):
    # Arrange

    url = f"{base_url}/api/products"
    
    #Act

    response = requests.post(url, json=producto_valido)

    #Assert

    assert response.status_code == 201
    data = response.json()
    assert data ["name"] == producto_valido["name"]
    assert data ["price"] == producto_valido["price"]
    assert data ["stock"] == producto_valido["stock"]

    requests.delete(f"{base_url}/api/products/{data['id']}")

def test_crear_producto_sin_nombre(base_url):
    # Arrange

    url = f"{base_url}/api/products"
    payload = {
        "price": 100,
        "stock": 10
    }
    
    #Act

    response = requests.post(url, json=payload)

    #Assert
    assert response.status_code == 400

def test_crear_producto_nombre_duplicado(base_url, producto_valido):
    # Arrange

    url = f"{base_url}/api/products"
    response_1 = requests.post(url, json=producto_valido)
    assert response_1.status_code == 201
    producto_id = response_1.json()["id"]
    
    #Act

    response_2 = requests.post(url, json=producto_valido)

    #Assert

    assert response_2.status_code in [400, 409]

    requests.delete(f"{base_url}/api/products/{producto_id}")

def test_crear_producto_precio_cero(base_url):
    # Arrange

    url = f"{base_url}/api/products"
    payload = {
        "name": "Producto Precio Cero",
        "price": 0,
        "stock": 5
    }
    
    #Act

    response = requests.post(url, json=payload)


    #Assert

    assert response.status_code == 400

def test_crear_producto_stock_negativo(base_url):
    # Arrange

    url = f"{base_url}/api/products"
    payload = {
        "name": "Producto Stock Negativo",
        "price": 100,
        "stock": -1
    }
    
    #Act

    response = requests.post(url, json=payload)

    #Assert

    assert response.status_code == 400

def test_crear_producto_nombre_100_caracteres(base_url):
    # Arrange

    url = f"{base_url}/api/products"
    payload = {
        "name": "A" * 100,
        "price": 100,
        "stock": 1
    }
    
    #Act
    response = requests.post(url, json=payload)

    #Assert
    assert response.status_code == 201

    data = response.json()
    requests.delete(f"{base_url}/api/products/{data['id']}")

def test_crear_producto_nombre_mayor_100_caracteres(base_url):
    # Arrange

    url = f"{base_url}/api/products"
    payload = {
        "name": "A" * 101,
        "price": 100,
        "stock": 1
    }
    
    #Act
    response = requests.post(url, json=payload)

    #Assert
    assert response.status_code == 400

# --------------------------------------------------------- PUT TEST ------------------------------------------------------------------

def test_actualizar_producto_existente(base_url, producto_creado, producto_actualizado):

    # Arrange

    producto_id = producto_creado["id"]
    url = f"{base_url}/api/products/{producto_id}"

    #Act
    
    response = requests.put(url, json=producto_actualizado)

    #Assert

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == producto_actualizado["name"]
    assert data["price"] == producto_actualizado["price"]
    assert data["stock"] == producto_actualizado["stock"]

def test_actualizar_producto_inexistente(base_url, id_inexistente, producto_actualizado):
    # Arrange

    url = f"{base_url}/api/products/{id_inexistente}"

    #Act
    response = requests.put(url, json=producto_actualizado)

    #Assert

    assert response.status_code == 404

def test_actualizar_producto_con_precio_cero(base_url, producto_creado):
    # Arrange

    producto_id = producto_creado["id"]
    url = f"{base_url}/api/products/{producto_id}"
    payload= { 
        "name": "Producto precio actualizado",
        "price": 0,
        "stock": 10
    }
    #Act
    response = requests.put(url, json=payload)

    #Assert
    assert response.status_code == 400

def test_actualizar_producto_con_stock_negativo(base_url, producto_creado):
    # Arrange

    producto_id = producto_creado["id"]
    url = f"{base_url}/api/products/{producto_id}"
    payload= { 
        "name": "Producto stock negativo actualizado",
        "price": 100,
        "stock": -1
    }

    #Act

    response = requests.put(url, json=payload)
    
    #Assert

    assert response.status_code == 400
    


# --------------------------------------------------------- DELETE TEST ------------------------------------------------------------------
    
def test_eliminar_producto_existente(base_url, producto_valido):
    # Arrange

    crear_response = requests.post(
        f"{base_url}/api/products",
        json=producto_valido
    )
    assert crear_response.status_code == 201
    producto_id = crear_response.json()["id"]

    url = f"{base_url}/api/products/{producto_id}"

    #Act
    response = requests.delete(url)

    #Assert
    assert response.status_code == 204

def test_eliminar_producto_inexistente(base_url, id_inexistente):
    # Arrange

    url = f"{base_url}/api/products/{id_inexistente}"
    

    #Act

    response = requests.delete(url)
    
    #Assert

    assert response.status_code == 404
    


   
   

    

    



    