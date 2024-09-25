# Exercise 1
# for number in range(-10, 11):
#     print(number)

# number = -10
# for i in range(21):
#     print(number)
#     number += 1

# Exercise 2
# max_num = input("Please pick a number ")
# max_num = int(max_num)
# sum = 0
# for i in range(1, max_num + 1):
#     # sum += i
#     sum = sum + i
# print(sum)

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

answer = ""
for i in range(1, 6):
    answer = answer + str(i) + " "
    print(answer)