def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring

names = ['Andy', 'Laura', 'James']

result = list(map(splicer,names))
print(result)