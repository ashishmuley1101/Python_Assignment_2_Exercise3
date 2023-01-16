
# Exercise 3 :-
# UC 1. Define a Python function student(). Using function attributes display the names of all arguments.
# UC 2.Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
# UC 3. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given forma


# UC 1. Function student(). Using function attributes display the names of all arguments.
def student(name, age, section):

    print("\nStudent Name : ", name, "\nStudent Age : ", age, "\nStudent Section : ", section)

student_name = input("Enter Student Name : ")
student_age = input("Enter Student Age : ")
student_section = input("Enter Student Section : ")

student(student_name, student_age, student_section)