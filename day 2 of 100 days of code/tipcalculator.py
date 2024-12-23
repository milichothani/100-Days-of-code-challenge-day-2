print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
# tip above is 10% 12% or 15%
people = int(input("How many people to split the bill? "))
#we need to first find the tip percentage and then multiply it with total bill
tip_percentage = (tip/100)*bill
result = (bill+tip)/people
print(f"\nEach person should pay : {round(result , 2)}")
#we need to round off the bill upto 2 decimal places


