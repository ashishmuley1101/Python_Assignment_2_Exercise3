
# Exercise 3 :-
# UC 1. Define a Python function student(). Using function attributes display the names of all arguments.
# UC 2.Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
# UC 3. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given forma


# UC 3. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given forma
class Student:

    name = ""
    age  = 0
    section = ""

    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section

    def display(self):
        print("Student Name :", self.name)
        print("Student age :", self.age)
        print("Student section :", self.section)

# Two instances student1, student2 and assign given values to the said instances attributes.
student1 = Student("Jack", 16, 'A')
student2 = Student("Krack", 15, 'B')

# Printing all the attributes of student1, student2 instances with their values.
student1.display()
print("\n")
student2.display()