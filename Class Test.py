#Q1.
# ****1
# ***12
# **123
# *1234
rows = 5
for i in range(1, rows):
    num = 1
    
    for j in range(rows, 0, -1):
        if j > i:
            print("*", end='')
        else:
            print(num, end='')
            num += 1
        if j > i:
            print("", end='')
    print("")

#Q2.

phy = 70
chem = 80
math = 66
eng = 77
hindi = 50

tot = (phy+chem+math+eng+hindi)
avg = (phy+chem+math+eng+hindi)/5

if(avg>40 and avg<60):
    print("Grade C")

elif(avg>60 and avg<80):
    print("Grade B")

elif(avg>80 and avg<100):
    print("Grade A")

else:
    print("Fail")
    

#Q3.

a = "Welcome to Gujarat University"
print(len(a))
print(a[10:29:1])
# x=0
# while x<len(a):
#     print(a[x])
#     x=x+1
    

# #Q4.

n = 6
fact = 1

for i in range(1,n+1):
    fact = fact * i

print ("The Factorial of 6 is : ",fact)


# #Q5.
# '''
# *Comparison Operators

# == Equal to
# != Not Equal to
# > Grater than
# < Less than
# >= Grater than equal to
# <= Less than equal to


# *Logical Operators

# && and
# || or
# not

# *Identity Operators

# is
# is not

# '''


