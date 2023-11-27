"""Basic Calculator"""

def add(a, b):
    print(f"  {a}")
    print(f"+ {b}")
    print(f"--------")
    return f"  {a + b}"

def substraction(a, b):
    print(f"  {a}")
    print(f"- {b}")
    print(f"--------")
    return f"  {a - b}"

def multiplication(a, b):
    print(f"  {a}")
    print(f"x {b}")
    print(f"--------")
    return f"  {a * b}"

def division(a, b):
    print(f"  {a}")
    print(f"/ {b}")
    print(f"--------")
    return f"  {a / b}"

# num = input("Enter a number: ")
# num_2 = input("Enter a number: ")
operator_sign = ["+", "-", "*", "/"]

def main():
    # Loop to make sure it is a number that is entered
    print(operator_sign)
    while True:
        num = input("Enter a number: ")
        num_2 = input("Enter a number: ")
        operation = input("Enter the operator: ")
        if num.isdigit() and num_2.isdigit():
            num = int(num)
            num_2 = int(num_2)
            print("Good")
            break
        else:
            print("Invalid input.")

        # Check that teh operator is valid
        if operation in operator_sign:
            continue
        else:
            print("invalid operator")

    # Conditional Statement
    if operation == operator_sign[0]:
        print(add(a=num, b=num_2))
    elif operation == operator_sign[1]:
        print(substraction(a=num, b=num_2))
    elif operation == operator_sign[2]:
        print(multiplication(a=num, b=num_2))
    elif operation == operator_sign[3]:
        print(division(a=num, b=num_2))


main()