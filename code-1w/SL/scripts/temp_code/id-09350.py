from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

def analyze_sequence(seq):
    frequency_map = Counter(seq)
    unique_elements = len(frequency_map)
    max_frequency = max(frequency_map.values())
    
    # Auxiliary metric – not used in final result
    redundancy = len(seq) - unique_elements
    
    total_entropy = calculate_entropy(frequency_map)
    return total_entropy

# Simulate character sequence from a constrained alphabet
data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'D', 'C', 'A']
result = analyze_sequence(data_stream)
print(f"Result: {result}")