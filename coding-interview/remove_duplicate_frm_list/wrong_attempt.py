
list = [10, "hello", 10, True, "hello"]

count = {}

for item in list :
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

'''
I am putting logic , I know its lengthy

first I will count the number of occurence of each element inside the list 


list = [10, "hello", 10, True, "hello"]

then I thought I will pop out those element whose value are larger than 1, problem, if hello : 2 and I will pop out hello then this was not expected , I just had to remove the duplicates from the original list
'''