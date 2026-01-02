def calculate_final_score(results, weights):
    weighted_sum = 0
    total_credits = 0
    
    # Use enumerate and zip to align results with their respective credit weights
    for i, (score, credit) in enumerate(zip(results, weights)):
        if score >= 50:  # Only count passing scores
            weighted_sum += score * credit
            total_credits += credit
    
    # Calculate final weighted average
    return weighted_sum / total_credits if total_credits > 0 else 0

# Simulated exam results and corresponding course credit weights
test_results = [78, 45, 85, 52, 91]
credit_hours = [3, 2, 4, 3, 4]

# Irrelevant auxiliary variable (minimal distraction)
avg_passing = 70

# Key computation
final_average = calculate_final_score(test_results, credit_hours)
total_score = round(final_average, 3)

print(f"Result: {total_score}")