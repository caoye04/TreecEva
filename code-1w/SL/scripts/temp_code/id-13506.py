def calculate_performance(base, data):
    adjustment_factor = 1.2
    threshold = base * 0.75
    filtered = [x for x in data if x > threshold]
    deviations = [(x - base) ** 2 for x in filtered]
    avg_dev = sum(deviations) / len(deviations) if deviations else 0
    
    # Distractor: irrelevant transformation chain
    temp_result = ''.join([chr(97 + (i % 26)) for i in range(len(data))])
    temp_hash = sum([ord(c) for c in temp_result[:10]])
    noise_offset = temp_hash % 13 - 6
    
    # Conditional expression with lambda (required feature)
    apply_bonus = (lambda x: x * 1.1) if sum(filtered) > base * 3 else (lambda x: x)
    raw_score = apply_bonus(sum(filtered) / len(filtered))
    
    # Multiple assignments and slicing distraction
    first_half, second_half = filtered[:len(filtered)//2], filtered[len(filtered)//2:]
    mirror_effect = first_half[::-1]
    
    # Real computation path
    stability_ratio = len(filtered) / len(data)
    final_score = raw_score * stability_ratio + (5 if noise_offset > 0 else 0)
    
    # Dead code path (irrelevant)
    if len(mirror_effect) > 100:
        final_score -= 999  # unreachable
    
    return final_score

# Main execution
baseline = 42
readings = [38, 45, 50, 33, 60, 44, 55, 40, 48, 52]

# Key statement
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")