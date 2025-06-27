# list1 = [278, 2, 99, 81, 984]
#
# largest_number = max(list1)
#
# print(largest_number)

# Another way

import random

list1 = [278, 2, 99, 81, 984]

random.shuffle(list1)

print(list1[-1])