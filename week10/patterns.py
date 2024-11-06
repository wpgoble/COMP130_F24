def calc_sum(my_list):
    answer = 0
    for i in range(len(my_list)):
        answer += my_list[i]
    return answer


def calc_avg(my_list):
    answer = 0
    for i in range(len(my_list)):
        answer += my_list[i]
    average = answer / len(my_list)
    return average

def major_count(my_list, major):
    count = 0
    for i in range(len(my_list)):
        current_major = my_list[i]
        if current_major == major:
            count += 1
    return count

def squares(my_list):
    answer = []
    for number in my_list:
        value = number ** 2
        answer.append(value)
    return answer

def match_majors(majors, names):
    match = []
    for i in range(len(majors)):
        element = names[i] + "->" + majors[i]
        match.append(element)
    return match

majors = ["Undeclaired", "BioChem", "Russian", "Undeclaired", 
          "Undeclaired", "BioChem", "Undeclaired", "QEcon"]
names = ["Coby", "Scarlett", "Sofia", "Lily", "Abigail", "Matthew", "Chase", "Preston"]
# print(major_count(majors, "BioChem"))

# temp = [1, 2, 3, 4, 5]
# print(temp)
# temp2 = squares(temp)
# print(temp, temp2)

# temp3 = match_majors(majors, names)
# print(temp3)

def find_computer(my_list):
    computer = []
    for course in my_list:
        prefix = course[0:4]
        if prefix == "COMP":
            computer.append(course)
    return computer



courses = ["COMP130", "RUSS231", "COMP132", "BIO132", "COMP190", "ART223", "CHEM241", "ITAL232"]
find_computer(courses)