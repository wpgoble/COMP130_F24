def count_x(target):
    count = 0
    for letter in target:
        if letter == "x":
            count += 1
    return count

count = count_x("axbcxxd")
print(count)
