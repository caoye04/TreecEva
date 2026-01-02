def evaluate_performance(output, risk):
    base_efficiency = output * 0.85
    penalty = 0
    
    # Conditional expression for adaptive adjustment
    adjustment = 1.2 if output > 75 else 0.9
    adjusted_efficiency = base_efficiency * adjustment
    
    # Simulate minor side computation (distractor)
    hypothetical_max = 100 * 0.85 * 1.2
    unused_normalization = hypothetical_max / (adjusted_efficiency + 1e-9)
    
    # Risk-based deduction using logical operation
    if risk and adjusted_efficiency > 50:
        penalty = 15
    elif not risk or adjusted_efficiency < 30:
        penalty = 5

    # Lambda function to compute bonus eligibility
    bonus_eligibility = lambda x: x > 60
    bonus = 10 if bonus_eligibility(adjusted_efficiency) and risk == False else 0
    
    # Accumulation of score components
    raw_score = adjusted_efficiency - penalty + bonus
    
    # Extra distraction: irrelevant loop with local state tracking
    temp_buffer = 0
    for i in range(3):
        for j in range(3):
            temp_buffer += (i * j) % 2
    # This affects nothing; just adds cognitive load
    
    final_normalized = raw_score * 0.95  # Final scaling
    return int(final_normalized)

# Main execution context
productivity = 88
risk_factor = True
interim_check = productivity + 12  # Distractor variable
placeholder_data = [1, 1, 2, 3, 5, 8]
filtered_data = list(filter(lambda x: x > 2, placeholder_data))  # Irrelevant filtering

# Key statement
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")