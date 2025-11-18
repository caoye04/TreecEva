from dataclasses import dataclass
from typing import List, Set
import bisect

def find_matches_in_sorted_array(arr: List[int], targets: Set[int]) -> int:
    count = 0
    for target in targets:
        index = bisect.bisect_left(arr, target)
        if index < len(arr) and arr[index] == target:
            count += 1
    return count

@dataclass
class GenomicSample:
    sample_id: str
    markers: List[int]

# Initialize genomic samples
sample_a = GenomicSample("HG001", [12, 28, 35, 44, 56, 67, 73, 89, 95, 102])
sample_b = GenomicSample("HG002", [15, 22, 35, 41, 55, 67, 78, 82, 99, 110])
sample_c = GenomicSample("HG003", [10, 28, 33, 44, 59, 66, 73, 85, 92, 105])

# Define signature patterns
signature_pattern_1 = frozenset([28, 44, 73])
signature_pattern_2 = frozenset([35, 67])
signature_pattern_3 = frozenset([12, 95, 102])

# Combine all patterns
all_patterns = [signature_pattern_1, signature_pattern_2, signature_pattern_3]

# Analysis pipeline
matched_signature_count = 0
for pattern in all_patterns:
    # Check if pattern exists in any sample
    found_in_any_sample = False
    for sample in [sample_a, sample_b, sample_c]:
        if find_matches_in_sorted_array(sample.markers, pattern) == len(pattern):
            found_in_any_sample = True
            break
    if found_in_any_sample:
        matched_signature_count += 1

print(f"Result: {matched_signature_count}")