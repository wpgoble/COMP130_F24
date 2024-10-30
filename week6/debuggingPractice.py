def fizzBuzz1(number):
    """
        This function implements a fruitful version of the 
        game fizzbuzz
    Args:
        number (int): The number we are testing to see 
        what our response should be
    """
    result = ""
    if number % 15 == 0:
        result = "fizzbuzz"
    elif number % 5 == 0:
        result = "buzz"
    elif number % 3 == 0:
        result = "fizz"
    else:
        result = number
    return result

def fizzBuzz2(number):
    """
        This function implements a fruitful version of the 
        game fizzbuzz
    Args:
        number (int): The number we are testing to see 
        what our response should be
    """
    
    if number % 15 == 0:
        return "fizzbuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return number

def my_summation():
    print("This program will calculate the sum of any two numbers")
    number1 = int(input("Please provide the first number: "))
    number2 = int(input("Please provide the second number: "))
    result = f"The summation of {number1} and {number2} is {number1 + number2}"
    print(result)

def doubleX(X):
    return X*2

def my_double():
    val = int(input("Please give me a number: "))
    # val2 = doubleX(val)
    result = f"If we double {val} we get {doubleX(val)}"
    print(result)

if __name__ == "__main__":
    # my_summation()

    my_double()

    # for i in range(1, 101):
    #     answer = fizzBuzz1(i)
    #     print(answer)
    
    for i in range(1, 101):
        answer = fizzBuzz2(i)
        print(answer)