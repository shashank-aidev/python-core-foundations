'''It uses when inheritance have if-else conditions which makes it harder to manage:
-> if new object is added then we need to add one more condition:
-> bad design


But using polymorphism is best it makes it clean and easy to manage

'''

#Let's see about inheritance :
'''class Animals:
    def __init__(self,Animal):
        self.Animal=Animal

    def sound(self):
        if self.Animal == "dog":
            print("dog barks:")
        elif self.Animal =="cat":
            print("Cat meows")
        elif self.Animal == "cow":
            print("Cow mows")
class ani(Animals):
    pass

dog=ani("dog")
dog.sound()'''

# above the code is based on inheritance now let's see how it is written in polymorphism

class Animals:
    # def __init__(self,animal):
    #     self.animal=animal it is use to assign value automatically for it we use __init__ function

    def sound():
        print("Animal makes sound :")

class dog(Animals):
    def sound():
        print("Dog barcks:") #here  we can see no if else uses and it is clean and best design 
                              #and we can add and remove the functions and class without changing the code.

class cat(Animals):
    def sound():
        print("cat mewos:")

animal=cat()
dog.sound()


# now let's solve a problem 

class Parent():
    def process(self):
        print("Processign data")
class ChildA(Parent):
    def process(self):
        print("Processing Image")
class ChildB(Parent):
    def process(self):
        print("Processing Video")
allprocess=[ChildA(),ChildB(),Parent()]#here we have created a list of function calling all the classes
for a in allprocess:
    a.process()

first_process=ChildA()
first_process.process()  # so this is polymorphism



#Types of polymorphisms 

'''
Method Overriding

Method overriding happens when a child class inherits from a parent class and provides its own version of the parent’s method.

Uses inheritance
Same method name
Child decides the output
Depends on the object type


Method Overloading (Python-style)

Method overloading happens when the same method name behaves differently based on different inputs (arguments), usually inside the same class.

Inheritance is NOT required
Same method name
Different arguments → different behavior
Depends on the input, not the object


Overriding → Inheritance-based

Overloading → Class-based
'''


#Question on overloading

class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other_pointers):#self means curent a and b values and other_pointers means the other point a and b vlaues "it will have new object"
        return Point(self.a + other_pointers.a,self.b+other_pointers.b)
    #Adding two Points should give another Point, not just a number. that's why here new point object is created
    #means now p3.a=self.a + other.a, p3.b=self.b+other.b

    def __str__(self):#so here self is calling or tlking to the nnew point object which is created above
        return(f"{self.a},{self.b}")# here have to use f tring beacuse the return type should be string
p1=Point(1,2)
p2=Point(2,3)
pp3=p1+p2
print(pp3)


'''
Python already knows that __add__ means + and __str__ means print().
These are predefined (built-in) rules of the Python language.


They are called “special methods” or “dunder methods”

| Operation | Method Python looks for |
| --------- | ----------------------- |
| `+`       | `__add__`               |
| `-`       | `__sub__`               |
| `*`       | `__mul__`               |
| `/`       | `__truediv__`           |
| `==`      | `__eq__`                |
| `<`       | `__lt__`                |
| `print()` | `__str__`               |
| `len()`   | `__len__`               |

This is advanced Python knowledge   '''


class Vector:
    def __init__(self,vect_a,vect_b):
        self.vect_a=vect_a
        self.vect_b=vect_b
    def __add__(self,other_vector):
        return Vector(self.vect_a+other_vector.vect_a,self.vect_b+other_vector.vect_b)
    
    def __str__(self):
        return(f"{self.vect_a},{self.vect_b}")# here have to use "f" tring beacuse the return type should be string
v1=Vector(1,2)
v2=Vector(4,5)
v3=v1+v2
v4=v3+v1+v2
print(v1)
print(v2)
print(v3)
print(v4)
'''

v4 = v3 + v1
or v4 = v3.__add__(v1)
it called def __add__(self, other):

Now Python assigns parameters:

🟢 self becomes → v3

Because v3 is on the left side of +

🟢 other becomes → v1

Because v1 is on the right side of +

So inside __add__ we have:

self  = v3
other = v1'''
#date 3/02/26

class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def __add__(self,other_time):
        return (self.hours+other_time.hours,self.minutes+other_time.minutes)
    def __str__(self):
        return (f"{self.hours},{self.minutes}")
time=Time(4,20)
time2=Time(5,10)
t3=time+time2
print(t3)
print(time)


class Hi:
    def __init__(self,name):
        self.name=name
    def sayname(self):
        return ("Hi "+self.name)
    
h=Hi("shashank")
print(h.sayname())


