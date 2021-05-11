class Student:
    def __init__(self, id, name, age, attendance):
        self.id = id
        self.name = name
        self.age = age
        self.attendance = attendance

    def __str__(self):
        return f'{self.name}'

