def blackjack (a,b,c):
    if sum(a,b,c) <= 21:
        return sum(a,b,c)
    elif sum(a,b,c) > 21:



result = blackjack(9,9,9)
print(result)