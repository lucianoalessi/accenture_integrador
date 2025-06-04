class City:
    def __init__(self, city_id, city_name, zip_code, country_id):
        self.city_id = city_id
        self.city_name = city_name
        self.zip_code = zip_code
        self.country_id = country_id

    def __str__(self):
        return self._name