my_list = [1,200,199,187,434,1,187]

frequency = []

for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)








