# input we need from user 
# Total rent
# Total food order for snacking 
# Electrity units spend 
# Charge per unit
# Persond living in room/flat


# Total amount you have paied is 
#  it's output .....?

rent = int(input("Enter your hostal/flat rent :"))
food = int(input("Enter the amount of foods order :"))
electrity_spend = int(input("Enter the total electrity spend :"))
charge_per_unit = int(input("Enter the charge par unit :"))
persons = int(input("Enter the number of persons living in room/flat :"))


total_bill = electrity_spend * charge_per_unit

output = (rent+food+total_bill)//persons
print("Each persons will pat amount :",output)