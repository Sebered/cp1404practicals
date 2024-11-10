class ProgrammingLanguage:

    def __init__(self, language_name, language_typing, language_reflection, language_year):
        self.name = language_name
        self.typing = language_typing
        self.reflection = language_reflection
        self.year = language_year

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"