# 5
# 10 15
# 20 25 30 
# 35 40 45 50
a = 5
for i in range(1,5):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=5
    print() 
  
# 5
# 5 10
# 5 10 15
# 5 10 15 20
for i in range(5,25,5):
    for j in range(5,i+1,5):
        print(j,end=" ")
    print()

# a
# a b
# a b c
# a b c d
for i in range(97,101):
    for j in range(97,i+1):
        print(chr(j),end=" ")
    print()

# a
# a b
# a b c
# a b c d
# a b c d e
# a b c d
# a b c
# a b
# a
for i in range(101,96,-1):
    for j in range(97,i+1):
        print(chr(j),end=" ")
    print()
    
#pyramid
#             5
#         10      15
#     20      25      30
# 35      40      45      50
a = 5
for i in range(1,5,1):
    for j in range(1,5-i):
        print("  ",end="  ")
    for k in range(1,(2*i-1)+1):
        print(a,end="  ")
        a+=5
    print()
    
for i in range(1,5,1):
    a=5
    for j in range(1,5-i):
        print("  ",end="  ")
    for k in range(1,(2*i-1)+1):
        print(a,end="  ")
        a = a+5
    print()