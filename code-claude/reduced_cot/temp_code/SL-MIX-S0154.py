def process_text(text_data):
    # Process text to extract numerical values
    word_lengths = [len(word) for word in text_data.split()]
    char_frequencies = {}
    
    for char in text_data:
        if char.isalpha():
            char_frequencies[char.lower()] = char_frequencies.get(char.lower(), 0) + 1
    
    # Calculate metrics that won't be used
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    max_frequency = max(char_frequencies.values()) if char_frequencies else 0
    entropy_simulation = sum([v * len(k) for k, v in char_frequencies.items()]) % 17
    
    # Extract only the values we need
    key_values = []
    for word in text_data.split():
        if word[0].lower() in 'aeiou':
            # Words starting with vowels have special weight
            key_values.append(len(word) * 2)
        else:
            # Words starting with consonants
            key_values.append(len(word))
    
    return key_values

def analyze_data(data_points):
    # This function performs various analyses but only some are relevant
    sorted_data = sorted(data_points)
    reversed_data = sorted_data[::-1]
    
    # Calculate several metrics
    sum_values = sum(data_points)
    product_values = 1
    for val in data_points[:3]:  # Only use first 3 values
        product_values *= val
    
    # Misleading calculations
    median = sorted_data[len(sorted_data) // 2]
    mean = sum(sorted_data) / len(sorted_data)
    harmonic_mean = len(sorted_data) / sum(1/x for x in sorted_data if x != 0)
    
    # The key calculation
    weighted_sum = sum([data_points[i] * (i+1) for i in range(len(data_points))])
    
    # More distraction
    transformed = list(map(lambda x: x**2 % 10, data_points))
    filtered = list(filter(lambda x: x > 5, data_points))
    
    return {
        'sum': sum_values,
        'product': product_values,
        'median': median,
        'mean': mean,
        'weighted_sum': weighted_sum,
        'harmonic': harmonic_mean,
        'transformed': transformed,
        'filtered': filtered
    }

def score_calculator(data_dict):
    # Complex scoring function with many branches
    base_score = data_dict['weighted_sum'] % 100
    
    # Misleading operations that don't affect final result
    if data_dict['median'] > data_dict['mean']:
        adjustment = (data_dict['median'] - data_dict['mean']) * 0.5
        temp_score = base_score + adjustment
    else:
        adjustment = (data_dict['mean'] - data_dict['median']) * 0.3
        temp_score = base_score - adjustment
    
    # Dead code path - never used
    if sum(data_dict['transformed']) > 50:
        complexity_factor = len(data_dict['filtered']) / len(data_dict['transformed'])
    else:
        complexity_factor = 0.75
    
    # The actual calculation that matters
    product_factor = data_dict['product'] % 17
    
    # More misleading calculations
    if product_factor > 10:
        final_value = base_score + product_factor
    else:
        final_value = base_score * 2 - product_factor
    
    return final_value

# Main execution
sample_text = "The quick brown fox jumps over a lazy dog"

# Misleading variables
decoy_data = [8, 15, 23, 42, 16]
decoy_result = sum(decoy_data) * 2

# Process that actually matters
processed_data = analyze_data(process_text(sample_text))
final_score = score_calculator(processed_data)

# Print result
print(f"Decoy result: {decoy_result}")
print(f"Result: {final_score}")