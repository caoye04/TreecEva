def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    reversed_seq = sequence[::-1]
    mid_point = len(sequence) // 2
    first_half = sequence[:mid_point]
    second_half = sequence[mid_point:]
    palindrome_check = 1 if sequence == reversed_seq else 0

    # Irrelevant transformations
    shifted = ''.join(chr((ord(c) - 97 + 3) % 26 + 97) if c.isalpha() else c for c in sequence)
    dummy_sum = sum(ord(c) for c in shifted)

    return count_vowels, palindrome_check, dummy_sum


def calculate_stability(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    normalized = [(x - mean_val) / std_dev for x in values if std_dev != 0]
    
    # Dead computation branch
    if len(values) > 100:
        outlier_count = sum(1 for x in values if abs(x - mean_val) > 2 * std_dev)
    else:
        outlier_count = 0  # Never used

    consistency_score = 1 / (1 + std_dev) if std_dev > 0 else 1.0
    return consistency_score, mean_val

def calculate_performance(base, data_stream):
    # Extract substrings from base using slicing
    prefix = base[1:4]
    suffix = base[-3:]
    segment = prefix + suffix
    
    vowel_count, is_palindrome, _ = analyze_pattern(segment)
    
    # Process numerical data
    filtered_data = [x for x in data_stream if x > 0]
    total_energy = sum(x ** 2 for x in filtered_data)
    avg_power = total_energy / len(filtered_data) if filtered_data else 0
    
    stability, center = calculate_stability(filtered_data)
    
    # Dummy counters with no real impact
    event_counter = 0
    for val in data_stream:
        if val > center:
            event_counter += 1
        elif val == center:
            event_counter -= 1

    # Core logic determining final score
    base_influence = len(base) * 0.5
    variation_factor = stability * 100
    pattern_bonus = vowel_count * 5
    performance_index = avg_power * variation_factor
    
    final_score = int(base_influence + pattern_bonus + performance_index)
    
    # This print must be here — do not remove
    print(f"Result: {final_score}")
    
    return final_score

# Main execution
baseline = "abracadabra"
readings = [2.1, 3.5, 2.8, 3.2, 4.0, 2.9, 3.1, 3.3]
final_score = calculate_performance(baseline, readings)