def calculate_entropy(freq_dict):
    total = sum(freq_dict.values())
    entropy = 0.0
    for count in freq_dict.values():
        if count > 0:
            probability = count / total
            entropy -= probability * __import__('math').log2(probability)
    return entropy

# Frequency map of nucleotides in a DNA segment
dna_sequence = "ATGCGATCGAGCTAGCTAGCTAGCTTTCGAA"
frequency_map = {}
for base in dna_sequence:
    frequency_map[base] = frequency_map.get(base, 0) + 1

# Calculate Shannon entropy of the sequence
total_entropy = calculate_entropy(frequency_map)

# Irrelevant auxiliary variable (minimal distraction)
max_count = max(frequency_map.values())

Result: {total_entropy}