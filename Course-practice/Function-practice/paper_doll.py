"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""
from tabnanny import check
from xxsubtype import bench


def paper_doll(name):
    new_string = ''
    for i in name:
        new_string += i * 3
    return new_string

check = paper_doll('shayam')
print(check)



