import itertools
from collections import namedtuple

def calculate_marker_score(markers):
    if not markers:
        return 0
    # Switch-case simulation using dictionary
    weight_map = {0: 7, 1: 3, 2: 5, 3: 2}
    weighted_xor = 0
    for idx, marker in enumerate(markers):
        weight = weight_map.get(idx % 4, 1)
        weighted_xor ^= (marker << weight) if marker & 1 else (marker >> weight)
    return weighted_xor

# Genetic marker data as named tuples
MarkerSet = namedtuple('MarkerSet', ['patient_id', 'markers'])
marker_data = [
    MarkerSet(101, [23, 45, 67]),
    MarkerSet(102, [12, 34, 56, 78]),
    MarkerSet(103, [91, 28]),
    MarkerSet(104, [15, 22, 33, 44, 55])
]

# Process marker sets with short-circuit evaluation
valid_sets = [mset for mset in marker_data if mset.markers and len(mset.markers) > 1]

# Divide and conquer approach for score calculation
def process_sets(sets):
    if len(sets) <= 1:
        return calculate_marker_score(sets[0].markers) if sets else 0
    mid = len(sets) // 2
    left_score = process_sets(sets[:mid])
    right_score = process_sets(sets[mid:])
    return left_score + right_score

# Calculate cumulative score using set operations for deduplication
unique_patient_ids = set(mset.patient_id for mset in valid_sets)
cumulative_score = process_sets(valid_sets) + (len(unique_patient_ids) * max(unique_patient_ids))

print(f"Result: {cumulative_score}")