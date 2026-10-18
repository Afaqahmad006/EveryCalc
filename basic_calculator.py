
def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number

    elif operator == "-":
        return first_number - second_number

    elif operator == "*":
        return first_number * second_number

    elif operator == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number

    else:
        raise ValueError("Invalid operator.")

