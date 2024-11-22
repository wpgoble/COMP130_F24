def my_length(the_list):
    # What is the base case?
    if the_list == []:
        return 0
    # What is the recursive case?
    else:
        # item = the_list[0]
        # temp_length = my_length(the_list[1:])
        # return 1 + temp_length
        element = the_list.pop()
        val = my_length(the_list)
        the_list.append(element)
        return 1 + val


my_list = [5, 6, 7, 8, 1, 2, 3]
the_length = my_length(my_list)
print(the_length, my_list)


def my_sum(my_list):
    if my_list == []:
        return 0
    else:
        item = my_list[0]
        temp_sum = my_sum(my_list[1:])
        return temp_sum + item
    
temp = [1, 2, 3, 4, 5, 6]
temp = [2, 3, 4, 5, 6]
temp = [3, 4, 5, 6]
temp = [4, 5, 6]
temp = [5, 6]
temp = [6]
temp = []

my_sum(temp)