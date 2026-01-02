def analyze_pattern(sequence):
    if not sequence:
        return 0
    avg = sum(sequence) / len(sequence)
    variance = sum((x - avg) ** 2 for x in sequence) / len(sequence)
    normalized_variance = variance / (avg + 1e-5)
    return round(normalized_variance, 3)


def extract_features(raw_data):
    cleaned = raw_data.strip().replace(' ', '').split(',')
    ints = [int(x) for x in cleaned if x.isdigit()]
    parity_flags = [1 if n % 2 == 0 else 0 for n in ints]
    total_even = sum(parity_flags)
    total_odd = len(ints) - total_even
    return ints, total_even, total_odd

def calculate_rating(convergence, stability_factor):
    base_rating = 50
    adjustment = 0
    
    if convergence > 0.7:
        adjustment += 15
    elif convergence > 0.4:
        adjustment += 8
    else:
        adjustment -= 10
    
    # Distractor: Irrelevant string processing
    status_msg = "System nominal" if stability_factor > 0.5 else "Status degraded"
    status_code = status_msg.lower().count('s') + len(status_msg.split())
    
    # Real impact branch
    if stability_factor > 0.6:
        adjustment += 12
    elif stability_factor > 0.3:
        adjustment += 5
    else:
        adjustment -= 20
    
    # Additional distractor: dead computation with strings
    metadata_tag = f"RAT-{stability_factor:.2f}".upper().replace('-', '_')
    tag_value = len(metadata_tag) * 2  # unused
    
    final = base_rating + adjustment
    return int(final)

# Main execution
raw_input = " 12, 15, 18, 22, 25, 30, 33 "
values, even_count, odd_count = extract_features(raw_input)

# Compute derived metrics
mean_val = sum(values) // len(values)
deviations = [abs(v - mean_val) for v in values]
convergence = analyze_pattern(deviations)

# Dummy variables for distraction
redundant_sum = sum([v**2 for v in deviations if v < 10])
temp_flag = even_count >= odd_count
flag_text = "balanced" if temp_flag else "skewed"
checksum_str = flag_text + str(redundant_sum)

# Stability determined by ratio of low-deviation points
effective_stable = sum(1 for d in deviations if d <= mean_val * 0.5)
stability_factor = effective_stable / len(deviations)

# Key statement
final_score = calculate_rating(convergence, stability_factor)

print(f"Result: {final_score}")