import re
from functools import reduce

def encode_nucleotides(seq):
    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return [mapping[nuc] for nuc in seq]

def compute_checksum(segment):
    return reduce(lambda x, y: x ^ y, segment, 0)

dna_fragment = "ATGCCGTA"
encoded_segment = encode_nucleotides(dna_fragment)
filtered_values = [x for x in encoded_segment if x > 1]
checksum = compute_checksum(filtered_values)
marker_detected = re.search(r'G[AT]C', dna_fragment) is not None
adjusted_checksum = checksum + (10 if marker_detected else 0)
final_score = adjusted_checksum if adjusted_checksum % 2 == 0 else adjusted_checksum * 2
print(f"Result: {final_score}")