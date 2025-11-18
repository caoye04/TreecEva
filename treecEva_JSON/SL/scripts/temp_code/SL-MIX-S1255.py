from itertools import combinations
from dataclasses import dataclass
from typing import List

genetic_markers = [
    0b110101,
    0b101110,
    0b011011,
    0b111000,
    0b001111
]

@dataclass
class MarkerPair:
    marker_a: int
    marker_b: int
    xor_result: int
    
valid_pairs: List[MarkerPair] = []
stability_score = 0

for m1, m2 in combinations(genetic_markers, 2):
    xor_val = m1 ^ m2
    # Check if the XOR result has even number of 1s AND the first marker is greater than 40
    if (bin(xor_val).count('1') % 2 == 0) and (m1 > 40):
        valid_pairs.append(MarkerPair(m1, m2, xor_val))
        # Additional condition: if the second marker has more 1s than the first
        if bin(m2).count('1') > bin(m1).count('1'):
            stability_score += 1
        else:
            stability_score += 2
    elif not (m1 > 40):  # Explicitly handle the case where first condition fails
        stability_score -= 1

# Final adjustment based on total valid pairs
if len(valid_pairs) >= 3:
    stability_score *= 2
else:
    stability_score //= 2 if stability_score > 0 else 1

print(f"Result: {stability_score}")