import random

# word = "      snake    "

# # print(word[::-1])
# # print(word.center(10, "*"))
# # print(len(word))
# # word2 = word.rstrip().replace(" ", "*")
# # print(word2, len(word2))

# number = input("Please type in a number: ").strip()
# if number.isdecimal():
#     print("Our number is", int(number))
# else:
#     print(number.replace(" ", ""))

def passwordGenerator():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet + alphabet.upper()
    alphabet = alphabet + "1234567890!@#$%^&*()"
    password = ""
    for i in range(12):
        randomIndex = random.randint(0, len(alphabet))
        password += alphabet[randomIndex]
    return password