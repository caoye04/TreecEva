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

def analyze_sequence_complexity(sequence):
    # Count frequency of each element
    frequency_map = Counter(sequence)
    
    # Calculate baseline statistics (some distraction)
    unique_elements = len(frequency_map)
    max_frequency = max(frequency_map.values())
    
    # Core computation: Shannon entropy as measure of complexity
    total_entropy = calculate_entropy(frequency_map)
    
    # Irrelevant scaling (minimal interference)
    normalized_score = total_entropy / math.log2(unique_elements) if unique_elements > 1 else 0.0
    
    return total_entropy

# Main execution
data_stream = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
total_entropy = analyze_sequence_complexity(data_stream)
print(f"Result: {total_entropy}")