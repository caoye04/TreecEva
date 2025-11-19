import itertools
import string

def base36_decode(encoded_str):
    return int(encoded_str, 36)

def calculate_permutation_signature(elements):
    return sum(len(list(itertools.permutations(elements, r))) for r in range(1, len(elements)+1))

# Network packet signatures encoded in base-36
packet_signatures = ['Z9', '1A2', 'B3C', 'Y7X']

# Decode signatures and analyze permutation patterns
signature_values = [base36_decode(sig) for sig in packet_signatures]
permutation_scores = [calculate_permutation_signature(list(str(val))) for val in signature_values]

# Identify common threat indicators using set operations
threat_indicators = {12, 15, 18, 21, 24}
signature_set = frozenset(permutation_scores)
common_indicators = threat_indicators & signature_set

# Calculate weighted threat score
weight_map = {score: idx+1 for idx, score in enumerate(sorted(permutation_scores))}
threat_score = sum(weight_map[score] * score for score in common_indicators)

print(f"Result: {threat_score}")