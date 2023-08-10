print("Welcome to my basic quiz!")

playing = input("Do you want to attempt this quiz? Yes/No: ")

if playing.lower() != "yes":
    print("I understand. Thank you for trying though!")
    quit()
    
print("Lets start!")
score = 0

#Question 1
answer = input("Question 1: What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("That's correct! Great Job!")
    score += 1
else:
    print("Oops, that's incorrect. Try again!")
    
#Question 2
answer = input("Question 2: What are the physically interactible parts of a computer? ")
if answer.lower() == "hardware":
    print("That's correct! Great Job!")
    score += 1
else:
    print("Oops, that's incorrect. Try again!")

#Question 3
answer = input("Question 3: What are the programs and applications required to run a computer? ")
if answer.lower() == "software":
    print("That's correct! Great Job!")
    score += 1
else:
    print("Oops, that's incorrect. Try again!")
    
#Question 4
answer = input("Question 4: What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("That's correct! Great Job!")
    score += 1
else:
    print("Oops, that's incorrect. Try again!")
    
#Question 5
answer = input("Question 5: How many characters is recommended for standard passwords? ")
if answer.lower() == "8" or answer == "eight":
    print("That's correct! Great Job!")
    score += 1
else:
    print("Oops, that's incorrect. Try again!")
    
    
print(f"Congratulations! You got a score of {score} points!")

    
def quit():
    return True


    

