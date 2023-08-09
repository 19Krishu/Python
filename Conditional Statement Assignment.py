subject1=int(input("Enter Sub1 marks : "))
subject2=int(input("Enter Sub2 marks : "))
subject3=int(input("Enter Sub3 marks : "))
subject4=int(input("Enter Sub4 marks : "))
subject5=int(input("Enter Sub5 marks : "))
subject6=int(input("Enter Sub6 marks : "))

print("Total of subjects : ",subject1+subject2+subject3+subject4+subject5+subject6)

avg=(subject1+subject2+subject3+subject4+subject5+subject6)/6

if(avg>80 and avg<100):
    print("Grade A")

elif(avg>60 and avg<80):
    print("Grade B")

elif(avg>40 and avg<60):
    print("Grade C")

elif(avg<40):
    print("Fail")
