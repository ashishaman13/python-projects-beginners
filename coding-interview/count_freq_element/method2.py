my_list = ['apple', 'orange', 'banana', 'apple', 'banana', 'apple']

frequency = {}

for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)



