print("Welcome to my computer quizz!")

playing = input("Do you want to play ? ").lower()
print(playing)

if playing != "yes":
    quit()

print("Okay! Fasten your seat belts")

score = 0

question1 = input("What is the full form of CPU? ").lower()
if question1 == "central processing unit":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')


question2 = input("What is the full form of GPU? ").lower()
if question2 == "graphical processing unit":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

question3 = input("What is the full form of IAS? ").lower()
if question3 == "indian administrative service":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

question4 = input("What is the full form of AWS? ").lower()
if question4 == "amazon web service":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

question5 = input("What is the full form of SAA? ").lower()
if question5 == "solution architect assosciate":
    print('Correct!')
    score += 1

else:
    print('Try Next Time!')

print(f"Your score is : {score}/5")

