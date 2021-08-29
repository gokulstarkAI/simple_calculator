from art import logo
def add(n1,n2):
    """This function takes two number as input and returns the addition as output"""
    return n1+n2
def sub(n1,n2):
    """This function takes two number as input and returns the subtraction as output"""
    return n1-n2
def multiply(n1,n2):
    """This function takes two number as input and returns the multiplication as the output"""
    return n1*n2
def divide(n1,n2):
    """This function takes two number as input and returns the divide as the output"""
    return n1/n2
operations={
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1=float(input("What's the first number:"))
    for operation in operations:
        print(operation)
    operation_symbol=input("Pick an operation to perform on the inputs:")
    num2=float(input("What's the second number:"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(n1=num1,n2=num2)
    print(f"{num1} {operation_symbol} {num2} = {answer} ")
    i = False
    while not i:
        user = input(f"Type 'y' to continue with {answer}, or type 'n' to continue with new calculation.:").lower()
        if user=="n":
            calculator()
            i = True
        elif user=="y":
            for operation in operations:
                print(operation)
            operation_symbol = input("Pick an operator:")
            num3 = float(input("What's the next number?:"))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(n1=answer, n2=num3)
            print(f"{answer} {operation_symbol} {num3} = {second_answer} ")
calculator()







