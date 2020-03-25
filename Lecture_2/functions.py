'''
def f1():
  print("Hello from a function")
  
f1()
'''

class Person:
    def __init__(self):
        pass
    def __init__(self, name="Beso", age=35):
        self.n = name
        self.__a = age
    def myfunc(self, name):
        print("Hello my name is ", name)
    def myfunc1(self):
        print("I am "+str(self.__a)+" years old")
        
class Student(Person):
    pass
    def myfunc2(self):
        print("Student Name is "+str(self.n)) 

        

p1 = Student()
p1.myfunc("Beso")
p1.myfunc1()
p1.myfunc2()
print(p1.n)