def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1
    
    # Irrelevant computation: counting non-letter characters
    digit_count = len([c for c in input_str if c.isdigit()])
    special_char_count = len([c for c in input_str if not c.isalnum()])
    
    # Semi-relevant transformation
    frequency_set = set(char_frequency.values())
    unique_frequencies = sorted(frequency_set, reverse=True)

    # Dummy filtering with lambda (not used later)
    high_freq_filter = list(filter(lambda x: x > 2, char_frequency.values()))
    
    return char_frequency, unique_frequencies


def transform_data(raw_freq, scaling_factor=1.5):
    scaled_values = []
    for freq in raw_freq.values():
        adjusted = freq * scaling_factor
        if adjusted % 1 == 0:
            scaled_values.append(int(adjusted))
        else:
            scaled_values.append(round(adjusted, 2))
    
    # Dead code path (never executed due to logic)
    if len(scaled_values) < 0:
        scaling_factor += 10
        
    return scaled_values


def calculate_efficiency(data_list):
    total = sum(data_list)
    count = len(data_list)
    
    # Early termination condition (distractor)
    if count == 0:
        return 0
    
    average = total / count
    variance = sum((x - average) ** 2 for x in data_list) / count
    efficiency = (average ** 2) / (variance + 1)  # Avoid division by zero
    
    # Extra unused metrics
    max_value = max(data_list)
    min_value = min(data_list)
    range_value = max_value - min_value
    
    return round(efficiency, 4)

# Main execution
raw_text = "The quick brown fox jumps over the lazy dog multiple times daily!"

# Step 1: Analyze character patterns
freq_map, uniq_freqs = analyze_text_patterns(raw_text)

# Step 2: Transform frequencies
transformed_freqs = transform_data(freq_map, scaling_factor=2.0)

# Step 3: Calculate derived statistics
length_metric = len(transformed_freqs)
dummy_weighted_sum = sum(i * v for i, v in enumerate(transformed_freqs))

# Step 4: Compute efficiency score
efficiency_score = calculate_efficiency(transformed_freqs)

# Output target result
print(f"Result: {efficiency_score}")