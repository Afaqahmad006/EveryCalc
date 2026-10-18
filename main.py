
from basic_calculator import calculate
from gpa_calculator import calculate_gpa, calculate_cgpa


def run_basic_calculator():
    print("\n--- Basic Calculator ---")

    operator = input(
        "Choose operation (+, -, *, /, %, ^, sqrt): "
    ).strip().lower()

    try:
        if operator == "sqrt":
            first_number = float(input("Enter number: "))
            result = calculate(first_number, operator)
        else:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            result = calculate(first_number, operator, second_number)

        print(f"Result: {result:g}")

    except ValueError as error:
        print(f"Error: {error}")
    except OverflowError:
        print("Error: The result is too large to calculate.")


def run_gpa_calculator():
    print("\n--- GPA Calculator ---")

    try:
        number_of_courses = int(input("How many courses? "))

        if number_of_courses <= 0:
            print("Error: Enter at least one course.")
            return

        courses = []

        for number in range(1, number_of_courses + 1):
            print(f"\nCourse {number}")

            course_name = input("Course name: ").strip()

            if not course_name:
                course_name = f"Course {number}"

            grade_points = float(
                input(f"Grade points for {course_name} (0-4): ")
            )

            credit_hours = float(
                input(f"Credit hours for {course_name}: ")
            )

            courses.append((grade_points, credit_hours))

        gpa = calculate_gpa(courses)

        print(f"\nSemester GPA: {gpa:.2f}")

    except ValueError as error:
        print(f"Error: {error}")

def run_cgpa_calculator():
    print("\n--- CGPA Calculator ---")

    try:
        number_of_semesters = int(input("How many semesters? "))

        if number_of_semesters <= 0:
            print("Error: Enter at least one semester.")
            return

        semesters = []

        for number in range(1, number_of_semesters + 1):
            print(f"\nSemester {number}")

            semester_gpa = float(
                input("Enter semester GPA (0-4): ")
            )

            credit_hours = float(
                input("Enter total semester credit hours: ")
            )

            semesters.append((semester_gpa, credit_hours))

        cgpa = calculate_cgpa(semesters)

        print(f"\nYour CGPA: {cgpa:.2f}")

    except ValueError as error:
        print(f"Error: {error}")
def main():
    while True:
        print("\n===== EveryCalc =====")
        print("1. Basic Calculator")
        print("2. GPA Calculator")
        print("3. CGPA Calculator")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_basic_calculator()
        elif choice == "2":
            run_gpa_calculator()
        elif choice == "3":
            run_cgpa_calculator()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
