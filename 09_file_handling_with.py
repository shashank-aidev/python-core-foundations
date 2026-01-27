'''
Their are few things that i need to undersatand
We can open file in 2 ways:

1: using open()
2: using with

but their is a catch while using open we have to close the file at the end no matter the opperation
otherwise , if the code crashes their file content can be corrupted 

but using "with" to assecc file we don't have to close the file it will close automatically

'''
# f = open("file.txt","w")
# f.write(" Chauhan")
# # print(f.readlines())
# f.close() #important


#using with

# with open("file.txt","r") as f:
#     print(f.read())

'''We can use "a" to write more content inside the file without deleting the previous data


| Mode   | Meaning       | Behavior        |
| ------ | ------------- | --------------- |
| `"r"`  | Read          | File must exist |
| `"w"`  | Write         | Overwrites file |
| `"a"`  | Append        | Adds to end     |
| `"r+"` | Read + Write  | No overwrite    |
| `"w+"` | Write + Read  | Overwrites      |
| `"a+"` | Append + Read | Adds to end     |

'''

with open("file.txt","r") as f: # you can create any file or access it by the given path
    for line in f:
        print(line)



#Solving 3 problems to understed it more 


#problem 1  image an data.txt is file and content is 
#A
#B  is written on it
with open("data.txt", "w") as f:
    f.write("C\n") # this will clear the whole file and rewrite the file again
    # It will write again the file with "C"

with open("data.txt", "a") as f:
    f.write("D\n") #now it will update the existing file So it will and "D" after "C".
#output will be C\n D


#problem 2
with open("data.txt", "r") as f:
    print(f.readline())#It will print the first line of the file 
    for line in f:
        print(line)#It will peint the whole content of the file, except the first line which is allready readed
#output will be 
'''
one
two
three'''

#problem 3
with open("data.txt", "r") as f:
    content1 = f.read()#it read the whole file 
    content2 = f.read()# it also does the same 

print(content1)
print(content2)
#output will be :
'''
hello 
world

As i was thinking it will not print the same content of the file again and agian i wonher why?
'''


'''
#Important
First read() → reads whole file

#file
Hello 
world | <- This is pointer

Pointer now at EOF
Second read() → nothing left → returns ""

'''