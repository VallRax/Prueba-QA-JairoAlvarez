import requests

def  test_crear_y_obtener_producto(base_url, producto_valido):
    # Arrange

    url = f"{base_url}/api/products"

    #Act
   
    crear_response = requests.post(url, json=producto_valido)

    #Assert

    assert crear_response.status_code == 201
    producto_creado = crear_response.json()
    producto_id = producto_creado["id"]

    obtener_response = requests.get(f"{base_url}/api/products/{producto_id}")

    assert obtener_response.status_code == 200
    producto_obtenido = obtener_response.json()
    assert producto_obtenido["id"] == producto_id
    assert producto_obtenido["name"] == producto_valido["name"]
    assert producto_obtenido["price"] == producto_valido["price"]
    assert producto_obtenido["stock"] == producto_valido["stock"]

    requests.delete(f"{base_url}/api/products/{producto_id}")


def test_crear_actualizar_y_verificar_producto(base_url, producto_valido, producto_actualizado):
    # Arrange

    url = f"{base_url}/api/products"

    #Act
    crear_response = requests.post(url, json=producto_actualizado)
   
    #Assert
    assert crear_response.status_code == 201
    producto_creado = crear_response.json()
    producto_id = producto_creado["id"]

    get_inicial = requests.get(f"{base_url}/api/products/{producto_id}")
    assert get_inicial.status_code == 200

    update_response = requests.put(f"{base_url}/api/products/{producto_id}", json=producto_actualizado)

    assert update_response.status_code == 200

    get_final = requests.get(f"{base_url}/api/products/{producto_id}")
    assert get_final.status_code == 200

    producto_final = get_final.json()
    assert producto_final["id"] == producto_id
    assert producto_final["name"] == producto_actualizado["name"]
    assert producto_final["price"] == producto_actualizado["price"]
    assert producto_final["stock"] == producto_actualizado["stock"]

    requests.delete(f"{base_url}/api/products/{producto_id}")
    
def test_crear_listar_y_verificar_producto_en_lista(base_url, producto_valido):
    # Arrange
    url = f"{base_url}/api/products"

    # Act
    crear_response = requests.post(url, json=producto_valido)

    # Assert
    assert crear_response.status_code == 201
    producto_creado = crear_response.json()
    producto_id = producto_creado["id"]

    listar_response = requests.get(url)

    assert listar_response.status_code == 200
    productos = listar_response.json()

    producto_encontrado = None

    for producto in productos:
        if producto["id"] == producto_id:
            producto_encontrado = producto

    assert producto_encontrado is not None
    assert producto_encontrado["name"] == producto_valido["name"]
    assert producto_encontrado["price"] == producto_valido["price"]
    assert producto_encontrado["stock"] == producto_valido["stock"]

    requests.delete(f"{base_url}/api/products/{producto_id}")