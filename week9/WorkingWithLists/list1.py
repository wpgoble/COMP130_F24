# family_guy = ["Brian", "Stewie", "Joe"]
# # # print(family_guy)
# # for character in family_guy:
# #     print(character)

# # for i in range(len(family_guy)):
# #     character = family_guy[i]
# #     if character == "Joe":
# #         family_guy.remove(character)

# # Can we make this a while loop?
# i = 0
# while i < len(family_guy):
#     character = family_guy[i]
#     if character == "Joe":
#         family_guy.remove(character)
#     i += 1

# print(family_guy)

# a = [1, 2, 3]
# b = a
# print(a, b)
# b[1] = 4
# print(a, b)
# a.append(6)
# print(a, b)

# student1 = ["alice", 3.8, 0]
# student2 = ["bob", 3.1, 3]
# students = [student1, student2, "William"]

# print(students[2][0])

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)