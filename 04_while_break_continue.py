# #------------------------------Loops-------------------------------------#
# x=10
# while x>=1:
#     print(x)
#     x=x-1



# #------------**Golden rule**------------#
# # If a loop condition depends on a variable, 
# # that variable MUST be updated before continue can execute.


# #problem 2

# for i in range (10):
#     print(i)
#     if i%2==0:
#         continue
#     if i==7:
#         break


# #problem 3
# i=0
# while(i>=0):
#     if(i<0):
#         break
#     else:
#         i=int(input("Enter number :"))
        
        
    
    
# #problem 4
# x = 0
# while x < 5:
#     x += 1
#     if x == 4:
#         continue
#     print(x)


#---------3 Questions for practicing the understanding------
x=1
while (10>x):
    
    if x==4 or x==7:
        x=x+1 # we have to do increment before continue other wise the value of x will never changes
        #it will be infinite loop.
        continue
    if x==9:
        break
    print(x)
    x=x+1
    




#Problem 2


user=int(input("Enter number :"))
while ( user>=0):
    if user==0:
        user=int(input("Enter number :"))
        continue
    print(user)
    user=int(input("Enter number :"))




#problem 3


for i in range(1,20):
    if i%3==0:
        continue
    if i%7==0:
        break
    print(i)