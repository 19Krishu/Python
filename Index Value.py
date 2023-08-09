a = ['a','b','c',5]
print(a[3])


b = [1,2,3,[2,'Ram'],11,'R']
print(b[3][1])


c = [1,2,3,[1,2,3,['R','A','D',77],44],11]
print(c[4])
print(c[3][3][2])
print(c[3][4])


d = ['a','b',{'name':'Krishu','age':[60,77,50,45]}]
print(d[2]['age'][2])


e = [1,2,3,{'name':{'name1':{'name2':['Krishu','Patel','V','P']}}}]
print(e[3]['name']['name1']['name2'][2])


f = ['a','b','c',{'name':[1,2,{'name1':[{'name2':[1,2,{'age':60}]}]}]}]
print(f[3]['name'][2]['name1']['name2'][2]['age'][0])
