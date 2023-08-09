#First Method
a = [1,2,3,4,5.6,'KRISHU']
print(a)
print(len(a))
print(type(a))

#Second Method
b = list((1,2,3,2.1,'PATEL'))
print(b)
print(len(b))
print(type(b))

#Third Method
c = [1,2,3,4,5.6,'KRISHU']
print(c[5])
print(c[-5])

#Fourth Method (Replace Value)
d = [1,2,3,4]
d[3] = "Krishu"
print(d)

e = [1,2,3,4]
e[0] = "18"
print(e)

f = [1,2,3,4,5,6,7,8]
print(f[2:6])
f[2:6] = ["RIAAN"]
print(f)

g = [1,2,3,4]
g[0:4] = ["Name","Krishu","Paritosh","Patel"]
print(g)

#Fifth Method (Add Value)
h = [1,2,3,4,5,]
'''
Add value on last position

'''
h.append("KRISHU")
'''
Add value on first position

'''
h.insert(0,"PATEL") 
print(h)


i = [1,2,3,4]
j = [5,6,7,8]
print(a+b)

#Simple List
k = [1,2,3,'KP' , '18']
print(k[3])
k[3]=['Krishu']
print(k)
k.insert(3,'Patel')
print(k)
k.append('Paritosh')
print(k)

#Addition Of 2 index
l=[1,2,3,'KP','18']
m=[1,2,3,4,5,6]

l.extend(m)
m.extend(l)
print(l)

#Delete Method
n=[1,2,3,'KP','18']
n.pop()
n.pop(2)
del(n[0])
'''
Delete Element

'''
print(n)

#Remove Method
o=[1,2,3,4,5,'KPP']
o.remove('KPP')
o.remove(2)
print(o)

#Clear Method
p=[1,2,3,4,5,'KP','18']
p.clear()
print(p)


#Sorting List
q=[55,44,64,2,1,0]
q.sort()

'''
Ascending Order

'''
print(q)
q.sort(reverse=True)
'''
Decending Order

'''
print(q)