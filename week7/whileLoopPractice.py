import answers

# for i in range(10):
#     print(i)

# print("#" * 15)
# i = 0
# while i < 10:
#     print(i) 
#     i = i + 1

# word = "Dickinson"
# for letter in word:
#     print(letter)

# # word[0]
# index = 0
# while index < len(word):
#     print(word[index])
#     index += 1

isGuessing = True 
count = 0
while isGuessing:
    guess = input("What is my favorite movie? ")
    count += 1
    if guess == answers.movie:
        isGuessing = False
        print(f"You guessed right in {count} guesses")
    else:
        print("You guessed wrong")
    