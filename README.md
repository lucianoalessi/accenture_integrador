# Cohorte de-prep-accenture: Sistema de análisis de ventas - Trabajo Integrador.

Proyecto integrador de análisis y manipulación de datos de ventas utilizando patrones de diseño en Python y MySQL.

## Descripción

Este proyecto implementa una arquitectura robusta para la gestión y análisis de datos de ventas, utilizando patrones de diseño como Singleton, Factory y Builder. Permite la conexión eficiente a una base de datos MySQL, la ejecución de consultas avanzadas (incluyendo CTEs y funciones de ventana), la creación de vistas, funciones, procedimientos y triggers, y la conversión de resultados a objetos Python o DataFrames de pandas.

## Estructura del Proyecto

```
accenture_integrador/
│
├── data/
│   └─ raw_data.csv                               # Datos crudos de ventas y entidades
├── sql/
│   ├─ load_data.sql                              # Script para cargar datos iniciales
│   ├─ function_calculate_age.sql                 # Función SQL para calcular edad
│   ├─ index.sql                                  # Scripts de creación de índices
│   ├─ procedure_get_employees_by_age_range.sql   # Procedimiento almacenado para empleados por rango de edad
│   ├─ trigger_before_product_update.sql          # Trigger para registrar modificaciones de productos
│   ├─ view_sales_by_employee_month.sql           # Vista resumen de ventas por empleado y mes
│   └─ view_sales_customer.sql                    # Vista resumen de ventas por cliente
├── src/
│   └─ models/
│       ├─ category.py                            # Modelo de categoría de producto
│       ├─ city.py                                # Modelo de ciudad
│       ├─ country.py                             # Modelo de país
│       ├─ customer.py                            # Modelo de cliente
│       ├─ employee.py                            # Modelo de empleado
│       ├─ product.py                             # Modelo de producto
│       └─ sale.py                                # Modelo de venta
│   └─ patterns/
│       ├─ builder_pattern/
│       │   └─ sales_query_builder.py             # Builder para consultas SQL dinámicas de ventas
│       ├─ factories/
│       │   └─ sale_factory.py                    # Factory para instanciar objetos Sale desde datos
│       └─ singleton/
│           └─ db_connector.py                    # Conector Singleton para la base de datos MySQL
├── test/
│   └─ test_sale_model.py                         # Pruebas unitarias para el modelo Sale
├── venv/                                         # Entorno virtual de Python
├── .env                                          # Variables de entorno para la conexión a la base de datos
├── .gitignore                                    # Archivos y carpetas ignorados por git
├── main.ipynb                                    # Notebook principal con ejemplos y pruebas
├── README.md                                     # Documentación del proyecto
├── requirements.txt                              # Listado de requerimientos
```

## Características principales

- Conexión a MySQL mediante patrón Singleton.
- Ejecución de queries y conversión de resultados a DataFrame o a objetos Python.
- Ejecución de scripts SQL completos desde archivos.
- Consultas avanzadas: CTEs, funciones de ventana, vistas, funciones, procedimientos y triggers.
- Patrones de diseño: Singleton, Factory, Builder.
- Notebook interactivo para pruebas y ejemplos (`main.ipynb`).

## Requisitos

- Python 3.8+
- Tener acceso a una base de datos MySQL.
- Archivo `.env` configurado con los datos de conexión.

## Instalación y ejecución paso a paso

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/tu_usuario/accenture_integrador.git
    cd accenture_integrador
    ```

2. **Crear y activar un entorno virtual**

    **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
    **Linux/Mac:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instalar las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar las variables de entorno**

    Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta los valores según tu entorno):

    ```
    DB_HOST=localhost
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_NAME=tu_base_de_datos
    DB_PORT=3306
    ```

5. **Crear la base de datos y cargar los datos**

    - Ejecuta el script SQL `load_data.sql` de la carpeta `sql/` en tu base de datos MySQL para crear la base de datos, tablas y cargar datos desde los archivos CSV.
    - Ejecuta el resto de archivos SQL para crear vistas, funciones, procedimientos, índices y triggers.
    - Puedes ejecutar estos scripts SQL desde `main.ipynb` usando el método `ejecutar_script_sql()` de la clase `MySQLConnector`.
    - Para la carga de datos desde los archivos csv, estos deben estar ubicados en: `C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/`

6. **Ejecutar el notebook de ejemplo**

    Abre el archivo `main.ipynb` con VSCode o Jupyter Notebook, sigue los ejemplos y ejecuta las celdas.

---




## Decisiones técnicas y justificación

### Uso de patrones de diseño

- **Singleton para la conexión a la base de datos:**  
  Se eligió el patrón Singleton en `db_connector.py` para asegurar que toda la aplicación utilice una única instancia de conexión a MySQL. Esto evita problemas de múltiples conexiones abiertas, reduce el consumo de recursos y centraliza la gestión de la conexión, facilitando el mantenimiento y la trazabilidad de errores.

- **Factory para instanciation de objetos de dominio:**  
  El patrón Factory (`sale_factory.py`) permite transformar fácilmente filas de un DataFrame en objetos `Sale`. Esto desacopla la lógica de acceso a datos de la lógica de negocio, permitiendo trabajar con objetos y métodos propios del dominio, lo que mejora la legibilidad y la extensibilidad del código.

- **Builder para consultas SQL dinámicas:**  
  El Builder Pattern (`sales_query_builder.py`) facilita la construcción de consultas SQL complejas de manera flexible y segura, permitiendo encadenar filtros y construir queries avanzadas (CTE, funciones de ventana, rankings) sin escribir SQL manualmente en cada parte del código. Esto reduce errores, mejora la reutilización y permite adaptar fácilmente las consultas a nuevas necesidades de análisis.

### Procesos implementados

- **Carga y preparación de datos:**  
  Scripts SQL para crear la estructura de la base de datos, cargar datos iniciales y definir vistas, funciones, procedimientos y triggers.
- **Ejecución de consultas y análisis:**  
  El notebook `main.ipynb` muestra el flujo completo: conexión, ejecución de queries, transformación de resultados a objetos, análisis avanzado y visualización.
- **Manejo de errores y robustez:**  
  El método `ejecutar_script_sql` informa claramente si hay errores de sintaxis en los scripts SQL, mostrando la sentencia problemática y su posición.

### Resultados obtenidos

- **Código modular y reutilizable:**  
  Gracias a los patrones de diseño, el código es fácil de mantener, extender y reutilizar en otros proyectos o contextos.

- **Consultas avanzadas y optimización:**  
  Se pueden realizar análisis complejos (por ejemplo, rankings de productos/categorías, acumulados por cliente, filtros dinámicos).

- **Documentación y ejemplos claros:**  
  El notebook y este README permiten a cualquier usuario comprender rápidamente el flujo de trabajo, adaptar el código a sus necesidades y entender el porqué de cada decisión técnica.





### Descripción de archivos clave

### `main.ipynb`

Guía práctica y demostrativa del proyecto. Incluye ejemplos de uso de todos los patrones y módulos principales, así como análisis y visualización de datos.

**Incluye:**
- Ejemplo de conexión a la base de datos usando el patrón Singleton.
- Ejecución de queries y conversión de resultados a DataFrame y a objetos `Sale` usando el Factory.
- Uso del Builder Pattern para construir consultas SQL dinámicas y avanzadas.
- Ejecución de scripts SQL para crear vistas, funciones, procedimientos y triggers.
- Consultas avanzadas con CTEs y funciones de ventana.
- Extra: Comparación de tiempos de ejecución antes y después de optimizar con índices.
- Buenas prácticas de cierre de conexión y manejo de errores.

### `src/patterns/singleton/db_connector.py`

Implementa el **patrón Singleton** para la conexión a la base de datos MySQL.

**Principales métodos:**
- `conectar()`: Establece la conexión usando las variables de entorno.
- `ejecutar_query(query)`: Ejecuta una consulta SQL y devuelve los resultados como lista de tuplas.
- `query_df(query)`: Ejecuta una consulta y devuelve los resultados como un DataFrame de pandas.
- `ejecutar_script_sql(ruta_script)`: Ejecuta un archivo `.sql` completo, mostrando errores de sintaxis si los hubiera.
- `cerrar()`: Cierra la conexión y el cursor.

**Ejemplo de uso:**
```python
from src.patterns.singleton.db_connector import MySQLConnector

db = MySQLConnector()
db.conectar()
resultados = db.ejecutar_query("SELECT * FROM tabla;")
df = db.query_df("SELECT * FROM tabla;")
db.ejecutar_script_sql("ruta/al/archivo.sql")
db.cerrar()
```

Consulta el archivo [`main.ipynb`](main.ipynb) para ejemplos prácticos de uso.

### `src/patterns/builder_pattern/sales_query_builder.py`

Implementa el **Builder Pattern** para la construcción dinámica y flexible de consultas SQL sobre la tabla `sales`.

**Permite:**
- Encadenar métodos para agregar filtros (por cliente, vendedor, cantidad mínima, rango de fechas).
- Construir consultas avanzadas como acumulados y rankings por categoría o producto usando funciones de ventana.
- Consultas con CTE para obtener totales por cliente.

**Ejemplo de uso:**
```python
from src.patterns.builder_pattern.sales_query_builder import SalesQueryBuilder

# Consulta filtrando por cliente y cantidad mínima
query = SalesQueryBuilder().with_customer(123).with_min_quantity(10).build()

# Consulta avanzada con ranking por producto
query = SalesQueryBuilder().with_top_acumulado_por_producto().build()
```

#### Métodos destacados

- `with_top_acumulado_por_categoria()`: Genera una consulta SQL que calcula el total acumulado de ventas por categoría y asigna un ranking.
- `with_top_acumulado_por_producto()`: Genera una consulta SQL que calcula el total acumulado de ventas por producto y asigna un ranking.

### `src/patterns/factories/sale_factory.py`

Implementa el **patrón Factory** para la creación de objetos `Sale` a partir de filas de un DataFrame de pandas.

**Método principal:**
- `Salefactory.from_series(serie)`: Recibe una fila (`pd.Series`) y devuelve una instancia de `Sale`.

**Ejemplo de uso:**
```python
from src.patterns.factories.sale_factory import Salefactory

sales_objs = [Salefactory.from_series(row) for _, row in df.iterrows()]
```

---


## Autor

Desarrollado por Luciano Alessi.
