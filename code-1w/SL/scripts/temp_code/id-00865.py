def calculate_performance(base, eff, thresh):
    adjustment = 0
    if eff > thresh:
        adjustment += (eff * 1.5) // 1
    else:
        adjustment -= (thresh - eff) * 0.8

    # Distractor: Irrelevant computation with unused variables
    temp_offset = base ** 0.5
    dummy_flag = temp_offset > 10
    auxiliary_data = [i * 2 for i in range(5) if i % 2 == 0]
    
    # Semi-relevant transformation
    normalized = (base + adjustment) / 2.0
    
    # Conditional expression using string method (required feature)
    status = "optimal" if str(int(normalized)).endswith("5") else "standard"
    
    # Another distractor: complex but unused calculation
    peak_value = max(auxiliary_data) ** 2 if dummy_flag else 0
    fallback_check = peak_value == 0 and len(auxiliary_data) >= 3
    
    # Final logic step
    if status == "optimal":
        normalized += 5.0
    return int(normalized)

# Main execution
baseline = 42
efficiency = 18
threshold = 15

# Additional irrelevant variables (interference)
counterfeit_metric = baseline * efficiency % 7
placeholder_array = [counterfeit_metric + x for x in range(3)]
shadow_copy = placeholder_array[:]

# Key statement
final_score = calculate_performance(baseline, efficiency, threshold)

print(f"Result: {final_score}")