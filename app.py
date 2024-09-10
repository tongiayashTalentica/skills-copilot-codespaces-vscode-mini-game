# write Welcome to Rock Paper Scissors Game to console
import random
choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock Paper Scissors Game")

# declare a variable called user_choice and assign it the value of input from the user
user_choice = input("Enter Rock, Paper, or Scissors: ")

# print the value of user_choice to the console
print("User choice: ", user_choice)

# declare a variable called computer_choice and assign it a random value from the list of choices
computer_choice = random.choice(choices)

# print the value of computer_choice to the console
print("Computer choice: ", computer_choice)

# if the user_choice is equal to the computer_choice, print "It's a tie!"
if user_choice == computer_choice:
    print("It's a tie!")

# if the user_choice is "Rock" and the computer_choice is "Scissors", print "You win!"
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")

# if the user_choice is "Rock" and the computer_choice is "Paper", print "You lose!"
elif user_choice == "Rock" and computer_choice == "Paper":
    print("You lose!")

# if the user_choice is "Paper" and the computer_choice is "Rock", print "You win!"
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")

# if the user_choice is "Paper" and the computer_choice is "Scissors", print "You lose!"
elif user_choice == "Paper" and computer_choice == "Scissors":
    print("You lose!")

# if the user_choice is "Scissors" and the computer_choice is "Paper", print "You win!"
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")

# if the user_choice is "Scissors" and the computer_choice is "Rock", print "You lose!"
elif user_choice == "Scissors" and computer_choice == "Rock":
    print("You lose!")

# if the user_choice is not equal to "Rock", "Paper", or "Scissors", print "Invalid choice!"
else:
    print("Invalid choice!")
    
# Run the code and test it with different inputs to see if it works as expected
# Run the code and test it with different inputs to see if it works as expected