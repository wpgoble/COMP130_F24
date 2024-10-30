import turtle
import random

def print_6_multiples(n):
    for i in range(1, 7):
        print(n * i)


def print_multiples(n, num_multiples):
    for i in range(1, num_multiples + 1):
        print(i * n)

def print_sum_of_multiples(n,num_multiples):
    sum = 0
    for i in range(1, num_multiples + 1):
        sum = sum + (i * n)
        print(i * n)
    print("Sum is", sum)

def print_even_multiples(n, num_multiples):
    for i in range(1, num_multiples + 1):
        val = i*n
        if val % 2 == 0:
            print(val)

def funny_square1(t, x, y):
    edge = 100
    indent = edge / 2
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(4):
        t.forward(edge)
        t.left(90)
        t.forward(indent)
        t.right(90)
        t.forward(indent)
        t.right(90)
        t.forward(indent)
        t.left(90)
        t.forward(edge)
        t.left(90)

def funny_square2(t, x, y, edge_len):
    indent = edge_len / 2
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(4):
        t.forward(edge_len)
        t.left(90)
        t.forward(indent)
        t.right(90)
        t.forward(indent)
        t.right(90)
        t.forward(indent)
        t.left(90)
        t.forward(edge_len)
        t.left(90)

def funny_square3(t, x, y, edge_len):
    if edge_len % 10 == 0:
        t.pencolor("black")
    elif x % 2 == 0 and y % 2 == 0:
        t.pencolor("red")
    elif x % 2 == 1 and y % 2 == 1:
        t.pencolor("green")
    else:
        t.pencolor("blue")
    funny_square2(t, x, y, edge_len)

def many_funny_squares(t, num_squares):
    for i in range(num_squares):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        edge_len = random.randint(5, 50)
        funny_square3(t, x, y, edge_len)

# print_6_multiples(5)
# print_multiples(8, 3)
# print_sum_of_multiples(7, 3)
# print_even_multiples(9, 10)
bob = turtle.Turtle()
# funny_square2(bob, -250, 100, 60)
many_funny_squares(bob, 15)
turtle.exitonclick()