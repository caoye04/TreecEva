from functools import reduce
from collections import namedtuple

# Define nucleotide bitmasks
NUCLEOTIDE_MASKS = {
    'A': 0b0001,
    'T': 0b0010,
    'G': 0b0100,
    'C': 0b1000
}

# Transformation function using closure
def create_hash_transformer(shift_val, xor_mask):
    return lambda x: ((x << shift_val) & 0xF) ^ xor_mask

# Genomic signature dataclass
class GenomicSignature:
    def __init__(self, seq_id, hash_val):
        self.seq_id = seq_id
        self.hash_val = hash_val
    
    def apply_transformation(self, transformer):
        self.hash_val = transformer(self.hash_val)
        return self

# Process DNA sequence
dna_sequence = "ATGCGTA"
base_hash = reduce(lambda acc, nuc: acc ^ NUCLEOTIDE_MASKS[nuc], dna_sequence, 0)

# Create transformer with dynamic programming cache for efficiency
transform_cache = {}
def cached_transform(x, shift, mask):
    key = (x, shift, mask)
    if key not in transform_cache:
        transform_func = create_hash_transformer(shift, mask)
        transform_cache[key] = transform_func(x)
    return transform_cache[key]

# Apply multi-step transformation
signature_obj = GenomicSignature("EXP_042", base_hash)
intermediate_result = cached_transform(signature_obj.hash_val, 2, 0b1010)
signature_obj.hash_val = intermediate_result

# Final transformation step
transformer_func = create_hash_transformer(1, 0b1100)
final_signature = signature_obj.apply_transformation(transformer_func).hash_val

print(f"Result: {final_signature}")