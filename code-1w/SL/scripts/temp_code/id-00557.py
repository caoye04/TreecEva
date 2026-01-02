from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    probabilities = [count / total for count in freq_map.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

def analyze_sequence_complexity(sequence):
    raw_counts = Counter(sequence)
    filtered_counts = {k: v for k, v in raw_counts.items() if v >= 2}
    
    # Irrelevant distraction: unused variable (minimal interference)
    normalized_scores = [x / 10.0 for x in raw_counts.values()]
    
    frequency_map = Counter(filtered_counts)
    total_entropy = calculate_entropy(frequency_map)
    return total_entropy

# Main execution
data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'E', 'C', 'C']
total_entropy = analyze_sequence_complexity(data_stream)
print(f"Result: {total_entropy}")