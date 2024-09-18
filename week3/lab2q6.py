# Implements question 6 from lab 2
data_type = input("what data type would you like to use? ")
first_value = input("What is your first value? ")
operator = input("What is your operator")
second_value = input("What is your second value? ")

if data_type == "int":
    first_value = int(first_value)
    second_value = int(second_value)
    if operator == "+":
        print(f"{first_value} + {second_value} = {first_value + second_value}")
    elif operator == "-":
        print(f"{first_value} - {second_value} = {first_value - second_value}")
    elif operator == "*":
        print(f"{first_value} * {second_value} = {first_value * second_value}")
    elif operator == "/":
        print(f"{first_value} / {second_value} = {first_value / second_value}")
    elif operator == "**":
        print(f"{first_value} ** {second_value} = {first_value ** second_value}")
    else:
        print("Invalid operator")
elif data_type == "str":
    if operator == "+":
        print(f"{first_value} + {second_value} = {first_value + second_value}")
    elif operator == "*":
        second_value = int(second_value)
        print(f"{first_value} * {second_value} = {first_value * second_value}")
    else:
        print("Invalid operator")
elif data_type == "float":
    first_value = float(first_value)
    second_value = float(second_value)
    if operator == "+":
        print(f"{first_value} + {second_value} = {first_value + second_value}")
    elif operator == "-":
        print(f"{first_value} - {second_value} = {first_value - second_value}")
    elif operator == "*":
        print(f"{first_value} * {second_value} = {first_value * second_value}")
    elif operator == "/":
        print(f"{first_value} / {second_value} = {first_value / second_value}")
    elif operator == "**":
        print(f"{first_value} ** {second_value} = {first_value ** second_value}")
    else:
        print("Invalid operator")