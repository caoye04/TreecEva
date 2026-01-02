def analyze_text_quality(text):
    words = text.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    upper_case_count = sum(1 for c in text if c.isupper())
    exclamation_count = text.count('!')
    
    # Distractor variables (not used in final score)
    char_frequency_map = {c: text.lower().count(c) for c in 'aeiou'}
    total_vowels = sum(char_frequency_map.values())
    redundant_sum = sum([i*i for i in range(3)])  # Irrelevant computation

    score = avg_length * 2 + upper_case_count - exclamation_count
    return score


def filter_noisy_entries(data_list):
    filtered = []
    for entry in data_list:
        cleaned = entry.strip().lower()
        if 'spam' not in cleaned and len(cleaned) > 5:
            # Semi-relevant transformation
            title_version = cleaned.title()
            filtered.append(title_version)
    return filtered


def calculate_final_score(items):
    base_values = []
    temp_accumulator = 0
    
    for item in items:
        length_contribution = len(item) % 7
        temp_accumulator += length_contribution
        
        # Use string method to extract key feature
        if item.startswith('A') or item.endswith('ing'):
            base_values.append(temp_accumulator)
        elif 'Error' in item:
            continue  # Dead code path in this context
        else:
            base_values.append(len(item))
    
    # Real computation path
    raw_total = sum(base_values)
    adjustment_factor = 0.8 if raw_total > 10 else 1.2
    adjusted_total = raw_total * adjustment_factor
    
    # Final nonlinear transformation
    final_score = int(adjusted_total ** 1.1)  # Key result
    
    # Unused intermediate
    peak_value = max(base_values) if base_values else 0
    buffer_string = ''.join([str(v) for v in base_values])
    
    return final_score

# Main execution flow
raw_input_data = [
    "Amazing performance today!",
    "Correct algorithm execution",
    "Spam entry should be filtered out",
    "Processing incoming stream",
    "Finalizing the arrangement"
]

# Step 1: Text quality analysis (produces unused metric)
quality_metrics = [analyze_text_quality(entry) for entry in raw_input_data]
mean_metric = sum(quality_metrics) / len(quality_metrics)

# Step 2: Filter entries
processed_data = filter_noisy_entries(raw_input_data)

# Step 3: Calculate final score
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")