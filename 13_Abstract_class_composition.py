# ============================================================ OOP MASTER
# NOTES Abstract Classes | Inheritance | Composition | Polymorphism
# ============================================================

# WHAT WE LEARNED

# 1.  Abstract Base Classes (ABC)
# 2.  Abstract Methods
# 3.  Inheritance (IS-A)
# 4.  Composition (HAS-A)
# 5.  Dependency Injection
# 6.  Polymorphism
# 7.  Encapsulation
# 8.  Real-world mini projects

# ============================================================ QUESTION 1:
# Basic Abstract Class Rule Enforcement
# ============================================================

from abc import ABC , abstractmethod

class Parent(ABC):

    @abstractmethod
    def First_rule(self):
        pass


class child(Parent):
    def First_rule(self):
        print("This is first rule")


c=child()
c.First_rule()

# ============================================================ QUESTION 2:
# Abstract Method with Parameters
# ============================================================

class Notification(ABC):
    @abstractmethod
    def  send(self, message):
        pass

class EmailNotificatin(Notification):
    def send(self,message):
        print(f"This is the Mail notification {message}")

class SMSNotification(Notification):
    def send(self,message):
        print  (f"This is SMS Notification {message}")

lst=[EmailNotificatin(),SMSNotification()]
for a in lst:
    a.send("Hello")

# ============================================================ QUESTION 3:
# Vehicle Abstract Example
# ============================================================

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        print(f"Bike is started.")
    def stop(self):
        print(f"Bike is stooped")

class Car(Vehicle):
    def start(self):
        print(f"Car is started.")
    def stop(self):
        print(f"Car is stooped")

v=Car()
v.start()
v.stop()

# ============================================================ QUESTION 4:
# Composition (School & Student)
# ============================================================

class student:
    def __init__(self,name):
        self.name=name

class School:
    def __init__(self):
        self.students=[]
    def add_students(self,student):
        self.students.append(student)
    def show_students(self):
        for s in self.students:
            print(s.name)

s1=student("shashank")
s2=student("sejal")

school=School()
school.add_students(s1)
school.add_students(s2)
school.show_students()

# ============================================================ QUESTION 5:
# Library & Book
# ============================================================

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def get_details(self):
        return f"Title:{self.title}\nAuthor:{self.author}"

class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,books):
        self.book.append(books)
    def show_books(self):
        for boo in self.book:
            print(f"{boo.get_details()}")

book1=Book("Hello book","Shashank Sir")
book2=Book("Another Book","New book suthor")

library=Library()
library.add_book(book1)
library.add_book(book2)
library.show_books()

# ============================================================ QUESTION 6:
# Engine & Car (Composition)
# ============================================================

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car moving")

c=Car()
c.drive()

# ============================================================ QUESTION 7:
# Animal Inheritance
# ============================================================

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} Dog barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Cat meows")

d=Dog("Bunty")
d.speak()

c=Cat("Pussy")
c.speak()

# ============================================================ QUESTION 8:
# Student HAS-A Laptop
# ============================================================

class Person:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        print(self.name)

class Laptop:
    def turn_on(self):
        print("Laptop turnned on")

class Student(Person):
    def __init__(self,name,laptop):
        super().__init__(name)
        self.laptop= laptop

    def study(self):
        self.laptop.turn_on()
        print(f"{self.name} Student is studying :")

laptop = Laptop()
student = Student("Rahul",laptop)
student.study()

# ============================================================ QUESTION 9:
# Course, Student, Professor
# ============================================================

class Person:
    def __init__(self,name):
        self.name=name

    def get_name(self):
        print(self.name)

class Student(Person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course

    def attend_class(self):
        print(f"{self.name} is attending the class")

class Professor(Person):
    def __init__(self, name,course):
        self.course=course
        super().__init__(name)

    def teach(self):
        self.course.start_class()
        print(f"{self.name} is teaching the students ")

class Course:
    def __init__(self,course_name):
        self.course_name=course_name
    def start_class(self):
        print(f"Class Started for  {self.course_name}")

course = Course("OOP")

student = Student("Rahul", course)
professor = Professor("Dr. Sharma", course)

professor.teach()
student.attend_class()

# ============================================================ 
# QUESTION  10: Bank Account & Payment
# ============================================================

class BankAccount:
    def __init__(self,balance):
        self._balance=balance

    def withdraw(self,amount):
        if amount>0:
            if self._balance<amount:
                print("Insufficient balance")
            else:
                self._balance-=amount
                print("Amount withdrawn")

    def total(self):
        print(f"Total balance left {self._balance}")

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self,amount,bank):
        self.bank=bank
        self.amount=amount
    def pay(self):
        print(f"{self.amount} is paid by Card")
        self.bank.widthraw(self.amount)

class UPIPayment(PaymentMethod):
    def __init__(self,amount,bank):
        self.amount=amount
        self.bank=bank
    def pay(self):
        print(f"{self.amount} is paid by UPI")
        self.bank.withdraw(self.amount)

bank=BankAccount(10000)
pay=UPIPayment(50000,bank)
pay.pay()
bank.total()

# ============================================================ 
# QUESTION 11: ATM & Bank
# ============================================================

class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    def Widthraw(self,amount):
        if amount>self._balance:
            print("Insufficenet balance")
            return False
        self._balance-=amount
        print("Widthraw is successful")
        return True
    def get_balnce(self):
        print(self._balance)

class ATM:
    def __init__(self,account):
        self.account=account
    def withdraw_cash(self,amount):
        self.account.Widthraw(amount)

bank=BankAccount(1000)
atm=ATM(bank)
atm.withdraw_cash(300)
atm.withdraw_cash(800)
bank.get_balnce()

# ============================================================ 
# QUESTION 12: Mini Uber Project
# ============================================================

class Vehicle(ABC):
    def __init__(self,name):
        self.name=name
    def get_driver(self):
        print(f"The driver name is {self.name}")
    @abstractmethod
    def calculate_fare(self,distance):
        pass

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def calculate_fare(self, distance):
        return distance*10
        
class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    
    def calculate_fare(self, distance):
        return distance*5

class Ride:
    def __init__(self,vehicle,distance):
        self.vehicle=vehicle
        self.distance=distance
    def start_ride(self):
        print(f"Ride started with {self.vehicle.name}")
    def End_ride(self):
        print(f"Ride Endead with {self.vehicle.name}")
        print(f"Total fare price {self.vehicle.calculate_fare(self.distance)}")

car=Car("shashank")
bike=Bike("Chauhan")

ride1 = Ride(car,10)
ride2= Ride(bike,30)

ride1.start_ride()
ride2.start_ride()
ride2.End_ride()
ride1.End_ride()