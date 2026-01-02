from itertools import combinations
from typing import Set, Tuple

def analyze_overlaps(zones_a: Set[int], zones_b: Set[int], zones_c: Set[int]) -> int:
    # Irrelevant computation: count pairwise disjointness (not used in final result)
    disjoint_pairs = 0
    if zones_a.isdisjoint(zones_b):
        disjoint_pairs += 1
    if zones_b.isdisjoint(zones_c):
        disjoint_pairs += 1
    if zones_a.isdisjoint(zones_c):
        disjoint_pairs += 1

    # Semi-relevant: generate all possible zone triplets (some distraction)
    all_triplets: Set[Tuple[int, int, int]] = set(combinations(range(1, 8), 3))
    valid_triplets = {t for t in all_triplets if sum(t) % 3 == 0}  # unused filtering

    # Core logic: compute union intersections
    ab_overlap = len(zones_a & zones_b)
    bc_overlap = len(zones_b & zones_c)
    ac_overlap = len(zones_a & zones_c)
    total_unique = len(zones_a | zones_b | zones_c)

    # Distractor: simulate load with dummy accumulation
    temp_sum = 0
    for i in range(len(zones_a)):
        for j in range(i + 1, len(zones_a)):
            temp_sum += i * j  # irrelevant to final score

    # Weighted contribution (only this part matters)
    overlap_score = ab_overlap * 2 + bc_overlap * 3 + ac_overlap * 2
    coverage_bonus = 10 if total_unique >= 10 else 5
    return overlap_score + coverage_bonus


def calculate_final_score(config: dict) -> int:
    # Extract zone sets from config
    primary_zones = set(config['primary'])
    secondary_zones = set(config['secondary'])
    tertiary_zones = set(config['tertiary'])

    # Dead code path: never executed due to condition
    if len(primary_zones) > 100:
        fallback = sum(primary_zones) // len(primary_zones)
        return fallback

    # Calculate auxiliary metrics (some are distractions)
    avg_zone_size = (len(primary_zones) + len(secondary_zones) + len(tertiary_zones)) / 3
    max_zone_id = max(max(primary_zones), max(secondary_zones), max(tertiary_zones))

    # Main analysis call
    base_analysis = analyze_overlaps(primary_zones, secondary_zones, tertiary_zones)

    # Additional distractor: string manipulation unrelated to logic
    status_tag = ''.join([chr(97 + (i % 26)) for i in range(10)])[:8]

    # Final scoring formula
    penalty = 0
    if len(primary_zones & secondary_zones & tertiary_zones) == 0:
        penalty = 7

    final_value = base_analysis - penalty

    return final_value

# Simulation data
config_data = {
    'primary': [1, 3, 4, 6, 7, 9, 10, 12],
    'secondary': [2, 3, 5, 6, 8, 9, 11, 12],
    'tertiary': [3, 4, 5, 6, 7, 11, 12, 13]
}

# Execute main calculation
final_score = calculate_final_score(config_data)
print(f"Result: {final_score}")