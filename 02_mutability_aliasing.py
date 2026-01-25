x = [1, 2, 3]
y = x
x.append(4)
print(x)
print(y)

a = 10
print("a=10 : id", id(a))
b = a
a = a + 1
print("a=11 : id", id(a))


'''
in the list which i have created above it have 2 variable pointing to the list [1,2,3] , python creates objects 
of the list , it is mutable so when we so chanegs in the list like above code then the chnages 
are done in the currnent object , it dosn'e create new objects because it is changable.

where as in the integer:
it is not mutable so it create new object for the vlaue and the variable pointing to it 
explaning the above code, a=10 "1 object is created", and b=a it also pointing to the same object
and then a=a+1 : python creates new object which holds a+1 and varibale a is moved to a+1
and if the previour value dosn't have any varibale pointing to it then it will abanded it or treat it as garbage value.

'''