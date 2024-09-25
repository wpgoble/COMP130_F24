import turtle

# joe = turtle.Turtle()

# for side in range(4):
#     print(f"side = {side}")
#     joe.forward(100)
#     joe.left(90)

# joe.penup()
# joe.forward(110)
# joe.pendown()

# for side in range(4):
#     joe.forward(100)
#     joe.left(90)

# turtle.done()

# only print out odd numbers
# odd numbers from 1 to 20
# for number in range(1, 20, 2):
    # print(number)

# for number in range(1, 20):
    # if not (number % 2 == 0):
    # if number % 2 != 0:
    # if number % 2 == 1:
    #     print(number)

# Implement a count down
# for number in range(20, -1, -1):
#     if number == 0:
#         print("Blast off")
#     else:
#         print(number)

for number in range(0, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    