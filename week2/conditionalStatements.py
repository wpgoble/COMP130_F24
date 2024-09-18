# Practice work on conditional statements
# Sept. 11, 2024
##########################################
# Import Statements go here
import random
##########################################
# Programming Practice
# write a script that will generate a 
# random number between a user defined 
# min and max value. Print the result when 
# complete.
min = input("Give me a minimum number")
max = int(input("Give me a maximum number"))
min = int(min)
guess = int(input("Please guess a number "))
answer = random.randint(min, max)

if guess == answer:
    print("Correct")
else:
    print("The answer was", answer)

print("Thanks for playing")
##########################################