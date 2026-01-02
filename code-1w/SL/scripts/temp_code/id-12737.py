def calculate_final_score():
    # Simulate student assessment results with overlapping criteria
    passed_logic = {"Alice", "Bob", "Charlie", "Diana"}
    passed_syntax = {"Bob", "Charlie", "Eve", "Frank"}
    passed_testing = {"Alice", "Eve", "Diana"}

    # Students who passed both logic and syntax (intersection)
    dual_pass = passed_logic & passed_syntax
    
    # Students who passed only one of the three areas (exclusive to one set)
    unique_to_one = (passed_logic ^ passed_syntax ^ passed_testing) \
                    - (passed_logic & passed_syntax & passed_testing)

    # Count accumulation based on criteria
    base_score = len(dual_pass) * 15
    bonus_per_unique = 10
    extra_credit = len(unique_to_one) * bonus_per_unique
    
    # Apply penalty for missing in testing but passed in others (irrelevant distraction)
    missing_testing = dual_pass - passed_testing
    penalty = len(missing_testing) * 3  # minor deduction

    final_score = base_score + extra_credit - penalty
    return final_score

result = calculate_final_score()
print(f"Result: {result}")