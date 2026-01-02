def calculate_final_score(values, deductions):
    total = sum(values)
    for i, penalty in enumerate(deductions):
        if i % 2 == 0:
            total -= penalty
        else:
            total -= penalty * 0.5
    return int(total)

# Simulate student test scores with penalty deductions
test_scores = [88, 92, 76, 94, 85]
fine_points = [10, 8, 5, 3]

# Irrelevant auxiliary variable (minimal distraction)
avg_score = sum(test_scores) / len(test_scores)

# Key computation
total_score = calculate_final_score(test_scores, fine_points)

print(f"Result: {total_score}")