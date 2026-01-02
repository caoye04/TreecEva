from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy

def analyze_text_pattern(text_data):
    char_count = Counter(text_data)
    filtered_chars = {k: v for k, v in char_count.items() if k.isalpha()}
    normalized_counts = Counter({k.lower(): v for k, v in filtered_chars.items()})
    frequency_map = normalized_counts
    scaling_factor = 1.0
    
    temp_sum = 0
    for idx, (char, count) in enumerate(zip(frequency_map.keys(), frequency_map.values())):
        temp_sum += idx * count
    
    total_entropy = calculate_entropy(frequency_map)
    return total_entropy

# Main execution
input_text = "abracadabra"
total_entropy = analyze_text_pattern(input_text)
print(f"Result: {total_entropy}")