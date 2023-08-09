amt = int(input("Enter Amount : "))
if amt%100 == 0:
    if amt >= 5000:
        notes = amt // 5000
        print("5000 notes : ",notes)
        amt = amt%5000

    if amt >= 1000:
        notes = amt // 1000
        print("1000 notes : ",notes)
        amt = amt%1000

    if amt >= 500:
        notes = amt // 500
        print("500 notes : ",notes)
        amt = amt%500

    if amt >= 100:
        notes = amt // 100
        print("100 notes : ",notes)
        amt = amt%100

    if amt >= 50:
        notes = amt // 50
        print("50 notes : ",notes)
        amt = amt%50

else:
    print("Invalid Amount")
