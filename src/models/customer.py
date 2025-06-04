class Customer:
    def __init__(self, customer_id, first_name, middle_initial, last_name, city_id, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.city_id = city_id
        self.address = address

    def full_name(self):
        return f"{self._first_name} {self._middle_initial}. {self._last_name}".strip()