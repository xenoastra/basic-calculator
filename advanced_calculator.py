
def repeat():
    #this statement defines the function called repeat which is going to be called if user asaks to use calculator again
    num1 = float(input("Enter first number: "))
    #this can also take decimal values
    #num1 is the name of the variable that will be the first user input
    op = (input("Enter operator: (+, -, /, *, sqrt, sqr, pow, fac, sin, cos, tan, log, cube, cubrt) "))
    #Here the user can enter varous operators. + for addition, _ for subtraction, / for division, * for multiplication, sqrt for square root
    #sqr for square, pow for power, fac for factorial, sin/cos/tan for trigonometry, log for logarithms, cube to cube the number, cubrt to cube root
    num2 = float(input("Enter second number: "))
    #num2 is the second number that the  user will input and can also be a decimal

    def calculator():
        #defines the function calculator which will be called later on
        str1 = "Invalid operator"
        #if they enter an invalid operator then we will return str1
        import math
        #this imports extra math statements that will be used later on
        if op == "+":
        #if the operator is + this will add the 2 numbers
            return num1 + num2
        #returns the sum of the two numbers
        elif op == "-":
            # if the operator is - this will subtract the 2 numbers
            return num1 - num2
        #returns the difference of the two numbers
        elif op == "/":
            return num1 / num2
        elif op == "*":
            return num1 * num2
        elif op == "sqrt":
            return math.sqrt(num1), math.sqrt(num2)
        elif op == "pow":
            return math.pow(num1, num2)
        elif op == "fac":
            return math.factorial(num1), math.factorial(num2)
        #returns the factorial of the two numbers
        elif op == "sin":
            return math.sin(num1), math.sin(num2)
        #returns sinx, siny where x is num1 and y is num2
        elif op == "cos":
            return math.cos(num1), math.cos(num2)
        elif op == "tan":
            return math.tan(num1), math.tan(num2)
        elif op == "log":
            return math.log(num1,num2)
        elif op == "cube":
            return num1 ** 3, num2 ** 3
        #cubes the two numbers
        elif op == "cubrt":
            return num1 *(1/3) , num2 *(1/3)
        elif op == "sqr":
            return num1 * num1, num2 * num2
        #squares the two numbers
        else:
            return str1
        #if not it returns the invalid statement

    str2 = f"The answer is {calculator()}"
    return str2
#returns the function calculator with the answer

print("           ")
print("Welcome to Xenoastra's Calculator")
print("you can calculate addition, subtraction, square root, powers, factorials, trigonometry and logarithms ")
print("                                               ")
print(repeat())

calculator = int(input("would you like do calculate anything else? (enter 0 for no, 1 for yes) "))
#this can only take integers
#If user types in 1, it will call function repeat and start over
if calculator == 1:
    while calculator == 1:
        print(repeat())
        calculator = int(input("would you like do calculate anything else? (enter 0 for no, 1 for yes) "))
        if calculator == 0:
            print("Have a great day, I hope you enjoyed the calculator, calc-you-later!")
#this while loop will run at the end of the program asking if the user wants to input anything else
elif calculator == 0:
    print("Have a great day, I hope you enjoyed the calculator!, calc-you-later")
    # If user types in 0, it will print out have a good day
else:
    print("Invalid response")
    #if user types anything else, it will come up as invalid response