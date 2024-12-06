# import matplotlib.pyplot as plt

# grades = {'A': 9, 'B':8, 'C':7, 'D':2, 'F':0}
# letters = grades.keys()
# amount = grades.values()

# # plt.plot(letters, amount)
# # plt.show()
# plt.bar(range(len(grades)), list(amount))
# plt.xticks(range(len(grades)), list(letters))
# plt.show()


grades = {}
answer = input("Enter a grade or type 'exit' to quit the program: ")
while answer != "exit":
    letters = "ABCDF"
    if answer.upper() not in letters:
        print("Invalid grade, try again")
    else:
        if answer not in grades:
            grades[answer] = 1
        else:
            grades[answer] = grades[answer] + 1
    answer = input("Enter a grade or type 'exit' to quit the program: ")

