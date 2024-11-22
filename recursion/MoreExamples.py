import turtle

def recur_reverse(my_str):
    if len(my_str) == 0:
        return ""
    else:
        return recur_reverse(my_str[1:]) + my_str[0]

def spiral(turt, sideLen, angle, scale, minLen):
    if sideLen <= minLen:
        return
    else:
        turt.forward(sideLen)
        turt.left(angle)
        sideLen = sideLen * scale
        spiral(turt, sideLen, angle, scale, minLen)

def spiral2(turt, sideLen, angle, scale, minLen):
    if sideLen <= minLen:
        return
    else:
        turt.forward(minLen)
        turt.right(angle)
        minLen = minLen / scale
        spiral2(turt, sideLen, angle, scale, minLen)


if __name__ == "__main__":
    bob = turtle.Turtle()
    print(recur_reverse("Time"))
    spiral2(bob, 200, 90, 0.8, 15)
    turtle.exitonclick()