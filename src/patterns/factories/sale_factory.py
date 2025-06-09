from src.models.sale import Sale

class Salefactory:
    """
    Clase de fábrica que implementa un método para crear instancias de la clase Sale
    a partir de una fila de un DataFrame de pandas (una pd.Series).
    """

    @staticmethod
    def from_series(serie):
        """
        Método estático que convierte una fila de un DataFrame (pd.Series) en un objeto Sale.

        Parámetros:
        - serie (pd.Series): una fila del DataFrame con los datos de una venta. 
          Debe contener las siguientes columnas: 
          'SalesID', 'SalesPersonID', 'CustomerID', 'ProductID', 
          'Quantity', 'Discount', 'TotalPrice', 'SalesDate', 'TransactionNumber'.

        Retorna:
        - Sale: una instancia de la clase Sale con los valores extraídos de la fila.
        """
        return Sale(
            sales_id=serie["SalesID"],                    
            sales_person_id=serie["SalesPersonID"],       
            customer_id=serie["CustomerID"],              
            product_id=serie["ProductID"],                
            quantity=serie["Quantity"],                   
            discount=serie["Discount"],                   
            total_price=serie["TotalPrice"],              
            sales_date=serie["SalesDate"],                
            transaction_number=serie["TransactionNumber"] 
        )
