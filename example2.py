# Scholarship
mark = float(input("Enter the mark:"))
if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 90:
    print("Full Scholarship")
elif mark >= 80:
    print("Half Scholarship")
elif mark >= 70:
    print("Quarter Scholarship")
else:
    print("No Scholarship") 

#====================================================
# Discount 
purchase_amount = float(input("Enter the amount of purchase:"))
if purchase_amount >=10000:
    discount = purchase_amount * 0.25
elif purchase_amount >= 5000:
    discount = purchase_amount * 0.15
elif purchase_amount >= 2000:
    discount = purchase_amount * 0.05
else:
    discount = 0
payable_amount = purchase_amount - discount
print(f"Your discount is {discount} and payable amount is {payable_amount}")                
