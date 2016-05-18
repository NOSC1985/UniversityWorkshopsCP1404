from Car import *

luxury_sedan = SilverServiceTaxi(100, "Lexus", 2)

luxury_sedan.drive(10)
print(luxury_sedan)
print("total Fare so far is ${:.2f}".format(luxury_sedan.get_fare()))
