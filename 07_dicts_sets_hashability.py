# Core idea #1 — Dictionary keys
# d = {1: "a", (2, 3): "b"}   # OK
# d[[1, 2]] = "c"            # ERROR


# Why?
# Keys must be hashable
# Lists are mutable
# Mutable → hash can change → dictionary breaks
'''Hashable vs Immutable (NOT the same)

Immutable objects are often hashable
But hashable means:
hash value never changes during lifetime

Examples:
int, str, tuple (if elements are hashable) → ✅
list, dict, set → ❌
frozenset → ✅'''

#Examples

d = {1: "a", "x": 10}
d[1] = "b"

s = {1, 2}
s.add(3)
print(d)
print(s)

#solving 3 questions on it 

#problem 1
a = (1, 2)
b = (1, [2])

d = {}
d[a] = "ok" # here we are give a =(1,2) as key and then assigning value "ok" to it 
# d[b] = "fail" #it will fail becasue [2] in b is not hasable 

#problem 2

x = (1, 2)
d = {x: "value"}

x += (3,)#x=x+3 this is not effect the current object

print(d) # it will give output {(1,2):"value"}


#Probelm 3
# Frist the code will execute line by line 
a = [1, 2]
b = tuple(a) # lst is changed into tuple which is hashable
s = {b} #here tuple chanegs into dictionary which have only keys in ti

a.append(3) # it will append the element in the lst but not in the dictionary

print(s)

