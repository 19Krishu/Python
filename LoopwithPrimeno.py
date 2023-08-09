n = 9
for i in range (2,n):
    r = n%i
    if r==0:
        print("This is not a prime number")
        break
else:
    print("This is a prime number")
