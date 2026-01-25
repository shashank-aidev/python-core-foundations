student = {"name": "Rahul","name":"chauhan","age": 20,"course": "Python"} #it store th vlaue like this {"key":"value"} , and it is mutable
# student.pop("name")#it removes the key and the vlaue of the selected key
# d.popitem()         # removes last item
# d.clear()           # empty dictionary
# print(student)
# print(student.get("salary"))        # None
# print(student.get("salary", 0))     # 0
# safe way to search keys if you'r not shure that it is available or not to use get function
squares = {x: x*x for x in range(1, 6)} #This prints squres ofeacch elements until the range given
print(squares)


for s in student.values():
    print(s)

for s in student.keys():
    print(s)

for s in student:# this automaticly prints the keys without use .keys after students if it has multiple keys with same name it will print only once 
    print(s)
    
