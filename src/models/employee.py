class Employee:
    def __init__(self, employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, hire_date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.city_id = city_id
        self.hire_date = hire_date

    def years_od_service(self, current_year):
        return current_year - self._hire_date.year