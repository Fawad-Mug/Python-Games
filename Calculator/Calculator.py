



def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations= {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculation():
    num1= float(input("What's the first Number?: "))
    for symbol in operations:
        print(symbol)

    should_continue=True
    while should_continue:
        symbol_operation=input('Pick an operation from the line above: ')
        num2= float(input("What's the next Number?: "))
        calculation_function= operations[symbol_operation]
        answer=calculation_function(num1,num2)

        print(f'{num1} {symbol_operation} {num2} = {answer}')
        if input(f"Type 'y' to continue with calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1= answer
        else:
            should_continue= False
            calculation()

calculation()