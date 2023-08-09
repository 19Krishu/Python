#Simple Function
def name():
    print("This is our first function")
name()

print("-------------------------------------------------------------------------------")

#User Define Function
#1. Parametarize / Argument Required function
def add(a,b,c,d):
    print(a,b,c,d)
add(11,11,22,33)

def add1():
    return "Hello"
print(add1())

#2. Default Argument Function
def name(a,b,c=33):
    print(a,b,c)
name(1,2,66)
    
#3. Variable Length Function
#This function return value 
def fun(*arg):
    print(arg)
    print(type(arg))
    print(arg[2])
    print(arg[0] + arg[1] + arg[2] + arg[3])
fun(1,2,3,4)    

#4. Key word variable lenght function
def multi(**kwarg):
    print(kwarg)
    print(type(kwarg))
    print(kwarg['b'])
    print(kwarg['a'] + kwarg['b'] + kwarg['c'])
multi(a=1,b=9,c=2)
    
print("-------------------------------------------------------------------------------")

#Pattern using Function
print(ord('a'))
print(ord('A'))
for i in range(97,101):
    for j in range(97,i+1):
        print(chr(j), end= ' ')
    print()
    
print("-------------------------------------------------------------------------------")

#Lambda Function 
a=lambda a,b,c:a+b+c
print(a(1,2,3))

#Syntax of Lambda
'''
variable = lambda function : expression
print(variable(Pass value to parameter))

'''