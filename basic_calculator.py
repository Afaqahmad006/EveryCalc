import math


def calculate(first_number, operator, second_number=None):
    if operator == "sqrt":
        if first_number < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(first_number)

    if second_number is None:
        raise ValueError("This operation requires a second number.")

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

    elif operator == "%":
        return first_number * second_number / 100

    elif operator == "^":
        if first_number == 0 and second_number < 0:
            raise ValueError("Zero cannot have a negative power.")

        result = first_number ** second_number

        if isinstance(result, complex):
            raise ValueError("Result must be a real number.")

        return result

    else:
        raise ValueError("Invalid operator.")
