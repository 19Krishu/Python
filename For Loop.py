#For i in range (start , end , step):
for i in range(1,11,1):
    print (i)

#Table for 2
for i in range(2,21,2):
    print (i)

print("Table of 2")


a=0
b=1
for i in range(2,20,1):
    c=a
    a=b
    b=c+b
    print(a)
