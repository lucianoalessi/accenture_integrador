class SalesQueryBuilder:
    """
    Esta clase implementa el patrón Builder para construir consultas SQL a la tabla 'sales'.
    Permite aplicar filtros condicionales, realizar agregaciones y utilizar expresiones CTE
    de forma modular y encadenada.
    """

    def __init__(self):
        # Consulta base por defecto
        self.query = "SELECT * FROM sales"
        # Lista de filtros (cláusulas WHERE) que se irán agregando
        self.filters = []

    def with_customer(self, customer_id):
        """
        Agrega un filtro por ID de cliente.
        """
        self.filters.append(f"CustomerID = {customer_id}")
        return self  # Permite el encadenamiento de métodos

    def with_salesperson(self, salesperson_id):
        """
        Agrega un filtro por ID de vendedor.
        """
        self.filters.append(f"SalesPersonID = {salesperson_id}")
        return self

    def with_min_quantity(self, quantity):
        """
        Agrega un filtro para seleccionar ventas con una cantidad mínima.
        """
        self.filters.append(f"Quantity >= {quantity}")
        return self

    def with_date_range(self, start_date, end_date):
        """
        Agrega un filtro para seleccionar ventas dentro de un rango de fechas.
        """
        self.filters.append(f"SalesDate BETWEEN '{start_date}' AND '{end_date}'")
        return self
    

    def with_top_acumulado_por_categoria(self):
        """
        Reemplaza la consulta base por una nueva que calcula el total acumulado de ventas
        por categoría y le asigna un ranking utilizando una función de ventana.

        Esta consulta:
        - Agrupa las ventas por nombre de categoría.
        - Calcula la suma total de ventas (TotalPrice) por cada categoría.
        - Aplica la función de ventana RANK() para asignar un ranking a cada categoría según el monto total vendido, 
        de mayor a menor.
        - Elimina cualquier filtro previamente acumulado ya que esta consulta es independiente del resto.

        Retorna:
        - self: Permite el encadenamiento de métodos (pattern: method chaining).
        """
        self.query = """
            SELECT  
                c.CategoryName,
                SUM(s.TotalPrice) AS total_sale,
                RANK() OVER (ORDER BY SUM(s.TotalPrice) DESC) AS categoria_rank
            FROM 
                sales s
            LEFT JOIN 
                products p ON s.ProductID = p.ProductID
            LEFT JOIN 
                categories c ON p.CategoryID = c.CategoryID
            GROUP BY 
                c.CategoryName
            ORDER BY  
                total_sale DESC;
        """
        self.filters = []  # Se eliminan los filtros anteriores porque esta consulta es independiente
        return self
    

    def with_top_acumulado_por_producto(self):
        """
        Reemplaza la consulta base por una nueva que calcula el total acumulado de ventas
        por producto y le asigna un ranking utilizando una función de ventana.

        Esta consulta:
        - Agrupa las ventas por nombre de producto.
        - Calcula la suma total de ventas (TotalPrice) por cada producto.
        - Aplica la función de ventana RANK() para asignar un ranking a cada product según el monto total vendido, 
        de mayor a menor.
        - Elimina cualquier filtro previamente acumulado ya que esta consulta es independiente del resto.

        Retorna:
        - self: Permite el encadenamiento de métodos (pattern: method chaining).
        """
        self.query = """
            SELECT  
                p.ProductName,
                SUM(s.TotalPrice) AS total_sale,
                RANK() OVER (ORDER BY SUM(s.TotalPrice) DESC) AS product_rank
            FROM 
                sales s
            LEFT JOIN 
                products p ON s.ProductID = p.ProductID
            GROUP BY 
                p.ProductName
            ORDER BY  
                total_sale DESC;
        """
        self.filters = []  # Se eliminan los filtros anteriores porque esta consulta es independiente
        return self


    def with_acumulado_por_cliente(self):
        """
        Reemplaza la consulta base con una que calcula el acumulado de ventas
        por cliente a lo largo del tiempo usando una función de ventana.
        """
        self.query = """
            SELECT
                CustomerID,
                SalesDate,
                TotalPrice,
                SUM(TotalPrice) OVER (
                    PARTITION BY CustomerID
                    ORDER BY SalesDate
                ) AS acumulado_cliente
            FROM sales
        """
        self.filters = []  # Se eliminan los filtros anteriores porque esta consulta es independiente
        return self

    def with_ventas_cte(self, min_total=500):
        """
        Reemplaza la consulta con una expresión CTE que calcula el total de ventas por cliente
        y filtra solo aquellos cuyo total supera un mínimo (por defecto 500).
        """
        self.query = f"""
            WITH ventas_por_cliente AS (
                SELECT CustomerID, SUM(TotalPrice) AS total
                FROM sales
                GROUP BY CustomerID
            )
            SELECT *
            FROM ventas_por_cliente
            WHERE total >= {min_total}
        """
        self.filters = []  # Se eliminan los filtros anteriores porque esta consulta también es independiente
        return self

    def build(self):
        """
        Devuelve la consulta SQL final.
        Si hay filtros agregados, los concatena a la consulta base.
        Si no hay filtros, devuelve la consulta tal como está.
        """
        if self.filters:
            return self.query + " WHERE " + " AND ".join(self.filters)
        return self.query
