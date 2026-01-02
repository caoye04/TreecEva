from collections import defaultdict, Counter
from itertools import combinations, cycle
import math

# Simulated sensor data processing with embedded logic chain
def analyze_readings(raw_data):
    readings = [x for x in raw_data if x > 0]
    filtered = list(filter(lambda x: x % 2 == 1, readings))

    # Irrelevant transformation (distractor)
    squared_map = {i: val**2 for i, val in enumerate(readings)}
    temp_offset = sum(squared_map.values()) // max(len(squared_map), 1)

    # Core logic begins: frequency analysis
    freq = Counter(filtered)
    mode_val = freq.most_common(1)[0][1] if filtered else 0

    # Bit manipulation layer (relevant)
    bit_signal = 0
    for val in filtered:
        bit_signal ^= val & 0xF
        bit_signal = (bit_signal << 1) % 256

    # Set-based anomaly detection (distractor)
    expected_range = set(range(1, 100))
    observed_set = set(filtered)
    anomalies = observed_set - expected_range
    anomaly_penalty = len(anomalies) * 10

    # Red herring: unused recursive function
    def traverse_tree(depth, acc):
        if depth <= 0:
            return acc
        return traverse_tree(depth - 1, acc * 2)

    # Data restructuring (partially relevant)
    grouped = defaultdict(list)
    for idx, val in enumerate(filtered):
        grouped[idx % 4].append(val)

    # Spurious statistical calculation
    mean_fake = sum(grouped[1]) / len(grouped[1]) if grouped[1] else 0
    variance_echo = sum((x - mean_fake)**2 for x in grouped[1]) if grouped[1] else 0

    # Critical path: combinatorial consistency check
    valid_pairs = 0
    for a, b in combinations(filtered, 2):
        if (a + b) % 7 == 0 and a != b:
            valid_pairs += 1

    # Decoy loop with no side effects
    buffer_cache = []
    for _ in range(3):
        buffer_cache.extend([temp_offset] * 2)
        temp_offset -= 1  # misleading mutation

    # Primary diagnostic score
    aggregate_score = mode_val * 13 + valid_pairs * 7

    # Correction factor derived from bit_signal and frequency spread
    spread = len(freq)
    correction_factor = bit_signal - spread

    # Dead code path (never executed)
    if False:
        backup_system = math.log(aggregate_score + 1)
        aggregate_score += int(backup_system)

    # Key assignment - answer depends on this
    final_diagnostic = aggregate_score + correction_factor

    # Unrelated print for obfuscation
    print(f"Processing complete. Cache size: {len(buffer_cache)}")

    return final_diagnostic

# Input data with engineered properties
input_stream = [23, 45, 67, 23, 89, 21, 45, 23, 12, 14, 16, 91, 23]

# Execution entry point
result = analyze_readings(input_stream)
print(f"Result: {result}")