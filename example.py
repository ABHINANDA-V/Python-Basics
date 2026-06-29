# Check whether a number is greater than or less than a number
num = int(input("Enter the number:"))
if num > 10:
    print(f"{num} is greater than 10")
elif num == 10:
    print(f"{num} is equal to 10")
else:
    print(f"{num} is less than 10")  

#=======================================================================
# Check whether a number is odd or even
num = int(input("Enter the number:"))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")  

#=============================================================================
# Find the Grade of the mark
mark = float(input("Enter the mark:"))
if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 90:
    print("A Grade")
elif mark >= 80:
    print("B Grade")
elif mark >= 70:
    print("C Grade")
elif mark >= 60:
    print("D Grade")
elif mark >= 50:
    print("E Grade")
else:
    print("Failed")   

#======================================================================    
# Nested if
age = int(input("Enter the age:"))
if age >= 18:
    nationality = input("Enter the Nationality:")
    if nationality == "Indian":
        print("You can vote")
    else:
        print("you can't vote")        
else:
    print("You are minor")   

#======================================================================= 
# Discount
purchase_amount = int(input("Enter the purchase amount:"))
if purchase_amount > 1000:
    discount = purchase_amount * 0.10     
    print(f"You have got 10% of discount RS.{discount}")
else:
    discount = 0
    print("You don't have a discount")  

#========================================================================    
# Check if a person is adult,teenager or child
age=int(input("Enter the age:"))
if age < 13:
    print("Child")
elif age <=19:
    print("Teenager")
else:
    print("Adult")  

#===========================================================================    
# Check the password is correct
entered_password = input("Enter the password:")
password = "123456"
if password == entered_password :
    print("Successfully login")
else:
    print("Failed to login")  

#============================================================================    
# Check whether a number is odd or even,and also check whether the number is greater than or less than 50.
num = int(input("Enter the number:"))
if num % 2 == 0 and num == 50:
    print("Number is Even and equal to 50")
elif num % 2 == 0 and num >50:
    print("Number is even and greater than 50")
elif num % 2 == 0:
    print("Number is Even and less than 50")
elif num > 50:
    print("Number is odd and greater than 50")
else:
    print("Number is odd and less than 50") 

#========================================================================= 
# Electricity Bill
units = int(input("Enter the number of units:"))
if units  <= 100:
    amount = units * 5
elif units <= 200:
    amount = (100 * 5) + (units - 100) * 7   
else:
    amount = (100 *5) + (100*7) + (units-200) * 10
print("Payable Amount:",amount)    

#===========================================================================
# Triangle Classifier
side1 = float(input("Enter the first side:"))
side2 = float(input("Enter the second side:"))
side3 = float(input("Enter the third side:"))
if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Triangle")
else:
    print("No sides are equal")   

#==============================================================================    
# Character check
ch = input("Enter the character:")
if ch >= "A" and ch <= "Z":
    print("Uppercase")
elif ch >= "a" and ch <= "z":
    print("Lowercase")
elif ch >= '0' and ch <= '9':
    print("Number")
else:
    print("Symbol")   

#==============================================================================    
# ATM Simulation
pin = input("Enter the pin:")
if pin == "1234":
    print("Transaction allowed")
else:
    print("Invalid pin")  

#==============================================================================    
# Discount and amount 
purchase_amount = float(input("Enter Purchased amount:"))
if purchase_amount > 5000:
    discount = purchase_amount * 0.20
    payable_amount = purchase_amount - discount
    print(f"You have got 20% of discount Rs.{discount} and Payable amount is {payable_amount}")
elif purchase_amount > 2000:  
    discount = purchase_amount * 0.10
    payable_amount = purchase_amount - discount
    print(f"You have got 10% of discount Rs.{discount} and Payable amount is {payable_amount}")
else:
    print("You don't have a discount") 

#======================================================================= 
