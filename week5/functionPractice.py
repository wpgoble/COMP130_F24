#####################################
# Import Statements are at the top.
# Global variables should also be at 
# the top, but please limit how many 
# global variables you create.
#####################################

#####################################
# Next we have our function 
# definitions
#####################################
def reverse(str):
    answer = ""
    for letter in str:
        answer = letter + answer
        # answer = answer + letter
    return answer
    # print(answer)
#####################################
# Last we have our main function 
# as the top level code
#####################################
if __name__ == "__main__":
    val = reverse("Racecar")
    print(val)