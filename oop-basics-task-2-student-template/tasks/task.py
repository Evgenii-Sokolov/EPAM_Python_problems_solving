class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades
    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"