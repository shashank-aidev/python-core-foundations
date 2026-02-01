# class parent:
#     def __init__ (self,number):
#         self.number=number
#     def increase(self):
#         self.number=self.number+2
#     def show(self):
#         print(self.number,"<---This is the number")



# class child(parent):
#     def multiply(self):
#         self.number=self.number*3
#     def show(self):
#         print("Final value is : ",self.number) #here the orviding is happening child overrides the parent show funtion

# a=child(5)
# b=child(4)
# a.increase()
# b.increase()
# b.multiply()
# a.show()
# b.show()
#inharitence using super() function

# class Account:
#     def __init__(self,balance):
#         self.balance=balance # here we are assing the value to the current object

#     def deposit(self):
#         self.balance=self.balance+100
#     def show(self):
#         print("Parent balanace : ",self.balance)


# class PremiumAccount(Account):
#     def __init__(self,balance): # here we have construct the child object
#         super().__init__(balance)
#         self.child_balance=self.balance+500 #**IMPORTANT** child_balance *here we will create differnet variable name of child to print it's balance
#     def deposit(self):
#         super().deposit()
#         self.child_balance+=200
#     def show(self):
#         super().show()
#         print("This is child account : ",self.child_balance)

# first=PremiumAccount(100)
# first.deposit()
# first.show()



#multi inheritance

'''
parent1
parent2

child->parent1
child->parent2
'''

class Father:
    def father_skill(self):
        print("Father skill : Driving")
class Mother:
    def mother_skill(self):
        print("Mother skill : Cooking")

class child(Father,Mother):
    # super().Father()
    # super().Mother()
    def skill(self):
        self.father_skill()
        self.mother_skill()
        
c=child()
c.skill()


# new porblem based on multiple inheritance

class Writer:
    def write(self):
        print("Writes Articles ")
class Speaker:
    def speak(self):
        print("Giving speachess")


class Influencer(Writer,Speaker):
    def show_skills(self):
        print("Influencer skills :")
        self.write()
        self.speak()
i=Influencer()
i.show_skills()
