list1 = [1,44,67,'hello',99, 100.51, 'apple']
list2 = ['apple', 3, 91, 100.51]

common_elements_list = []

for item in list1:
    if item in list2:
        common_elements_list.append(item)

print(common_elements_list)
