from itertools import combinations

# Simulate sensor data calibration and weighted scoring
raw_readings = [12, 15, 8, 23, 7]
weights = [0.2, 0.4, 0.1, 0.25, 0.05]
dummy_flags = [True, False, True, True, False]

# Irrelevant preprocessing: generate all 2-element combos (not used later)
distractor_combos = list(combinations(raw_readings, 2))
combo_count = len(distractor_combos)

# Misleading normalization step (unused in final logic)
normalized_readings = [x / sum(raw_readings) for x in raw_readings]

# Auxiliary function to filter anomalies based on threshold
def filter_anomalies(data, threshold=10):
    return [x for x in data if x >= threshold]

# Another red herring: bitmask analysis (not actually influencing score)
bit_analysis = []
for val in raw_readings:
    bit_count = bin(val).count('1')
    parity = 'even' if (bit_count % 2) == 0 else 'odd'
    bit_analysis.append((val, bit_count, parity))

# Real processing begins: only high-confidence readings are kept
filtered_data = filter_anomalies(raw_readings)

# Map filtered values to their original indices using enumerate
index_map = {i: raw_readings[i] for i, val in enumerate(raw_readings) if val in filtered_data}

# Compute dynamic adjustment factors (some are unused)
adjustments = []
for idx, val in index_map.items():
    adj = val * weights[idx] * (0.9 if dummy_flags[idx] else 1.1)
    adjustments.append(adj)

# Actual core logic hidden among distractions
def calculate_final_score(data, w):
    score = 0.0
    # Use zip to align filtered data with corresponding weights
    for d, weight in zip(data, w[:len(data)]):
        # Conditional expression determines scaling factor
        factor = 1.5 if d > 10 else 0.8
        score += d * weight * factor
    # Additional adjustment based on count
    penalty = len(data) * 0.2
    return score - penalty

# Final computation — the key statement
final_score = calculate_final_score(filtered_data, weights)

print(f"Result: {final_score}")