import random 

cpu_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Select 'rock', 'paper' or 'scissors':  ")

if user_choice == 'rock':
    if cpu_choice == 'rock':
        print("Tie")
    elif cpu_choice == 'paper':
        print("You Lose")
    else:
        print("You win")
elif user_choice == 'paper':
    if cpu_choice == 'rock':
        print("I win")
    elif cpu_choice == 'paper':
        print("Tie")
    else:
        print("You lose")
else:
    if cpu_choice == 'rock':
        print("You lose")
    elif cpu_choice == 'paper':
        print("You win")
    else:
        print("Tie")