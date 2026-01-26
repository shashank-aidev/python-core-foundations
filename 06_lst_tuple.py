# # a = [1, 2]
# # b = [a, a] # we we haev to know something here b creates to refrence which are pointing to the same elements as a
# # # b[0]->a & b[1]-> a So there are 2 different name pointing the same object , no new object is created


# # b[0].append(3)
# # #b[0]->a and a is[1,2] then and adding new element 3 is changing the lst a and overall lst

# # print(a)
# # print(b)
# # # So, a and b are same output

# # x = [[1, 2], [3, 4]]
# # y = x.copy()#***Important*** copy() function just copies the outer list not the inner lst which means
# # #her y= c.copy() copy the outer lst creating new object and inside it , it will be same as x 
# # # which means y = [ [1,2],[3,4] ] asscessign y[0]=[1,2] changing in this will automaticlly change in x
# # '''Why?
# # x.copy() creates a shallow copy
# # Outer list is new
# # Inner lists are shared
# # y[0] and x[0] point to the same inner list
# # Mutation affects both''' 

# # y[0].append(99)

# # print(x)
# # print(y)
# a=[0]
# b=[a]
# c=b*2
# print(b)

# x = [[1, 2], [3, 4]]
# y = x.copy()

# y[0] = [9, 9]
# y[1].append(5)

# print(x)
# print(y)




# #--Questions ---

# a = [0]
# b = [a]
# c = b * 2

# c[0].append(1)

# print(a)
# print(b)
# print(c)

# '''Tasks

# Exact output (3 lines)
# How many list objects exist?
# Why does b * 2 make this dangerous?'''

# x = [[1, 2], [3, 4]]
# y = x.copy()

# y[0] = [9, 9]
# y[1].append(5)

# print(x)
# print(y)
# '''Tasks
# Exact output
# Which operation breaks aliasing?
# Which operation mutates shared state?'''



# t = ([1, 2], [3, 4])
# t[0].append(99)
# t[1] = [7, 8]
# '''Tasks
# Does this code crash? YES / NO
# If YES, at which line and why?
# What is the state of t just before the crash?'''


# def f(x):
#     x[0].append(5)
#     x = [[0, 0]]
#     return x

# a = [[1, 2]]
# b = f(a)

# print(a)
# print(b)

# '''Tasks
# Exact output
# Why does a change but later reassignment not affect it?
# Which concept explains this fully?'''




# '''Q1:
# Output: a= [0,1], b=b[[0,1]], c=[[0,1],[0,1]]
# Objects:2
# Explanation:b*2 it creats multiple lst inside a list it means this [[a],[a]] , where a =[0], befor eappend.

# Q2:
# Output: x = [[1,2], [3,4,5]], y= [[9,9], [3,4,5]]
# Alias broken by:y[0]=[9,9]
# Shared mutation by:y=x.copy( )

# Q3:
# Crash: yes
# Line:t[1] = [7,8] it creats new object inside tuple , where tuple is immutable.
# State before crash: t= ([1,2,99],[3,4])

# Q4:
# Output:a = [[1,2,5]], b = [[0,0]]
# Explanation:because inside function x = [[0,0]] creating new object inside ffunction it is not related to previous x .
# Concept: Hidden Alias via Function

# Q5:
# Works:no
# Reason:because in Dictionary there will be onlly 1 key but it can have multiple values.
# Required property:{"key":"value"}'''

# #i have answer only 1 correct 4 and all are wrong just minar mistakes

# #let's move to 7 questions 
# #problem 1
a = [1, 2, 3]
b = a[:]
b.append(4)

print(a)
print(b)
# a and b will be different because here for b  new object is created and the output will bw
#a=[1,2,3], b=[1,2,3,4]

#problem 2

x = [[0], [1]]
y = x[:]# Here new object is created but for only the outer lst but they share the inner lst like
# x = [0],[1]
#so y= [ [0], [1] ]
y[0].append(9)
#after this line y=[[0,9],[1]]
print(x) # x = [[0,9],[1]]
print(y) # y = [[0,9],[1]]


#problem 3

t = ([],) # Here tuple is immutable but the list inside is mutable So it will work like this
t[0].append(1)# t = ([1],)
t[0].append(2)# t =([1,2])

print(t) # t = ([1,2], )


#problem 4
a = [[1], [2]]

for x in a: # here x will have each element of a like this [1] and the [2]
    x = x + [9] # Here x is seen as new varibale 
    # print(x)

print(a) #output will be : [[1],[2]] there will be not change because chaneg is done in the x localy

#problem 5 
a = [[1], [2]]

for x in a:
    x.append(9)# here it adds [9] in each element , no new object is created 

print(a) # output will be [[1,9],[2,9]]


#probelm 6
def add_noise(data):
    data[0].append(99) # here the data is added in the old object 
    data = [[0]]# here new object is created 
    return data # returing the new object which will go into the y

x = [[1]]
y = add_noise(x)

print(x) # [[1,99]]

print(y) #[[0]]


