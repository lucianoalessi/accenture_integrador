class sale:
    def __init__(self, sales_id, sales_person_id, customer_id, product_id, quantity, discount, total_price, sales_date, transaction_number):
        self.sales_id = sales_id
        self.sales_person_id = sales_person_id
        self.customer_id = customer_id
        self.product_id = product_id,
        self.quantity = quantity,
        self.discount = discount
        self.total_price = total_price
        self.sales_date = sales_date
        self.transaction_number = transaction_number

    def is_high_value(self):
        return self._total_price >= 1000