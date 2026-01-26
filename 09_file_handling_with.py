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

with open("file.txt","r") as f:
    for line in f:
        print(line)