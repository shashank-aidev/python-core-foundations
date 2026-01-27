'''First what we use this exeception handling in python


we use when we don't know which and what problem occurs in future while running the code



Exceptions are Python’s way of saying:
“Something went wrong that normal logic cannot handle.”


'''
try:
    x = int("abc")
except ValueError:
    print("Invalid number")


#3 problems to solve 

#problem 1:
#given this funciton
def safe_divide(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return "DIVIDE_BY_ZERO"
# now we haev to check at a="10" and b=2
#It will give an error becasue "10" is string and can't be divided by 2 
#Invalid valied or string input is not handeled here

# safe_divide("10",2)


#problem 2
#this is code 
def parse_int(s):#here "42" is passed as string 
    try:
        return int(s)# string is cahnegd into integer and given to caller as studied before 
    except ValueError: #When this will be activate 
        return -1
    finally:
        print("parsed")#it will always tun error or not
#this is given to function  as first input  
# x = parse_int("42")
# print(x)

#this is given to function  as second  input
y = parse_int("abc") #it will give an error as string text can't be chanegd into numbers
#so the error will print which is parsed , but why does it printed first after -1 shouldn't it be printing -1 first then why?
print(y)
#Finally doesn't change the retuen value 

#problem 3

def get_item(lst, idx):
    try:
        return lst[idx]
    except IndexError:
        return None
    except Exception:
        return "ERROR"

# '''What is returned for:
get_item([1, 2, 3], 1)
get_item([1, 2, 3], 10)

#At first it will give 2 then it will give None as mentioned it is an indexing error

#and for this input 
get_item(None, 0)
'''It will give "ERROR" because their is no lst to access the index of it'''