# EveryCalc

EveryCalc is a Python command-line application that combines basic mathematical calculations with GPA and CGPA calculations in one easy-to-use program.

## Features

### 1. Basic Calculator
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Percentage calculations (%)
- Power calculations (^)
- Square-root calculations (sqrt)
- Input validation and error handling
- Protection against division by zero

### 2. GPA Calculator
- Calculate semester GPA using course grade points and credit hours.
- Support multiple courses in one semester.
- Validate grade points and credit hours.
- Display the final GPA rounded to two decimal places.

### 3. CGPA Calculator
- Calculate cumulative GPA across multiple semesters.
- Enter each semester's GPA and total credit hours.
- Calculate a credit-hour-weighted CGPA.
- Validate semester GPAs and credit hours.

## Technologies

- Python
- Git
- GitHub
- uv

## Requirements

- Python 3
- uv (Python project and tool manager)

## How to Run

Clone the repository or download the project files.

Run EveryCalc from the project directory:

```bash
uv run main.py
```

Follow the menu and select the calculator you want to use.

## Running Tests

Run all automated tests with:

```bash
uv run python -m unittest discover -s tests -v
```

## Project Structure

```text
EveryCalc/
├── main.py
├── basic_calculator.py
├── gpa_calculator.py
├── README.md
├── .gitignore
└── tests/
    ├── test_basic_calculator.py
    └── test_gpa_calculator.py
```

## GPA Formula

GPA is calculated using credit-hour weighting:

GPA = Sum of (Grade Points × Credit Hours) / Total Credit Hours

## CGPA Formula

CGPA is calculated by weighting each semester GPA by that semester's total credit hours:

CGPA = Sum of (Semester GPA × Semester Credit Hours) / Total Credit Hours Across Semesters

The calculator uses a 4.0 grade-point scale. Confirm your university's grading rules for official academic results.

## Development Goals

- Practice Python functions and modular programming.
- Improve input validation and error handling.
- Write and run automated tests.
- Learn Git version control and GitHub collaboration workflows.
