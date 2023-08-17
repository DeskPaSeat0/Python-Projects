import random

top_of_range = input("Input a number: ")

if top_of_range.is_digit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please enter a number bigger than zero (0) next time")
        quit()
else:
    print("Please input a number next time.")
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.is_digit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number. Try again.")
    else:
        print("You were below the number. Try again!")
        
print(f"You got the correct answer in {guesses} guesses.")