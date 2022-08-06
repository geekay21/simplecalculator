def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


print("**************")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("**************")


while True:
    # take input from the user
    choice1= input("Enter choice: ")

    # check if choice is one of the four options
    if choice1 in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice1 == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice1 == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice1 == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice1 == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        choice2= input("Do you want to continue(yes/no): ")
        if choice2== "no":
            break
    else:
        print("Invalid Input")