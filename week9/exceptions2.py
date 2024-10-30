def division(a, b):
    try:
        result = a // b
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("Invalid input, please use a valid number")
    except Exception as e:
        print("Generic exception:", e)
    else:
        return result


answer1 = division(6, 2)
print("Your answer is:", answer1)
answer2 = division(3, 0)
if not (answer2 == None):
    print("Your answer is:", answer2)
