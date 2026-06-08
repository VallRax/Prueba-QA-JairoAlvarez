from flask import Flask, request, jsonify

app = Flask(__name__)

productos = []
next_id = 1


def buscar_producto(product_id):
    for producto in productos:
        if producto["id"] == product_id:
            return producto
    return None


def validar_producto(data):
    if not data:
        return False

    if "name" not in data or data["name"] == "":
        return False

    if len(data["name"]) > 100:
        return False

    if "price" not in data or data["price"] <= 0:
        return False

    if "stock" not in data or data["stock"] < 0:
        return False

    return True


@app.route("/api/products", methods=["GET"])
def listar_productos():
    return jsonify(productos), 200


@app.route("/api/products/<int:product_id>", methods=["GET"])
def obtener_producto(product_id):
    producto = buscar_producto(product_id)

    if producto is None:
        return "", 404

    return jsonify(producto), 200


@app.route("/api/products/<product_id>", methods=["GET"])
def obtener_producto_id_invalido(product_id):
    return jsonify({"error": "ID inválido"}), 400


@app.route("/api/products", methods=["POST"])
def crear_producto():
    global next_id

    data = request.get_json(silent=True)

    if not validar_producto(data):
        return jsonify({"error": "Datos inválidos"}), 400

    for producto in productos:
        if producto["name"] == data["name"]:
            # Simula el bug real esperado en la prueba técnica:
            # debería ser 400/409, pero devuelve 500.
            return jsonify({"error": "Error interno por duplicado"}), 500

    nuevo_producto = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"]
    }

    productos.append(nuevo_producto)
    next_id += 1

    return jsonify(nuevo_producto), 201


@app.route("/api/products/<int:product_id>", methods=["PUT"])
def actualizar_producto(product_id):
    producto = buscar_producto(product_id)

    if producto is None:
        return "", 404

    data = request.get_json(silent=True)

    if not validar_producto(data):
        return jsonify({"error": "Datos inválidos"}), 400

    producto["name"] = data["name"]
    producto["price"] = data["price"]
    producto["stock"] = data["stock"]

    return jsonify(producto), 200


@app.route("/api/products/<product_id>", methods=["PUT"])
def actualizar_producto_id_invalido(product_id):
    return jsonify({"error": "ID inválido"}), 400


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def eliminar_producto(product_id):
    producto = buscar_producto(product_id)

    if producto is None:
        return "", 404

    productos.remove(producto)

    return "", 204


@app.route("/api/products/<product_id>", methods=["DELETE"])
def eliminar_producto_id_invalido(product_id):
    return jsonify({"error": "ID inválido"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=8080)