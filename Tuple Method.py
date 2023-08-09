#Tuple Method
a=(1,2,3,'KP','KPP')
print(a[2])
print(a[4])

#Tuple List
b=(1,2,3,'KP','KPP')
b=list(a)
print(type(b))
b[3]=4
b=tuple(b)
print(b)
print(type(b))

#Add 2 tuple
c=[1,2,3,4,5]
d=[6,7,8,9,10]

c.extend(d)
d.extend(c)
print(c)
