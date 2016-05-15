from Date import *

test_date = Date(22, 12, 2016)
counter = 1
for i in range(0, 100, 1):
    test_date.add_days(1)
    print(test_date)
    print(counter)
    counter += 1
