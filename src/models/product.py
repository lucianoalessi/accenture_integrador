class Product:
    def __init__(self, product_id, product_name, price, category_id, product_class, modify_date, resistant, is_allergic, vitality_days):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category_id = category_id
        self.product_class = product_class
        self.modify_date = modify_date
        self.resistant = resistant
        self.is_allergic = is_allergic
        self.vitality_days = vitality_days


        def is_perishable(self):
            return self._vitality_days > 0
        
        def is_premium(self):
            return self._product_class.lower() == "high"