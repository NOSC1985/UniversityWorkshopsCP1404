from Car import *


the_bomb = UnreliableCar(100000, "The Bomb", 56.77846)

for i in range (0, 100, 1):
    the_bomb.drive(100)
    print(the_bomb)
