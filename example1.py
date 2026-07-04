age=int(input("Enter the age:"))
if age>=18:
    print("You are adult")
else:
    print("You are minor")    

#===========================================
#is operator(identity operator)
x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=x
print(x is y)
print(x is z)

#==============================================
# in operator(membership operator)
nums = [1,2,3,4,5]
print(4 in nums)
print(12 in nums)
str1= "Python"
print("y" in str1)

#==================================================
#Bank
pin="1234"
entered_pin=input("Enter the pin:")
if entered_pin == pin:
    withdraw_amount = float(input("Enter the amount to be withdraw:"))
    balance= float(input("Enter the balance:"))
    if withdraw_amount <= balance:
        balance = balance - withdraw_amount
        print("Current balance:",balance)
    else:
        print("Insufficient balance")    
else:
    print("Invalid pin")

#======================================================
# Average Mark
chem=float(input("Enter the mark of Chemistry:"))
bio=float(input("Enter the mark of Biology:"))
mala=float(input("Enter the mark of malayalam:"))
engl=float(input("Enter the mark of English:"))
avg=(chem+bio+mala+engl)/4
print("Average Mark:",avg)
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
elif avg >= 50:
    print("E")
else:
    print("Fail")                       
