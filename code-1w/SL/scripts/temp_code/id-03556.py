def main():
    # Simulate student test results with correct and attempted questions
    total_questions = 50
    correct_answers = 38
    time_bonus_seconds = 45  # Bonus time in seconds

    # Irrelevant distraction: unused variable (minimal interference)
    max_time_limit = 3600

    # Calculate base accuracy as percentage
    accuracy = (correct_answers / total_questions) * 100

    # Determine if bonus applies using conditional expression
    performance_multiplier = 1.2 if time_bonus_seconds > 30 else 1.0

    # Use list comprehension to generate weighted section scores (simulated sections)
    section_weights = [0.8, 1.0, 1.2, 0.9]
    base_section_scores = [accuracy * w for w in section_weights]

    # Aggregate using average adjusted score
    avg_adjusted_score = sum(base_section_scores) / len(base_section_scores)

    # Apply performance multiplier
    final_score = avg_adjusted_score * performance_multiplier

    # Output result as required
    print(f"Target result: {final_score}")

main()