from math import log

def calculate_entropy(sequence):
    char_frequency = {}
    for char in sequence:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    total_chars = len(sequence)
    probabilities = [count / total_chars for count in char_frequency.values()]
    
    # Irrelevant variable (minimal distraction)
    normalized_vals = [p**2 for p in probabilities]
    
    entropy_components = []
    for p in probabilities:
        if p > 0:
            entropy_components.append(-p * log(p, 2))
    
    raw_entropy = sum(entropy_components)
    
    # Simulate data filtering based on threshold
    indexed_data = list(enumerate([log(p, 2) for p in probabilities if p > 0]))
    filtered_data = [p for p in probabilities if p > 0.1]
    
    # Core computation with lambda and map
    log_values = [log(p, 2) for p in filtered_data]
    product_pairs = zip(filtered_data, log_values)
    total_entropy = sum(map(lambda x: x[0] * x[1], product_pairs))
    
    # Unused but plausible variable (low interference)
    max_prob = max(probabilities)
    
    print(f"Result: {total_entropy}")
    return total_entropy

# Input string with non-uniform distribution
text_sequence = "aabbbccccddddd"
calculate_entropy(text_sequence)