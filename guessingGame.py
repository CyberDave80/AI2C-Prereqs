import random

random_number = random.randint(1,100)
guess = int(input("Guess a number from 1 to 100:   "))
count = 1

while guess != random_number:
    if guess > random_number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess a number from 1 to 100:   "))
    count += 1
print("Congratulations, you got it!")
print("You got it in ", count, "guesses")