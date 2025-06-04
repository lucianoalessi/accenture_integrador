class Country:
    def __init__(self, country_id, name, code):
        self.country_id = country_id
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self._name} ({self._code})"