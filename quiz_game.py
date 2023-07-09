print("Welcome to my computer quizz!")

playing = input("Do you want to play ? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Fasten your seat belts")

score = 0

question1 = input("What is the full form of CPU? ")
if question1.lower() == "central processing unit":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')


question2 = input("What is the full form of GPU? ")
if question2.lower() == "graphical processing unit":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

question3 = input("What is the full form of IAS? ")
if question3.lower() == "indian administrative service":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

question4 = input("What is the full form of AWS? ")
if question4.lower() == "amazon web service":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

question5 = input("What is the full form of SAA? ")
if question5.lower() == "solution architect assosciate":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

print(f"Your score is : {score}/5")

