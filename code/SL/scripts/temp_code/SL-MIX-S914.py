from functools import reduce
from itertools import combinations

def encode_dna(seq):
    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return [mapping[nucleotide] for nucleotide in seq]

def compute_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b) if a and b else 0

class HashProcessor:
    def __init__(self, modulus=10007):
        self.modulus = modulus
    
    def hash_sequence(self, seq):
        hash_val = 0
        for num in seq:
            hash_val = (hash_val * 5 + num) % self.modulus
        return hash_val

dna_sequences = ['ATGC', 'GGCC', 'TATA']
encoded_sequences = list(map(encode_dna, dna_sequences))
lcm_values = []
for seq in encoded_sequences:
    if len(seq) >= 2:
        pairs = list(combinations(seq, 2))
        current_lcms = [compute_lcm(a, b) for a, b in pairs]
        lcm_values.append(max(current_lcms) if current_lcms else 0)
    else:
        lcm_values.append(0)

processor = HashProcessor()
hashed_lcms = [processor.hash_sequence([val]) for val in lcm_values]
checksum = reduce(lambda x, y: (x ^ y) + 17, hashed_lcms, 0)
print(f"Result: {checksum}")