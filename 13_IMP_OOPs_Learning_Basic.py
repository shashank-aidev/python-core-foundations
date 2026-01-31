# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     # def show(self,name,amount): method should not cal the A again like here :
#     def show(self):
#         print("Name :",self.name,"\nBalance :",self.balance)

# First=BankAccount("Shashnak",10000)
# First.deposit (int(input("Enter amount to deposit : ")))
# First.show()


# 2 problem clearing basic understanding


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def add_marks(self,extra):
#         self.marks=self.marks+extra
#     def grade(self):
#         if self.marks>=90:
#             print("Grade : A")
#         elif self.marks>=75:
#             print("Grade : B")
#         else:
#             print("Grade : C")
#     def show(self):
#         print("Name : ",self.name,"\nCurrent marks: ",self.marks)

# info=Student("Shashank",50)
# info.add_marks(int(input("enter the marks to be added : ")))
# info.show()
# info.grade()


#problem 3

class Counter:
    def __init__(self,value):
        self.value=value

    def increase(self):
        self.value=self.value+3
    def decrease(self):
        self.value=self.value-1
    def multiply(self):
        self.value=self.value*2
    def show(self):
        print("Here is the current changed value: ",self.value)
A=Counter(int(input("Enter the value : ")))
A.increase()
A.decrease()
A.multiply()
A.show()
B=Counter(int(input("Enter the value : ")))

B.increase()
B.decrease()
B.multiply()
B.show()