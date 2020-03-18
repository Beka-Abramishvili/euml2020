import random

'''
print('Hello World')
x=12
print(x+12)
s='Elene'
print("me var "+s)
y=13.9
print(y)
z=True
print(type(x))
t = complex(2, 3)
print(t)
print(random.randrange(1,10))
d = random.randrange(0, 100)
thislist = ["apple", 
            "banana", 
            "cherry", 
            "orange", 
            "kiwi", 
            "melon", 
            "mango"]
print(thislist[2:4])
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["model"])

x=45
if x<20:
    print(x*2)
    print("hello")
else:
    print(x-30)
    
x=3
  
if x>5:
    print(x+1)
elif x>2:
    print(x+2)
else:
    print(x)

i=0
while i<12:
    print(i)
    i=i+1    
for x in range(2, 6):
  print(x) 
'''

def my_function1():
    print("Hello from a function")
    
def my_function2():
    return 12    

my_function1(); 

print(my_function2());  

def my_function3(a, b):
    return a+b

x = lambda a, b: a + b
print(x(3, 4))
    






















