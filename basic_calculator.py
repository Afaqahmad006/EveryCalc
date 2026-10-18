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
