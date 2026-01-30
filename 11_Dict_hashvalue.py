'''



Dictionary uses hashing to map keys to values.
Hashable means the hash value does not change.
Immutable objects are safe as keys.
Counting with dictionaries is faster than lists.



'''

# count = {}
# nums = [1, 2, 2, 3]

# for x in nums:
#     count[x] = count.get(x, 0) + 1
# print(count)
'''
dictionary.get(key, default)

If key exists in the dictionary, return its value.
If it does NOT exist, return default.


count.get(1, 0)
 it means get the value and key 1 if not hen give 0""'''


# nums =  [3, 1, 4, 1, 5, 9, 3]
# dict={}
# # Output: 1
# for i in nums:
#     # print(dict[i]) # if print i then it will print the "keys", but for this it will print the values print in the keys
#     # print(nums [i] =nums.get(i,0)+1) ERROR
#     if i in dict: #It will find the keys , to find the values in keys we have to write dict[i] it will give the values in that dict
#         dict[i]=dict[i]+1
        
#     else:
#         dict[i]=1
# for i in dict:
#     if dict[i]==2:
#         print(dict[i],"<--found it")
#         break


#solution 1
lst=[1,2,3,4,5,1]
find={}

for i in lst:
    if i in find:
        find[i]=find[i]+1
        if find[i]==2:
            print(i,"<--here's the repeating element")
            break
    else:
        find[i]=1

#solution 2 I will print first non repreating cahracter in the string

s="shashank"
cap={}

for i in s:
    if i in cap:
        cap[i]=cap[i]+1
    else:
        cap[i]=1

for i in s:
    if cap[i]==1:
        print(i)
        break

#solution 3it will find if the 2 strings are anagram or not 
# s=input("enter string 1:")
# t=input("enter string 2:")
s = "silent"
t = "lister"

f = {}

if len(s) != len(t):
    print("not anagram")
else:
    # count characters in s
    for ch in s:
        if ch in f:
            f[ch] = f[ch] + 1
        else:
            f[ch] = 1

    is_anagram = True

    # reduce counts using t
    for ch in t:
        if ch not in f:
            is_anagram = False
            break
        f[ch] = f[ch] - 1
        if f[ch] < 0: # checking if counting is zero or smaller then that 
            is_anagram = False
            break

    if is_anagram:
        print("Yes")
    else:
        print("No")



# just example of break using in about code 
# nums = [5, 7, 9, -1, 3]
# f={}
# for n in nums:
#     if n < 0:
#         # break # it will not go to the element 3
#         continue # It will escape the element and move to the next 
#     print(n)
# for i in nums:
#     f[i]=f.get(i,0)+1
# print(f)


# To clear  the concept we will solve 5 move problems
#problem 1 Majority Element (Counting Core)
n=[1,2,3,2,4,2,5,2,4,1]
f={}
for i in n:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1

max_value=0 # to store the max value
for i in f:
    if f[i]>max_value:
        max_value=f[i] # it will store the max value of the dictionary
        keys=i # it will store the max value key
print(keys,":", max_value, "<--here is the max value and the key")

#problem 2 Check If All Characters Have Unique Frequency  not complete!!!
print("\n problem 2\n")
# s=input("enter the string to ind each frequency : ")
# s="string"
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# # print(d)
# setup=set()
# # print(len(s))
# for i in range(4):
#     setup.add(i)
# print(setup)

#i don't understand it 

print("\n program 3 \n")
#To find the multipple numbers appear more than 1
n=[1,2,3,4,1,2,5,6,7]
# n=[]
# items=int(input("enter how many emelents you won't to enter in list :"))
# for i in range(items):
#     n.append(input("enter element:"))
# print(n)
f={}
for i in n:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1

lst=[]
for i in f:
    if f[i]>1:
        lst.append(i)
        # print(i,":",f[i])
print(lst)

print("\n problem 4\n")
#problem 4 Word Pattern Match
s="a  bb bb a"
# s=input ("give a sentence : ")
d={}
d1={}

words=s.split()
# print(len(words))
# print(words[0])
for i in range (len(words)):
    d[i]=words[i]
print(d)
print("opposit dictionary:")

j=0
for i in range(len(words)-1,-1,-1):
    d1[j]=d[i]
    j+=1
print(d1)
check=True
# print("finding the pattern:")
for i in range(len(words)):
    if d[i]!=d1[i]:
        # print(d,di)
        check=False
        break
    
if check:
    print("It is in pattern:")
else:
    print("not in pattern:")

#problem 5 Group Characters by Frequency Input:  "aabccc" Output: {2: ['a'], 1: ['b'], 3: ['c']}
# print("\n Problem 5\n")
# s="stinginput"
# f={}
# changed_dict_into_list={}
# for i in s:
#     if i in f:
#         f[i]=f[i]+1
#     else:
#         f[i]=1
# print(f)
# for i in f:
#     changed_dict_into_list[f[i]]=list[i]
# print(changed_dict_into_list)
#my logic is wrong in this above


s = "aaaabcccc"

f = {}
new = {}

# Step 1: count frequency
for ch in s:
    if ch in f:
        f[ch] += 1
    else:
        f[ch] = 1

# Step 2: group by frequency
for i in f:
    if f[i] in new: # f[i] menas value at i key in f
        new[f[i]].append(i) # here we are storing the sppen value in the list don't write new[f[i]]=new[i].append(i) we are not creating new object or value it will give error 
    else:
        new[f[i]]=[i]
print(new)