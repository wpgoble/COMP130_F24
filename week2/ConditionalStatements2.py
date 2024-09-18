# More practice work on conditional statements
# Sept. 13, 2024
##########################################
name = "William"
user_name = input("what is your name? ")
if name == user_name:
    print("we have the same name")
else:
    print("We do not have the same name")

score = int(input("what score did you get? "))
if score > 90:
    outcome = "A"
elif score > 80 and score < 90:
    outcome = "B"
elif score > 70 and score < 80:
    outcome = "C"
elif score > 60 and score < 70:
    outcome = "D"
else:
    outcome = "F"

n = int(input("give me a number "))
if n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
elif n % 15 == 0:
    print("FizzBuzz")
else:
    print(n)

if day == "Saturday" or day == "Sunday":
    if day == "Saturday":
        print("It's Saturday")
    