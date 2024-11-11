"""
first I want to specify where my text file is 
located so I can properly access it.
"""
filename = "./week11/sample.txt"

"""
Next I am going to open it in write mode so 
I can add information to the file
"""
my_file = open(filename, "w")

"""
Here is the list of students that I want added 
to my sample document.
"""
studentList = [
    ["Alice", "Math", 3.95],
    ["Bob", "QEcon", 3.59],
    ["Carol", "English", 3.68],
]

"""
The following for loop will iterate across the 
studentList list and convert each sublist into 
a string. This will result in strings formatted 
like '["Alice", "Math", 3.95]'. In order to 
remove the square brackets, I then call the replace 
method to swap out each square bracket with an 
empty string.
"""
for student in studentList:
    my_info = str(student).replace("[", "").replace("]", "")
    my_file.write(my_info + "\n")

# Make sure we close the file when we are done working with it
my_file.close()
