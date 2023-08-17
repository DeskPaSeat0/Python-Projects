import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter your pick. Rock, Paper, or Scissors? Enter Q if you want to quit! ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    