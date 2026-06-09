# Prueba-QA-JairoAlvarez

Este proyecto corresponde a la resolución de la Prueba Técnica QA Junior Automatizador.
Se desarrollaron casos de prueba funcionales, de integración y de regresión para una API REST de gestión de productos utilizando Python, Pytest y Requests.
Debido a que no se disponía de un backend Spring Boot ejecutable, se implementó una API mock utilizando Flask que replica el comportamiento esperado de los endpoints definidos en el enunciado, incluyendo el defecto identificado para la creación de productos duplicados.

### Tecnologías utilizadas
- Python 3.x
- Pytest
- Requests
- Flask
- Git / GitHub

## Instalacion

- Crear entorno virtual:

    - python -m venv venv

    - Activar entorno virtual:

    - venv\Scripts\activate

    - Instalar dependencias:

    - pip install pytest requests flask

### Backend Mock

Para ejecutar las pruebas se creó un archivo app.py utilizando Flask.

Este archivo implementa los siguientes endpoints:

GET    /api/products
GET    /api/products/{id}
POST   /api/products
PUT    /api/products/{id}
DELETE /api/products/{id}

La aplicación mantiene los productos en memoria y replica las validaciones descritas en el código Java entregado en la prueba.

También se simuló el defecto esperado para productos duplicados, retornando un error HTTP 500 al intentar registrar un nombre existente.

### Ejecución del Backend

- Iniciar la API mock:

    - python app.py, La aplicación quedará disponible en: http://localhost:8080

### Ejecución de Pruebas

- Ejecutar todas las pruebas:

    - pytest -v

- Ejecutar únicamente pruebas funcionales:

    - pytest tests/functional -v

- Ejecutar únicamente pruebas de integración:

    - pytest tests/integration -v

- Ejecutar únicamente pruebas de regresión:

    - pytest tests/regression -v

## Variables de entorno

export API_BASE_URL=http://localhost:8080

## Ejecucion

pytest tests/ -v

## Preguntas de cierre
1.¿Qué caso de prueba te pareció más importante y por qué?

R: El caso que más me parecio importante fue la creación de productos con nombres duplicados que en este caso es la prueba CP-007, el cual me permitio identificar un defecto de la lógica de la API que genera un error interno en el servidor en lugar de un codigo de validacion adecuado como el codigo 400 o 409. Considero que este caso es crítico por que valida reglas de negocio relacionadas a la integridad de los datos y tambien nos demuestra la capacidad de detectar errores que pueden afectar directamente a los usuarios.

2. ¿Encontraste algo en el código que te generó dudas o que probarías diferente si tuvieras más tiempo?

R: Si encontre algo que en este caso seria la duplicacion de los productos, no esta siendo manejada por el controlador, entonces provoca el error 500 detectado durante las pruebas.
Si pudiera realizar mas pruebas adicionales relacionadas a ese BUG, buscaria una concurrencia en la creacion de los productos, valores extremos en los precios y stock, tambien los caracteres especiales o algun tipo de espacio en blanco en el nombre, validaria tambien los formatos y los tipos de datos incorrectos y finalizaria con pruebas de rendimiento para evaluar su comportamiento.

3. ¿Cómo organizarías los tests si esta API tuviera 10 endpoints en vez de 5?

R: Mantendria la estructura del proyecto actual, y separaria las pruebas por tipo y por recurso, tambien reutilizaria los fixtures comunes en mi archivo conftest.py, utilizaria los datos de prueba centralizados y ejecutaria los distintos grupos de pruebas mediante piplines de IC para facilitar el mantenimiento y la escalabilidad.

