"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""

"""Take input from two user and return the smallest number"""

# input1 = int(input("Enter first number:"))
# input2 = int(input("Enter the second number:"))
# if input1 < input2:
#         print(f"Lesser number is:{input1}")
# else:
#          print(f"Lesser number is:{input2}")




def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(min(num1,num2))
    elif num1 % 2 != 0 or num2 % 2 != 0:
        print(max(num1,num2))
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print(max(num1,num2))

lesser_of_two_evens(98,102)


