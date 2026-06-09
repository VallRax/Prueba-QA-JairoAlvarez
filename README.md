# Prueba-QA-JairoAlvarez
Prueba tecnica QA Junior Automatizador.
## Instalacion

pip install pytest requests

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

