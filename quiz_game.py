print('Welcome to the ashish quiz')

consent = input("Are you ready to play ? ").lower()
if consent != 'yes':
    quit()

print('Ok! Fasten your seat belts')

score = 0

answer = input("What is your name ? ").lower()
if answer == 'ashish':
    print('Correct!')
    score += 1

else:
    print('incorrect')

answer = input("What is ashish's location ? ").lower()
if answer == 'patna':
    print('Correct!')
    score += 1
else:
    print('incorrect')

print(f"Your score is {score}/2")
print("You got " + str((score)/2 * 100) + "%")