# # # # #Solving the 3 problems

# # # # #problem 1
# # # # def f(x):
# # # #     x.append(4) # here 4 is added in the lst , here it is not talking about x 
# # # #     x = [9, 9] # new object is created with variable x it doesn't do anything

# # # # a = [1, 2, 3]
# # # # f(a)# Here function is called and the lst is passsed 

# # # # print(a)# it will print the output [1,2,3,4]


# # # # #problem 2
# # # # x = 10

# # # # def g():
# # # #     print(x)#it is printing the x but inside function it doesn't recognise it, becasuse x is not declared
# # # #     x = x + 1 # x is not declared so it will give error and not operation will be performed

# # # # g()#Here we can see the unction is called but no parameter is passed or given


# # # # #problem 3
# # # # def h(x):
# # # #     print(x + 1)#here there is increment in the value of x given by the function parameter,6

# # # # y = h(5)
# # # # print(y)#output will be 5, there will be no change globalelly as it is done inside the function
# # # # # 2 of them are wrong 

# # # # #5 problems to solve now 

# # # # #problem 1
x = 5
def f(x):
    x += 1 #increment will happen in the pased paraemeter
    return x # here it will retuen the vlaue to the function changed or not no matter.

print(f(x))#here x = 6
print(x) #here x= 5


# # # # #problem 2
def g(a):
    a[0] += 1# a[0]=a[0]+1, a[0]=1 so it will be a[0]=2
    # print(a[0])
    a = [0, 0]# here new object is created 

x = [1, 2]
g(x)
print(x)#here the output will be [2,2]

# # # #problem 3

def h(a=[]):
    a.append(1)
    return a #it will give the value return to the function

print(h())#here output [1]

print(h())#output will we [1,1]

# # #problem 4
y = 3
def k():
    y = y + 2 # we are incrementing the y without declaring it so it will give an error 
    #Here new object is created because no y parameter is passed in the function called
    return y

# k()
# # #their will be no output because their is no parameter is passed whilw calling the function

# #problem 5
def m(x):#heere -1 is given
    if x > 0:#-1>0 which is false 
        return x #it will retuen the vlaue to the function, but it is skipped because of the condition
    print("neg")#it will print the "neg"
#when their is no return function is present so it return the None vakue to the function
z = m(-1) # z = None
print(z)#it will print the output (None)
