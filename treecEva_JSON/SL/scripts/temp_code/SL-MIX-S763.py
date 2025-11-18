import itertools

def encode_sequence(dna_seq):
    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return [mapping[nucleotide] for nucleotide in dna_seq]

def divide_and_process(segment):
    if len(segment) <= 1:
        return segment
    mid = len(segment) // 2
    left = divide_and_process(segment[:mid])
    right = divide_and_process(segment[mid:])
    return sorted(left + right)

def compute_combinations(processed_segment):
    total = 0
    for r in range(1, min(3, len(processed_segment)) + 1):
        for combo in itertools.combinations(processed_segment, r):
            product = 1
            for num in combo:
                product *= num
            total += product
    return total

def process_batch(sequences):
    checksum = 0
    for seq in sequences:
        encoded = encode_sequence(seq)
        processed = divide_and_process(encoded)
        checksum += compute_combinations(processed)
    return checksum

# Batch of DNA sequences to analyze
lab_sequences = [
    "ATG",
    "CGT",
    "AAC"
]

final_checksum = process_batch(lab_sequences)
print(f"Result: {final_checksum}")