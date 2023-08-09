#Find Second largest value using for...loop
a = [22,33,44,1,2,3,5]
for i in range (len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j]:
            b = a[i]
            a[i] = a[j]
            a[j] = b
print("Maximum No : ",a[-1])
print("Second Largest No : ",a[-2])