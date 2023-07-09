print("Welcome to my computer quizz!")

playing = input("Do you want to play ? ")
print(playing)

if playing != "yes":
    quit()

print("Okay! Fasten your seat belts")

question1 = input("What is the full form of CPU? ")
if question1 == "Central Processing Unit":
    print('Correct!')

else:
    print('Try Next Time!')


