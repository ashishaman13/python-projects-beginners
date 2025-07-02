"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
"""

def number_checker(a):
    return 100-a < 10 or 200-a < 10

number_checker(182)