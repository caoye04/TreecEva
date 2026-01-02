def process_performance(data_str, bonus):
    # Irrelevant preprocessing: counting characters (distractor)
    char_count = len(data_str)
    temp_offset = char_count % 7
    
    # Extract numeric values from comma-separated string
    str_values = data_str.split(',')
    parsed_values = []
    for s in str_values:
        if s.strip().isdigit():
            parsed_values.append(int(s.strip()))
    
    # Misleading transformation: reverse and shift (partially irrelevant)
    reversed_vals = [x + temp_offset for x in reversed(parsed_values)]
    shifted_sum = sum(reversed_vals) - temp_offset * len(reversed_vals)

    # Actual computation begins: filter even-indexed original values
    relevant_subset = [parsed_values[i] for i in range(0, len(parsed_values), 2)]
    
    # Compute base score with conditional boosts
    base_score = 0
    for val in relevant_subset:
        if val > 50:
            base_score += val * 1.1
        elif val >= 30:
            base_score += val * 1.2
        else:
            base_score += val
    
    # Bonus logic with string-based condition (uses string method)
    trigger_word = "BOOST"
    activation_flag = trigger_word.lower() in data_str.lower()
    
    # Secondary distractor: unused statistical calculation
    avg_val = sum(parsed_values) / len(parsed_values) if parsed_values else 0
    variance_proxy = sum((x - avg_val) ** 2 for x in parsed_values) / len(parsed_values) if parsed_values else 0

    # Final scoring with conditional bonus (only this matters)
    if activation_flag and bonus > 0:
        final_score = int(base_score * bonus)
    else:
        final_score = int(base_score)

    return final_score

# Main execution
raw_data = "45,67,82,23,55,12,91"
bonus_multiplier = 2
final_score = process_performance(raw_data, bonus_multiplier)
print(f"Result: {final_score}")