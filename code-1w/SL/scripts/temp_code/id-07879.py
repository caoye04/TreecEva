from collections import defaultdict

# Simulate frequency analysis of character transitions in a ciphered DNA sequence
dna_sequence = "AGCTAGGGCTAGCGTATCGATCGATCGATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

# Step 1: Build transition pairs
transitions = [dna_sequence[i:i+2] for i in range(len(dna_sequence) - 1)]

# Step 2: Count transition frequencies using defaultdict
transition_count = defaultdict(int)
for pair in transitions:
    transition_count[pair] += 1

# Misleading distraction: Nucleotide composition analysis (not used in final result)
nucleotide_count = {base: dna_sequence.count(base) for base in "AGCT"}
total_bases = sum(nucleotide_count.values())
base_ratios = {k: v / total_bases for k, v in nucleotide_count.items()}

# Step 3: Filter rare transitions (frequency >= 3)
significant_transitions = {k: v for k, v in transition_count.items() if v >= 3}

# Step 4: Map transitions to numeric codes using XOR hashing (relevant)
transition_hash = {}
for idx, (pair, freq) in enumerate(sorted(significant_transitions.items())):
    hash_val = 0
    for char in pair:
        hash_val ^= ord(char)  # Simple XOR over ASCII values
    transition_hash[pair] = hash_val

# Step 5: Compute weighted checksum with position and frequency
# Distractor: unused helper lambda
unused_helper = lambda x: (x ** 2 + 3 * x) % 101

# Real computation begins
sorted_transitions = sorted(significant_transitions.items(), key=lambda item: (-item[1], item[0]))  # Sort by freq desc, then lex asc

checksum = 17

# Final loop with key update point
for index, (pair, freq) in enumerate(sorted_transitions):
    intermediate = (freq + transition_hash[pair]) * (index + 1)
    temp_adjust = intermediate // 2
    
    # Key statement
    checksum = (checksum + freq * index) % 97
    
    # More distraction: tracking unused cumulative stats
    if index % 2 == 0:
        dummy_var = temp_adjust - intermediate

# Print final target result
print(f"Result: {checksum}")