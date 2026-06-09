import requests

def test_eliminar_producto_sin_afectar_otros_registros(base_url, producto_valido):
    # Arrange
    producto_1 = {
        "name": producto_valido["name"] + "-1",
        "price": 100,
        "stock": 10
    }

    producto_2 = {
        "name": producto_valido["name"] + "-2",
        "price": 200,
        "stock": 20
    }

    response_1 = requests.post(f"{base_url}/api/products", json=producto_1)
    response_2 = requests.post(f"{base_url}/api/products", json=producto_2)

    assert response_1.status_code == 201
    assert response_2.status_code == 201

    producto_id_1 = response_1.json()["id"]
    producto_id_2 = response_2.json()["id"]

    #Act
    delete_response = requests.delete(f"{base_url}/api/products/{producto_id_1}")
    

    #Assert
    assert delete_response.status_code == 204

    get_producto_2 = requests.get(f"{base_url}/api/products/{producto_id_2}")
    assert get_producto_2.status_code == 200

    data = get_producto_2.json()
    assert data["id"] == producto_id_2
    assert data["name"] == producto_2["name"]

    requests.delete(f"{base_url}/api/products/{producto_id_2}")


def test_producto_eliminado_no_puede_recuperarse(base_url, producto_valido):
    # Arrange
    crear_response = requests.post(f"{base_url}/api/products", json=producto_valido)
    assert crear_response.status_code == 201

    producto_id = crear_response.json()["id"]

    #Act
    
    delete_response = requests.delete(f"{base_url}/api/products/{producto_id}")
    get_response = requests.get(f"{base_url}/api/products/{producto_id}")    

    #Assert
    assert delete_response.status_code == 204
    assert get_response.status_code == 404
    

    