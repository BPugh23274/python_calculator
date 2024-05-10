def add(x,y):
    result = x + y
    print("The sum of ",x," and ",y," is ",result)

def subtract(x,y):
    result = x - y
    print("The difference of ",x," and ",y," is ",result)

def multiply(x,y):
    result = x * y
    print("The product of ",x," and ",y," is ",result)


def division(x,y):
    result = x / y
    print("The quotient of ",x," and ",y," is ",result)



def calculator():
    op = input("Select operation: add, subtract, multiply, or divide: ")
    
    op_tuple = userinput()
    x = int(op_tuple[0])
    y = int(op_tuple[1])


    if (op == "add") or (op == "Add") or (op == "ADD"):
        add(x,y)

    elif (op == "subtract") or (op == "Subtract") or (op == "SUBTRACT"):
        subtract(x,y)

    elif (op == "multiply") or (op == "Multiply") or (op == "MULTIPLY"):
        multiply(x,y)

    elif (op == "divide") or (op == "Divide") or (op == "DIVIDE"):
        division(x,y)
    
    else:
        print("Could not register operation, please try again. Wahhh")
        calculator()

    
        


def userinput():
    x = input("Enter first number: ")
    y = input('Enter second number: ')

    return x,y


calculator()
