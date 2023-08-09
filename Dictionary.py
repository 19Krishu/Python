Dict = {'Name':'Krishu','Age':18}
print(Dict)
print(Dict['Name'])
print(Dict['Age'])
print(type(Dict))

print('-----------------------------------------------------------------------------------')

Dict1 = {'Name' : 'Krishu' , 'Marks' : [1,2,3,4,5,6,7,8,9,10]}
print(Dict1)
print(Dict1['Marks'])
print(Dict1['Marks'][3])
print(Dict1['Marks'][8])
print(Dict1['Marks'][6])

print('-----------------------------------------------------------------------------------')
 
Dict2 = {'Name' : 'Nupur' , 'Age' : {'Age1' : [1,2,3,4,5,6,7,8,{'Name':'Krishu'}]}}
print(Dict2)
print(Dict2['Age']['Age1'][8]['Name'])

print('-----------------------------------------------------------------------------------')

Dict3 = {'Roll' : {'Roll':19,'Name':'KPP'}}
print(Dict3)
print(Dict3['Roll']['Name'])

print('-----------------------------------------------------------------------------------')

Dict4 = {'Name' : 'Krishu','Age' : 18,'City' : 'Ahmedabad'}
print(Dict4)
print(type(Dict4))
print(Dict4['Name'])
Dict4['Name'] = 'Krisha'
print(Dict4)
Dict4['Year'] = 2022
print(Dict4)
Dict4['Year1'] = 2004
print(Dict4)
print(Dict4.get('Year'))
print(Dict4.get('Year1'))
print(Dict4.keys())
print(Dict4.values())
print(Dict4.items())
del(Dict4['City'])
print(Dict4)
Dict4.pop('Name')
print(Dict4)
Dict4.popitem()
print(Dict4)

print('-----------------------------------------------------------------------------------')

