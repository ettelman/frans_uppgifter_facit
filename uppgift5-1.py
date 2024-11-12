"""
Skriv en funktion “calculate” som kan ta ett obegränsat antal numeriska argument och en 
valfri parameter operation som kan vara 'add', 'subtract', 'multiply' eller 'divide'.

Funktionen ska utföra den specificerade operationen på alla numeriska argument.
"""

def calculate(*args, **kwargs):
    operation = kwargs.get("operation", "add")

    if not args:
        return None
    
    if operation == "add":
        result = sum(args)
    elif operation == "substract":
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
    elif operation == "divide":
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Zero division not allowed"
        result /= num
    else:
        return "Error: operation not allowed"
    
    return result

print(calculate(1,2,3,5,6, operation="add"))
print(calculate(1,2,3,5,6, operation="substract"))
print(calculate(1,2,3,5,6, operation="multiply"))