def calculate_gpa(courses):
    if not courses:
        raise ValueError("At least one course is required.")

    total_weighted_points = 0.0
    total_credit_hours = 0.0

    for grade_points, credit_hours in courses:
        if not 0 <= grade_points <= 4.0:
            raise ValueError("Grade points must be between 0 and 4.")

        if credit_hours <= 0:
            raise ValueError("Credit hours must be greater than zero.")

        total_weighted_points += grade_points * credit_hours
        total_credit_hours += credit_hours

    return total_weighted_points / total_credit_hours
