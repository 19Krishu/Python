amt=5000
notes=amt//2000
print("2000 notes : ",notes)

amt=amt % 2000
notes=amt//500
print("500 notes : ",notes)

amt=amt % 500
notes=amt//200
print("200 notes : ",notes)

amt=amt % 200
notes=amt//100
print("100 notes : ",notes)
