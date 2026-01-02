def analyze_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

# Irrelevant helper function (distractor)
def calculate_entropy(frequency_dict):
    import math
    total = sum(frequency_dict.values())
    entropy = 0
    for count in frequency_dict.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Semi-relevant preprocessing step
def normalize_values(freq_dict):
    if not freq_dict:
        return {}
    max_freq = max(freq_dict.values())
    return {k: round(v / max_freq, 3) for k, v in freq_dict.items()}

# Core logic with state tracking and dictionary operations
def process_metrics(raw_data, config):
    temp_results = {}
    cumulative = 0
    
    # Simulate data filtering and transformation
    for key, value in raw_data.items():
        if len(key) % 2 == 1:  # Only odd-length keys
            capped = min(value, config['limit'])
            adjusted = capped * config['multiplier']
            temp_results[key] = adjusted
            cumulative += adjusted
    
    # Additional processing that affects result
    modifier = len(temp_results) % 7
    if modifier > 0:
        cumulative = int(cumulative / modifier)  # integer division
    
    # Dead code path (distractor)
    if False:
        fallback = 0
        for v in temp_results.values():
            fallback += v * 0.1
        cumulative += fallback
    
    # Final adjustment based on auxiliary condition
    extra_boost = 0
    for val in temp_results.values():
        if val % 2 == 0:
            extra_boost += 1
    
    final_score = cumulative + extra_boost * config['bonus']
    return final_score

# Main execution block
message = "QuantumResonanceField"
data = analyze_frequency(message)
normalized_data = normalize_values(data)

# Unused entropy computation (distractor)
entropy_value = calculate_entropy(data)

thresholds = {
    'limit': 15,
    'multiplier': 3,
    'bonus': 4
}

intermediate_sum = 0
for letter, count in normalized_data.items():
    intermediate_sum += int(count * 100)

# Key statement
final_score = process_metrics(data, thresholds)
print(f"Result: {final_score}")