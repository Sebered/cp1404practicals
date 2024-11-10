class Guitar:

    def __init__(self, guitar_name = "", guitar_year = 0, guitar_cost = 0):
        self.name = guitar_name
        self.year = guitar_year
        self.cost = guitar_cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        age = 2024 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False