print("Welcome to my basic quiz!")

playing = input("Do you want to attempt this quiz? Yes/No: ")

if playing.lower() != "yes":
    print("I understand. Thank you for trying though!")
    quit()
    
print("Lets start!")
score = 0

#Question 1
answer = input("Question 1: What does CPU stand for? \nAnswer: ")
if answer.lower() == "central processing unit":
    print("That's correct! Great Job!\n")
    score += 1
else:
    print("Oops, that's incorrect. Try again!\n")
    
#Question 2
answer = input("Question 2: What are the physically interactible parts of a computer? \nAnswer: ")
if answer.lower() == "hardware":
    print("That's correct! Great Job!\n")
    score += 1
else:
    print("Oops, that's incorrect. Try again!\n")

#Question 3
answer = input("Question 3: What are the programs and applications required to run a computer? \nAnswer: ")
if answer.lower() == "software":
    print("That's correct! Great Job!\n")
    score += 1
else:
    print("Oops, that's incorrect. Try again!\n")
    
#Question 4
answer = input("Question 4: What does GPU stand for? \nAnswer: ")
if answer.lower() == "graphics processing unit":
    print("That's correct! Great Job!\n")
    score += 1
else:
    print("Oops, that's incorrect. Try again!\n")
    
#Question 5
answer = input("Question 5: How many characters is recommended for standard passwords? \nAnswer: ")
if answer.lower() == "8" or answer == "eight":
    print("That's correct! Great Job!\n")
    score += 1
else:
    print("Oops, that's incorrect. Try again!\n")
    
    
print(f"Congratulations! You got {score} out of the 5 questions correct.")
print(f"You got a grade of {(score / 5) * 100}%.")

    
def quit():
    return True


    

