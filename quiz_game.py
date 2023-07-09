print("Welcome to my computer quizz!")

playing = input("Do you want to play ? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Fasten your seat belts")

question1 = input("What is the full form of CPU? ")
if question1.lower() == "central processing unit":
    print('Correct!')

else:
    print('Try Next Time!')


question2 = input("What is the full form of GPU? ")
if question2 == "Graphical Processing Unit":
    print('Correct!')

else:
    print('Try Next Time!')

question3 = input("What is the full form of IAS? ")
if question3 == "Indian Administrative Service":
    print('Correct!')

else:
    print('Try Next Time!')

question4 = input("What is the full form of AWS? ")
if question4 == "Amazon Web Service":
    print('Correct!')

else:
    print('Try Next Time!')

question5 = input("What is the full form of SAA? ")
if question5 == "Solution Architect Assosciate":
    print('Correct!')

else:
    print('Try Next Time!')