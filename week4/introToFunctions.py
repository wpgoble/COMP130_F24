def print_twice(word):
    print(word)
    print(word)

def cat_twice(line1, line2):
    sentence = line1 + " " + line2
    print_twice(sentence)

if __name__ == "__main__":
    str1 = "Hello"
    str2 = "Class"
    cat_twice(str1, str2)

