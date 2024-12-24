print("Welcome to the tip calculator! ")
bill= float (input("What was the total bill: "))
tip =float(input("How much tip would you like to give? 10,12 or 15 ? "))
if tip in [10,12,15]:
    billAfterTip=  bill + (bill * tip / 100)
else:
    print("input the options given")    
    exit()
split =float(input("How many people to split the bill? "))

netBill=billAfterTip/split
print(f"Each person should pay {netBill}")
# another solution using functions
def tip_calculator():
    print("Welcome to the tip calculator!")
    
    # Get the total bill amount
    bill = input("What was the total bill? ")
    if not bill.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a valid numeric value for the bill.")
        return
    bill = float(bill)
    
    # Get the tip percentage
    tip = input("How much tip would you like to give? 10, 12, or 15? ")
    if not tip.isdigit() or int(tip) not in [10, 12, 15]:
        print("Please choose a valid tip percentage: 10, 12, or 15.")
        return
    tip = int(tip)
    
    # Calculate the total bill including tip
    bill_after_tip = bill + (bill * tip / 100)
    
    # Get the number of people to split the bill
    split = input("How many people to split the bill? ")
    if not split.isdigit() or int(split) <= 0:
        print("Invalid input. The number of people must be a whole number greater than 0.")
        return
    split = int(split)
    
    # Calculate the amount each person should pay
    net_bill = bill_after_tip / split
    print(f"Each person should pay: ${net_bill:.2f}")

# Run the tip calculator
tip_calculator()
