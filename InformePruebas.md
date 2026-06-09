# Informe de Pruebas API Productos

## Información General

* Proyecto: API Productos
* Herramienta de pruebas: Pytest
* Lenguaje: Python
* Fecha de ejecución: 08-06-2026
* Entorno: Localhost
* URL Base: http://localhost:8080

---

## Resumen de Ejecución

| Métrica                     | Valor  |
| --------------------------- | ------ |
| Total de pruebas ejecutadas | 19     |
| Pruebas exitosas            | 18     |
| Pruebas fallidas            | 1      |
| Tasa de éxito               | 94.74% |

---

## Resultados Funcionales

| ID     | Caso                                             | Resultado |
| ------ | ------------------------------------------------ | --------- |
| CP-001 | Listar productos                                 | PASS      |
| CP-002 | Obtener producto existente                       | PASS      |
| CP-003 | Obtener producto inexistente                     | PASS      |
| CP-004 | Obtener producto con ID inválido                 | PASS      |
| CP-005 | Crear producto exitoso                           | PASS      |
| CP-006 | Crear producto sin nombre                        | PASS      |
| CP-007 | Crear producto duplicado                         | FAIL      |
| CP-008 | Crear producto con precio cero                   | PASS      |
| CP-009 | Crear producto con stock negativo                | PASS      |
| CP-010 | Crear producto con nombre de 100 caracteres      | PASS      |
| CP-011 | Crear producto con nombre mayor a 100 caracteres | PASS      |
| CP-012 | Actualizar producto existente                    | PASS      |
| CP-013 | Actualizar producto inexistente                  | PASS      |
| CP-014 | Eliminar producto existente                      | PASS      |
| CP-015 | Eliminar producto inexistente                    | PASS      |

---

## Resultados de Integración

| ID      | Caso                                   | Resultado |
| ------- | -------------------------------------- | --------- |
| INT-001 | Crear y obtener producto               | PASS      |
| INT-002 | Crear, actualizar y verificar producto | PASS      |

---

## Resultados de Regresión

| ID      | Caso                                          | Resultado |
| ------- | --------------------------------------------- | --------- |
| REG-001 | Eliminar producto sin afectar otros registros | PASS      |
| REG-002 | Producto eliminado no puede recuperarse       | PASS      |

---

# Defectos Encontrados

## BUG-001 - Error al crear producto duplicado

### Caso asociado

CP-007 - Crear producto con nombre duplicado

### Descripción

Al intentar registrar un producto utilizando un nombre que ya ha sido creado, la API responde con un error interno del servidor.Según lo esperado de la aplicación debería validar la duplicidad del nombre y retornar una respuesta controlada indicando que el producto ya existe.

### Resultado esperado

http 400 Bad Request o http 409 Conflict

### Resultado obtenido

http 500 Internal Server Error

### Severidad

Alta

### Prioridad

Alta

### Evidencia

text FAILED tests/functional/test_products.py::test_crear_producto_nombre_duplicado assert response.status_code in [400, 409] E assert 500 in [400, 409]

### Impacto

El usuario recibe el error interno del servidor en lugar de una respuesta valida y controlada, lo cual esto dificulta la identificacion del problema, afectando la experiencia del  consumo de la APi

# Conclusiones

lA API presenta un comportamiento estable en los escenarios funcionales, de integracion y regresion ejecutados, lo cual, fueron 18 de las 19 pruebas automatizadas que tuvieron exito, calculando que es uan tasa de exito del 94.74%

Se identifico un defecto relacionado con la creacion de los productos duplicados, donde la aplicacion retorna un codigo http 500 que es una error en el servidor interno, cuando deberia de responder con un codigo de validacion controlado 400 o 409 que en este caso son un Bad request o Conflict. Recomiendo implementar un manejo de la excepcion relacionada a los productos duplicados para evitar errores internos y mejorar la robustez de la API.


## Hallazgo adicional

Durante la lectura del documento me pude percatar que la seccion de ProductService.update() no valida unicidad del nombre del producto, por ende, podria permitirse actualizar un producto utilizando el nombre de otro producto ya existente y generaria un registro duplicado. 

## Estado Final

**APROBADO CON OBSERVACIONES**

La funcionalidad principal de la API funciona correctamente, sin embargo, existe un defecto que debería ser corregido antes de un paso a producción.

