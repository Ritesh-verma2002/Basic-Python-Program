amount=int(input("Enter the amount:"))
if amount >= 25000:
    amount = amount-amount*20/100
elif  10000 < amount < 25000:
    amount = amount-amount*10/100
else: amount=amount-amount*5/100
print("Payable amount =",amount,"Rs")
