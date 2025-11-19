import itertools
import re

def encode_nucleotide(nuc):
    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return mapping.get(nuc, 0)

def process_dna_sequence(sequence):
    checksums = [0]  # Initial checksum
    for i, nuc in enumerate(sequence):
        index = i + 1
        encoded = encode_nucleotide(nuc)
        new_checksum = (checksums[-1] ^ encoded) + index
        checksums.append(new_checksum)
    return checksums

def find_marker_combinations(sequence, target_sum):
    nucleotides = list(sequence)
    combinations = itertools.combinations(nucleotides, 3)
    valid_count = 0
    for combo in combinations:
        encoded_sum = sum(encode_nucleotide(n) for n in combo)
        if encoded_sum == target_sum:
            valid_count += 1
    return valid_count

# Main execution
if __name__ == "__main__":
    dna_sequence = "ATGCGTAAC"
    
    # Validate sequence using regex
    if not re.fullmatch(r'[ATGC]+', dna_sequence):
        marker_count = 0
    else:
        checksum_list = process_dna_sequence(dna_sequence)
        last_checksum = checksum_list[-1]
        target_modulo = last_checksum % 100
        marker_count = find_marker_combinations(dna_sequence, target_modulo)
    
    print(f"Result: {marker_count}")