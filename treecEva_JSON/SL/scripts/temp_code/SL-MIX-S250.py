import itertools

def custom_hash(s):
    hash_val = 0
    for char in s:
        hash_val = (hash_val * 31 + ord(char)) % 100000007
    return hash_val

def process_dna_sequence(sequence):
    codon_freq = {}
    # Tokenize into codons
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in codon_freq:
            codon_freq[codon] += 1
        else:
            codon_freq[codon] = 1
    
    # Transform frequencies
    transformed_values = []
    for codon, freq in codon_freq.items():
        if freq > 1:
            value = custom_hash(codon) * freq
        else:
            value = custom_hash(codon) + 1000
        transformed_values.append(value)
    
    # Compute checksum
    checksum = 0
    for val in sorted(transformed_values):
        checksum = (checksum + val) % 100000007
    return checksum

# Main execution
sequence_data = "ATGCGTACGTAGCTAGCTACGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
codon_triplets = [sequence_data[i:i+3] for i in range(0, len(sequence_data), 3)]
frequency_map = {}
for triplet in codon_triplets:
    frequency_map[triplet] = frequency_map.get(triplet, 0) + 1

checksum_components = []
for codon_key, count in frequency_map.items():
    match count:
        case 1:
            checksum_components.append(custom_hash(codon_key) + 500)
        case 2:
            checksum_components.append(custom_hash(codon_key) * count)
        case _ if count > 2:
            modified_value = custom_hash(codon_key[:2] + 'X') if len(codon_key) == 3 else 0
            checksum_components.append(modified_value)

checksum_result = sum(checksum_components) % 100000007
print(f"Result: {checksum_result}")