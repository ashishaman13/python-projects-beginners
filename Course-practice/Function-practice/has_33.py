"""
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

# If you want to iterate on list but not on the basis of items, but on the index position number

def has_33(list):
    for i in range(0, len(list)-1):
        if list[i:i+2] == [3,3]:
            return True

    return False

result = has_33([1,2,3,3,5,6,33])
print(result)


