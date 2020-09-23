import math
import random
import operator

guess = ""
guess_count = 0
guess_limit = 10
guess_limit_reached = False
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]

# Random math-op based on two user-inputs
zahl1 = int(input("Enter number one: "))
zahl2 = int(input("Enter number two: "))
op, fn = random.choice(operators)
secret_number = fn(zahl1, zahl2)

# Bonus-game if first nr is in range(9,12)
if zahl1 in range(9, 12):
    print("You hit the jackpot") 
    guess = secret_number 
    
# Calc-game with 10 tries
else:
    while guess != secret_number and not(guess_limit_reached):
        
        if guess_count < guess_limit:
            guess = int(input("Guess the secret number: "))
            if guess == secret_number:
                print("you win")
                break
            elif guess > secret_number:
                print("too big")
            else:
                print("Too small")
            guess_count += 1
        else:
          guess_limit_reached = True
if guess_limit_reached:
     print("secret number is: {} {} {} =".format(zahl1, op, zahl2), secret_number)
     print("You lose!")
else:
     print("secret number is: {} {} {} =".format(zahl1, op, zahl2), secret_number)
     print("You win!")