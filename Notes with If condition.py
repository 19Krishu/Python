amt = 5200
if amt%100 == 0:
    if amt >= 2000:
        notes = amt // 2000
        print("2000 notes : ",notes)
        amt = amt%2000
        
    if amt >= 500:
        notes = amt // 500
        print("500 notes : ",notes)
        amt = amt%500
        
    if amt >= 200:
        notes = amt // 200
        print("200 notes : ",notes)
        amt = amt%200
        
