from Car import *

Prius = Taxi(100, "Prius 1", 1.20)
Prius.drive(40)
print(Prius)
Prius.start_fare()
Prius.drive(100)
print(Prius)
fare = Prius.get_fare()
print("Fare is ${}".format(fare))
