class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"Student - Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"Teacher - Name: {self.name}, Age: {self.age}, Subject: {self.subject}"


def read_students_from_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            name, age, student_id = line.strip().split(', ')
            students.append(Student(name, int(age), student_id))
    return students


def read_teachers_from_file(filename):
    teachers = []
    with open(filename, 'r') as file:
        for line in file:
            name, age, subject = line.strip().split(', ')
            teachers.append(Teacher(name, int(age), subject))
    return teachers


# Öğrenci ve öğretmen bilgilerini dosyadan okuma
students = read_students_from_file('students.txt')
teachers = read_teachers_from_file('teachers.txt')

# Bilgileri görüntüleme
for student in students:
    print(student.display_info())

for teacher in teachers:
    print(teacher.display_info())