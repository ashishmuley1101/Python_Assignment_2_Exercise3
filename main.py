
# Exercise 3 :-
# UC 1. Define a Python function student(). Using function attributes display the names of all arguments.
# UC 2.Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
# UC 3. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given forma



# UC 2. Student class display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
class Student:

    pass      # Pass keyword passing the body if we don't write any code inside class

print(type(Student))  # type() method display its <class 'type'>

# A special attribute of every module is __dict__.
# This is the dictionary containing the module’s symbol table.
# The function __dict__.keys() returns a dictionary view object with the dictionary's list of keys.
print(Student.__dict__.keys())

# This built-in class attribute when called prints
# the name of the module the function/object was defined in, or None if unavailable
print(Student.__module__)  # default print __main__ in python

# Output :
# <class 'type'>
# dict_keys(['__module__', '__dict__', '__weakref__', '__doc__'])
# __main__