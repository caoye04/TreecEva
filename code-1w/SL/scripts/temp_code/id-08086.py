def calculate_total(marks, modifiers):
    base_total = sum(marks)
    adjustment_factor = 1.0
    
    # Apply dynamic adjustment using lambda and enumerate
    for i, mod in enumerate(modifiers):
        if i % 2 == 0:
            adjustment_factor *= (1 + mod / 100)
    
    # Irrelevant distraction: case conversion (no effect on logic)
    status = 'PASS'
    status = status.lower()  # Distractor: not used later
    
    # Use slicing to consider only first 4 grades
    effective_base = sum(marks[:4])
    
    # Final computation
    raw_score = effective_base * adjustment_factor
    final_score = int(round(raw_score))
    return final_score

# Input data
grades = [88, 92, 75, 85, 96]
adjustments = [5, -2, 10, 0]  # Only even-indexed values affect factor

# Key statement
final_score = calculate_total(grades, adjustments)
print(f"Result: {final_score}")