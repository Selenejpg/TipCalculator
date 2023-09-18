print("Welcome to the tip calculator")
bill_total_str = input("What was the total bill? $")
bill_total = float(bill_total_str) 
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people_bill = input("How many people will split the bill? ")
people_bill_int = int(people_bill)

total_per_person = round(bill_total / people_bill_int, 2)

if tip_percentage == "10":
    total_per_person *= 1.10
elif tip_percentage == "12":
    total_per_person *= 1.12
elif tip_percentage == "15":
    total_per_person *= 1.15
else:
    print("You entered an invalid tip percentage!")

print(f"Each person should pay ${round(total_per_person, 2)}")

