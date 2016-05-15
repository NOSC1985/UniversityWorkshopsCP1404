##If sales are under $1,000, the user gets a 10% bonus.
##If sales are $1,000 or over, the bonus is 15%.

salesTotal = float(input("Enter sales: $"))
while salesTotal >0:
    if salesTotal < 1000:
        bonus = salesTotal * 0.1
    else:
        bonus = salesTotal * 0.15
    print("Bonus for sales is: $", bonus, sep='')
    salesTotal = float(input("Enter sales: $"))

