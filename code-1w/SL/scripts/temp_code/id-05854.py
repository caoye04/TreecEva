def process_student_data(students):
    base_multiplier = 1.2
    threshold = 75
    temp_results = []
    adjustment = 0

    for idx, (name, score) in enumerate(students):
        if score < threshold:
            adjusted = score * base_multiplier
        else:
            adjusted = score + 5

        # Irrelevant transformation
        inverted = 100 - adjusted
        temp_results.append((idx, adjusted))

        # Dead code branch (never used later)
        if len(name) > 6:
            adjustment += 1

    return temp_results


def calculate_total(grades, bonuses):
    total = 0
    bonus_factor = 1.1
    penalty = 0.9
    extra_buffer = []

    # List comprehension with zip: relevant computation
    weighted_grades = [g * bonus_factor for g, b in zip(grades, bonuses) if b > 0]

    # Misleading list comprehension (not used)
    [extra_buffer.append(g * 0.1) for g in grades if g < 60]

    # Another irrelevant variable
    avg_grade = sum(grades) / len(grades) if grades else 0

    for grade in weighted_grades:
        if grade > 80:
            total += grade * bonus_factor
        else:
            total += grade * penalty

    return int(total)

# Main data
student_records = [('Alice', 82), ('Bob', 67), ('Charlie', 93), ('Diana', 74)]
bonus_points = [10, 0, 15, 5]

# Process but do not use result directly
processed = process_student_data(student_records)

# Extract grades only
extracted_scores = [score for _, score in student_records]

# Key computation
final_score = calculate_total(extracted_scores, bonus_points)

print(f"Result: {final_score}")