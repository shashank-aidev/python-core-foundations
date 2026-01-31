#cheeecking if the numbers appears 2 atlest
# s=[1,2,3,2,4,5,1]
# seen=set()
# for i in s:
#     if i in seen:
#         print("True")
#         break
#     else:
#         seen.add(i)
# print(seen)

#using function

def check(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
n=[1,2,3,1,2,4,5,6]
print(check(n))


#set intersection set removes the dublicate values inside it , 1 of the function of sets
n1=[1,2,3,4,5]
n2=[1,2]
# s=set()
s=set(n1+n2)
print(s)

#problem 3 to find substring from string

s="shashankhello"
# s=input("Enter the string: ")
seen= set()
left=0
max_value=0
start=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left]) # it will remove the value present on the sting which is present in set
        #means s[left] if left is 4 so the 4th element of string == to the element in the set
        left+=1
    
    seen.add(s[right])
    current_value= right-left+1
    max_value=max(max_value,current_value)
#     if right - left + 1 > max_value:
#             max_value = right - left + 1
#             start = left

# print(s[start : start + max_value])


#     if current_value > max_value:
#             max_value=current_value
#             start = left

# print(s[start:start+max_value])
print(max_value)


# 2 more problems

#Problem 1 — Remove Duplicates While Preserving Order
nums = [5,6,3,2,4,1,3]
seen = set()
result = []

for x in nums:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)
print(seen)



# Problem 2 — Length of Longest Subarray With All Unique Elements
n=[1,2,3,1,2,3,4,5]
max_value=0
left=0
seen=set()
start=0
for right in range(len(n)):
    while n[right] in  seen:
        seen.remove(n[left])
        left+=1
    seen.add(n[right])

    current_value=right-left+1
    if current_value > max_value:
        max_value=current_value
        start = left

print(n[start:start+max_value])
print(max_value)


#3 problems

#1
def after(lst):
    lst.append(99)
    # lst=lst+[0]
    return lst # it returs the lst having new object



lst=[1,2,3]
print("Before : ",lst)
print("After :",after(lst))

#problem 2
def f(a=[]): # list is global without using global it acts like global annd it is mutable
    a.append(1)
    return a
print(f())
print(f())



#problem 3

def increment(val):# we are avoiding using global un-wanted
    return val + 1 #here it creates new object that return the value to the caller

x = 10
print(increment(x))
