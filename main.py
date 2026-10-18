
from basic_calculator import calculate


def run_basic_calculator():
    print("\n--- Basic Calculator ---")

    try:
        first_number = float(input("Enter first number: "))
        operator = input("Choose operation (+, -, *, /, %, ^): ").strip()
        second_number = float(input("Enter second number: "))

        result = calculate(first_number, operator, second_number)
        print(f"Result: {result:g}")

    except ValueError as error:
        print(f"Error: {error}")


def main():
    while True:
        print("\n===== EveryCalc =====")
        print("1. Basic Calculator")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_basic_calculator()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()

