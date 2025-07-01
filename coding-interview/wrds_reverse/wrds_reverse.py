"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""

"""
Concept learned


1. ::-1 works for reversing a list as well as string
2. split() - It will convert a scentence (string) to a list, with each word of a scentence acting as the element for the list
3. join function - 

"""


def aalo_function(ipt):
    a = ' '.join(ipt.split()[::-1])
    print(a)

aalo_function("Hippopotamus")












