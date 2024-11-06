def addStudent(my_list):
    name = input("What is the student's name? ")
    major = input("What is the student's major? ")
    gpa = float(input("What is the student's GPA? "))
    student = [name, major, gpa]
    my_list.append(student)


def filterMajor(my_list, major):
    pass


def calcGPAaverage(my_list):
    pass

def findStudent(my_list):
    pass


def printStudent(student):
    print(f"name:\t\t{student[0]}")
    print(f"major:\t\t{student[1]}")
    print(f"GPA:\t\t{student[2]}")


if __name__ == "__main__":
    # Here is a list in which each element 
    # is a list with information about students
    # it contains their name, major, and GPA
    studentList = [
        ["Alice", "Math", 3.95],
        ["Bob", "QEcon", 3.59],
        ["Carol", "English", 3.68]
    ]
    running = True
    while running:
        print("What would you like to do? ")
        print("1 for add student.")
        print("2 for filter by major.")
        print("3 for find average GPA.")
        print("4 to see a specific student.")
        print("0 to quit.")
        input = int(input(""))
        if input == 1:
            addStudent(studentList)
        elif input == 2:
            major = input("What major would you like to filter by? ")
            filterMajor(studentList, major)
        elif input == 3:
            average = calcGPAaverage(studentList)
            print(f"The average GPA is {average}")
        elif input == 4:
            student = findStudent(studentList)
            printStudent(student)
        elif input == 0:
            running = False