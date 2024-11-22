def count_down(n):
    if n == 1:
        print(n)
    else:
        print(n)
        count_down(n - 1)


def lengeth(my_list):
    if my_list == []:
        return 0
    else:
        return 1 + lengeth(my_list[1:])

# temp = [0, 1, 2, 3, 4]
# print(lengeth(temp), temp)
count_down(10)