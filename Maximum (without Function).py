#Find maximum value using while...loop
a=[22,33,44,1,2,3,5]
max1 = a[0]
i = 0
while i<len(a):
    if max1<a[i]:
        max1=a[i]
    i+=1
print("Maximum No : ",max1)

#Find maximum value using for...loop
b=[22,33,44,1,2,3,5]
max2 = b[0]
for i in range(len(b)):
    if max2<b[i]:
        max2=b[i]
print(max2)
