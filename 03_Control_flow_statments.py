#solveing 3 problems to understant the control flow 

a=[4,5]
b=a

print("a before:",a)
# print(a,end=" ")


#we will create new object for that we will use copy ffunction with moved varibale a like this
a=a.copy() # here a is moved and new onject is created with "a" list copying into a 
#and now if i change something in the a list that will no effect "b" list
a.append(6)
print("a After :",a)
print("b :",b)



#------------------questioon 2---------------------
#in this question we don't have to use the compaire sign , it should output in empty and non-empty, and the inputes are " ",1,0, "text",[1],[]
def check(value):
    if value:
        print("Non-Empty")
    else:
        print("Empty")
value = input("Enter something: ")
check(value)#inputs 0, "0", " ", "text" , [0] , []


#---------Importent-----------
# Q2 — Local vs Global Scope (CRITICAL)
# Code reminder:
x = 5

def change():
    x = x + 1

change()
print(x)

# Correct behavior:
# This code CRASHES before printing anything.
# Actual error:
# UnboundLocalError: local variable 'x' referenced before assignment
# Why?
# Because:
# Python sees x = x + 1
# That makes x a local name
# But you try to read it before assigning
# So Python raises an error

# Correct concept name:
# 👉 Local scope & name binding (UnboundLocalError)
