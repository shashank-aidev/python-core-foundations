s={10,20,30,30}
s.add(50) # add is used to add single element

s.update([50, 60]) # update is use to add multiple elements

s.remove(20)     # Error if not present
s.discard(30)    # No error
print(s.pop())   # Removes first element
# s.clear()      # Empty set
print(s)


s1={1,2,3,4,56,6}
s2={6,7,8,9,10}
print(s1|s2) #"|" This is union sign that combine the 2 sets as one
print(s1&s2)#"&" This finds the comman elemts in both sets
print(s1^s2)#"^" This removes the comman elements and combine the unique elements
print(s1-s2) #A − B = elements present in A and not present in B


fs = frozenset([1, 2, 3])
# We use this function to make set immutable *IMPORTANT*