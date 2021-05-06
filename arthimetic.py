# numeric operations
def subtraction():
    sub=a-b
    print(sub)
def division():
    div=a/b
    print(div)
def addition():
    print(a+b)
def multiplication():
    print(a*b)
def average():
    print((a+b)/2)
print('enter two numbers:')
a=int(input())
b=int(input())
print('enter the operation such as subtration,addition,multiplication,division,average')
opr=input()
if opr=="subtration":
    subtration()
if opr=="division":
    division()
if opr=="addition":
    adition()
if opr=="multiplication":
    multiplication()
if opr=="average":
    average()
