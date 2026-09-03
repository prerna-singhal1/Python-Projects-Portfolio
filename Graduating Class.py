class Student:

    class_yr = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Prerna", 20)
student2 = Student("Aaditi", 22)
student3 = Student("Ritu", 22)
student4 = Student("Nilendra", 22)

print(f"My graduating class of {Student.class_yr} has {Student.num_students} students:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)