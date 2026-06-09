# Casos de Prueba API Productos

## Funcionales


### GET

### CP-001 - Listar productos

- Endpoint: GET /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada: Sin parámetros
- Resultado esperado: Retorna listado de productos
- Status code esperado: 200

### CP-002 - Obtener producto existente

- Endpoint: GET /api/products/{id}
- Tipo: Funcional
- Condición: Existe un prodcuto registrado
- Entrada:  
``` json 
{ 
    "id": 1
} 
```
- Resultado esperado: Retorna informacion del producto
- Status code esperado: 200

### CP-003 - Obtener producto inexistente

- Endpoint: GET /api/products/99999
- Tipo: Funcional
- Condición: Producto No existe
- Entrada:  
``` json 
{ 
    "id": 99999
} 
```
- Resultado esperado: Producto no encontrado
- Status code esperado: 404

### CP-004 - Obtener producto con ID inválida

- Endpoint: GET /api/products/abc
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "id": abc
} 
```
- Resultado esperado: Error de validación
- Status code esperado: 400



### POST

### CP-005 - Crear producto exitoso

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "name": "Producto A",
    "price": 100,
    "stock": 10
} 
```
- Resultado esperado: Producto creado correctamente
- Status code esperado: 201

### CP-006 - Crear producto sin nombre

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "price": 100,
    "stock": 10
} 
```
- Resultado esperado: Error de validación
- Status code esperado: 400

### CP-007 - Crear producto con nombre duplicado

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: Producto con mismo nombre ya existente
- Entrada:  
``` json 
{ 
    "name": "Producto A",
    "price": 100,
    "stock": 10
} 
```
- Resultado esperado: Error de validacion
- Status code esperado: 400 o 409
- Resultado actual: 500 Internal Server Error (BUG)

### CP-008 - Crear producto con precio cero

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "name": "Producto B",
    "price": 0,
    "stock": 5
} 
```
- Resultado esperado: Error de validacion
- Status code esperado: 400

### CP-009 - Crear producto con stock negativo

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "name": "Producto C",
    "price": 100,
    "stock": -1
} 
```
- Resultado esperado: Error de validacion
- Status code esperado: 400

### CP-010 - Crear producto con nombre de 100 caracteres

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "name": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "price": 100,
    "stock": 1
} 
```
- Resultado esperado: Producto creado correctamente
- Status code esperado: 200

### CP-011 - Crear producto con nombre mayor a 100 caracteres

- Endpoint: POST /api/products
- Tipo: Funcional
- Condición: API disponible
- Entrada:  
``` json 
{ 
    "name": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "price": 100,
    "stock": 1
} 
```
- Resultado esperado: Error de validacion
- Status code esperado: 400


### PUT

### CP-012 - Actualizar producto existente

- Endpoint: PUT /api/products/{id}
- Tipo: Funcional
- Condición: Producto existe
- Entrada:  
``` json 
{ 
    "name": "Producto Actualizado",
    "price": 150,
    "stock": 20
} 
```
- Resultado esperado: Producto actualizado
- Status code esperado: 200

### CP-013 - Actualizar producto inexistente

- Endpoint: PUT /api/products/99999
- Tipo: Funcional
- Condición: Producto no existe
- Entrada:  
``` json 
{ 
    "name": "Producto Actualizado",
} 
```
- Resultado esperado: Producto no encontrado
- Status code esperado: 404

### DELETE


### CP-014 - Eliminar producto existente

- Endpoint: DELETE /api/products/{id}
- Tipo: Funcional
- Condición: Producto existe
- Entrada:  
``` json 
{ 
    "id": 1
} 
```
- Resultado esperado: Producto eliminado
- Status code esperado: 204

### CP-015 - Eliminar producto inexistente

- Endpoint: DELETE /api/products/99999
- Tipo: Funcional
- Condición: Producto no existe
- Entrada:  
``` json 
{ 
    "id": 99999
} 
```
- Resultado esperado: Producto no encontrado
- Status code esperado: 404

### CP-016 - Actualizar producto con precio cero

- Endpoint: PUT /api/products/{id}
- Tipo: Funcional
- Condición: Producto existente
- Entrada:
``` json
    {
        "name": "Producto Precio Cero Update",
        "price": 0,
         "stock": 10
    }
```
- Resultado esperado: Error de validación
- Status code esperado: 400

### CP-017 - Actualizar producto con stock negativo
- Endpoint: PUT /api/products/{id}
- Tipo: Funcional
- Condición: Producto existente
- Entrada:
``` json
    {
        "name": "Producto Stock Negativo Update",
        "price": 100,
        "stock": -1
    }
```
- Resultado esperado: Error de validación
- Status code esperado: 400


### INTEGRACIÓN

### INT-01 - Crear y obtener producto

- Tipo: Integración
- flujo:
```text
POST /api/products
↓
GET /api/products/{id}
```
- Resultado esperado: El producto creado se recupera correctamente.

### INT-02 - Crear, actualizar y verificar producto

- Tipo: Integración
- flujo:
```text
POST /api/products
↓
GET /api/products/{id}
↓
PUT /api/products/{id}
↓
GET /api/products/{id}
```
- Resultado esperado: Los cambios realizados se guardan correctamente.

### INT-003 - Crear, listar y verificar producto
- Tipo: Integración

- Flujo:

POST /api/products
↓
GET /api/products

- Resultado esperado: El producto creado aparece en el listado de productos.

### REGRESIÓN


### REG-001 - Eliminar producto sin afectar otros registros

- Tipo: Regresion
- Resultado esperado: Los demas productos permanecen disponibles despues de una eliminacion

### REG-002 - Producto eliminado no puede recuperarse
- Tipo: Regresión
- Resultado esperado: La consulta posterior retonra 404 Not Found

### REG-003 - Actualizar producto sin modificar su ID

- Tipo: Regresión

Flujo:

PUT /api/products/{id}
↓
GET /api/products/{id}
- Resultado esperado: El producto mantiene su ID original después de ser actualizado.




