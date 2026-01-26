string="Hello I'm Shashank Chauhan"
print(string[0],string[-1])
#[-1] means it's start from last elements of string and it goes backwords

print(string[0:-5])

print(string[:-1])
print(string[-1:])
print(string[0:-1:4])# it is working like this [start : end : point to skip]

print(string[::-1])#it will revesr the string 

# string[0]="H" "It will give error "
string = "H" + string[1:] # it is working becasue it is creating new object and add,
                          # all the ements from the previous object from index 1 not taking *h*
print(string)

s = "abcdefgh"
print(s[6:2:-1])
# start = index 6 → g
# step = -1 → move left
# end = index 2 (exclusive)
# collected: g → f → e → d
# stop before index 2

s = "abcdefgh"
print(s[2:6:-1])
# t will give an error because it will move to left and thatis not possible.