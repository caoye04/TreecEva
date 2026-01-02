from collections import Counter

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * __import__('math').log2(probability)
    return round(entropy, 3)

def analyze_sequence_dynamics(sequence):
    # Count character frequencies using Counter
    frequency_map = Counter(sequence)
    
    # Extract positions of vowels using enumerate
    vowel_positions = [i for i, char in enumerate(sequence) if char.lower() in 'aeiou']
    
    # Pair adjacent characters using zip (with offset), though not used in final result
    adj_pairs = list(zip(sequence, sequence[1:]))
    
    # Calculate entropy based on frequency distribution
    total_entropy = calculate_entropy(frequency_map)
    
    # Return entropy (other variables are side products)
    return total_entropy

# Input sequence
input_seq = "abracadabra"

# Execute function
total_entropy = analyze_sequence_dynamics(input_seq)
print(f"Result: {total_entropy}")