print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Amazing! Let's start playing :)")
score = 0

answer = input("What deos pc stand for? ")
if answer.lower() == "personal computer":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("MS - Word is an example of___? ")
if answer.lower() == "application software":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Ctrl,Shift and Alt are called _____ keys? ")
if answer.lower() == "modifier":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("A Computer cannot boot if it does not have the____? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("The process of dividing the disk into tracks and sectors is called? ")
if answer.lower() == "formatting":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("Junk e-mail is also called ______? ")
if answer.lower() == "Spam":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " Questions Correct!")
print("You got " + str((score/ 6) * 100) + "%.")
