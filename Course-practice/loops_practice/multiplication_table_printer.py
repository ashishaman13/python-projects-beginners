# Print the multiplication table for a given number upto 10 , but skip the fifth iteration

n = 12

for x in range(1,11):
    if x == 5:
        pass
    else:
        print(f"12 * {x} =" + str(12 * x) + "\n")

