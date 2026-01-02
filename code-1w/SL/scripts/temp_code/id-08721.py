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
    # Count frequency of each element
    frequency_map = Counter(seq)
    
    # Some auxiliary computation (minimal interference)
    unique_elements = len(frequency_map)
    max_frequency = max(frequency_map.values())
    
    # Core calculation: entropy of the sequence
    total_entropy = calculate_entropy(frequency_map)
    
    # Additional unrelated metric (slight distraction, low interference)
    redundancy = 1 - (entropy / math.log2(unique_elements)) if unique_elements > 1 else 0
    
    return total_entropy

# Example DNA sequence data
sequence = ['A', 'T', 'G', 'C', 'A', 'A', 'T', 'T', 'G', 'G', 'G', 'C']
result = analyze_sequence(sequence)
print(f"Result: {result}")