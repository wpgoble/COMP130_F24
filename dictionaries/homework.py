courses = {}
while True:
    user_input = input("Enter course code or type 'exit' to end").strip().upper()
    if user_input == "EXIT":
        break
    index = 4
    for i in range(len(user_input)):
        if user_input[i].isdeciml():
            index = i
            break
    department = user_input[0:index]
    if department in courses and type(courses[department]) is not list:
        value = courses[department]
        courses[department] = [value, user_input]
    elif department in courses:
        courses[department].append(user_input)
    else:
        courses[department] = user_input

print(courses)
