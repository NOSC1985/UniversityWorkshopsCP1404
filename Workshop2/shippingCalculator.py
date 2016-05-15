##While item entry != finished

##prompt User and store float for the currently working Item (Amount of item)
##prompt User and store float for the currently working Item (price of item)
##Calculate the cost of shipping that Item
##Increment and display to calculated cost so far
__author__ = 'Nicholas Stanton-Cook'
totalPrice = 0
totalItems = 0
print("Welcome to Shipping Calculator\n")
topMenu = ('(E)nter New Item\n(R)estart\n(Q)uit\n')
print(topMenu)
topMenuSelector = input('ENTER: ')
while topMenuSelector != 'Q':

    if topMenuSelector == 'E':
        numberOfItem = float(input("how many of this item will be shipped?: "))
        while numberOfItem <= 0:
            print("Number of Items must be more than 0")
            numberOfItem = float(input("how many of this item will be shipped?: "))
        costOfItem = float(input("How much does this Item cost to ship per Unit?: "))
        while costOfItem < 0:
            print("cost of Items must be either Zero or a positive amount")
            costOfItem = float(input("How much does this Item cost to ship per Unit?: "))
        addOnPrice = numberOfItem * costOfItem
        addOnItems = numberOfItem
    elif topMenuSelector == 'R':
        print("you have reset your totals")
        topMenuSelector = 'Q'
        addOnPrice = 0
        addOnItems = 0
        totalPrice = 0
        totalItems = 0

    else:
        print("Please enter a valid Menu selection")
        addOnPrice = 0
        addOnItems = 0
    totalPrice += addOnPrice
    totalItems += addOnItems

    print("\nTotal cost so far for {} Items is\n${}\n".format(totalItems, totalPrice))
    print(topMenu)
    topMenuSelector = input('ENTER: ')
print("\nThank you for using Shipping Calculator,\nby ", __author__)