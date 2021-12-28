class ProgrammingLanguage:
    def __init__(self, fields, type, reflection, year):
        self.fields = fields
        self.type = type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.type == "Dynamic"

    def __str__(self):
        return "{}, {}, reflection = {}, first appeared in{}".format(self.fields,self.type, self.reflection,self.year)
