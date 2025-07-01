"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
"""


def capitol(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short"

kuch_bhi = capitol('Macdowell No1 Soda')
print(kuch_bhi)



my_string = 'Hi my name is Ashish'
my_string = 'Misissippi'

