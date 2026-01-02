def calculate_final_score(ranks, coeffs):
    total_score = 0
    sorted_ranks = sorted(ranks)
    offset = len(coeffs) - len(sorted_ranks)
    
    # Apply weighted sum using enumerate for index-aware computation
    for i, rank in enumerate(sorted_ranks):
        total_score += (rank * coeffs[i]) + i
    
    # Irrelevant distraction: unused variable
    temp_result = [x ** 0.5 for x in ranks if x > 0]
    
    # Extra step: adjust score based on coefficient sum threshold
    coeff_sum = sum(coeffs)
    if coeff_sum > 10:
        total_score -= 5
    else:
        total_score += 2
    
    return total_score

# Main execution
weights = [3, 1, 4, 2]
rankings = [8, 5, 9]

# Distractor: unrelated list transformation (minimal interference)
doubled_ranks = [r * 2 for r in rankings]

# Key computation
result = calculate_final_score(rankings, weights)
total_score = result

print(f"Result: {total_score}")