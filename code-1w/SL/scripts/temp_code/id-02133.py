import itertools

# Simulated sensor array diagnostics with noise filtering and calibration
raw_readings = [18, 22, 15, 30, 12, 27, 19, 24, 16, 21, 14, 26]
noise_floor = 13
calibration_map = {i: val ** 0.5 for i, val in enumerate([x * 1.5 for x in range(12)])}
baseline_offset = sum(calibration_map[i] for i in range(0, 12, 3)) / 4

# Irrelevant auxiliary computation - dead path (simulates temperature drift compensation not used)
temperature_drift = [0.1 * i - 0.05 * (i ** 1.1) for i in range(10)]
compensated_drift = list(map(lambda x: x * 1.2 if x > 0 else x * 0.8, temperature_drift))
unused_checksum = sum(compensated_drift) * 1000 % 97

# Real data path begins: filter out low-amplitude noise
filtered_data = [reading for reading in raw_readings if reading > noise_floor]

# Misleading intermediate transformation (appears important but unused in final result)
shadow_copy = [x - 10 for x in filtered_data if x % 2 == 0]
phantom_aggregate = sum(shadow_copy) // len(shadow_copy) if shadow_copy else 0

# Use of enumerate and zip to align readings with dynamic weights
weights = [(i + 1) * 0.9 for i in range(len(filtered_data))]
weighted_pairs = list(zip(filtered_data, weights, enumerate(filtered_data)))

dynamic_factor = 0.0
for val, w, (idx, original) in weighted_pairs:
    if idx % 2 == 0:
        dynamic_factor += w * (val / (original + 1)) * calibration_map.get(idx, 1.0)
    else:
        dynamic_factor -= w * 0.1

# Conditional expression based adjustment (relevant only if threshold met)
adjustment = 2.5 if dynamic_factor > 5.0 else 1.8

# Auxiliary function that appears critical but is only partially used
def compute_health_score(data, offset):
    base_score = sum(d ** 0.8 for d in data) / len(data)
    penalty = 0
    for i, val in enumerate(data):
        if val < offset * 1.2:
            penalty += 0.3
    return base_score - penalty

# Decoy function call with misleading name
placeholder_result = compute_health_score(raw_readings, baseline_offset)

# Actual aggregation logic using itertools.chain and conditional scaling
expanded_data = list(itertools.chain.from_iterable(
    [[x] * 2 if x > 22 else [x] for x in filtered_data]
))

scaling_factor = adjustment if len(expanded_data) > 10 else 0.9
interim_total = sum(x * scaling_factor for x in expanded_data)

# Final diagnostic depends on scaled total, baseline offset, and dynamic factor
final_diagnostic = int((interim_total - baseline_offset * 3.1) // (dynamic_factor + 1))

# Distractor: complex-looking but irrelevant bitwise manipulation
obfuscation_key = 0
for i in range(8):
    obfuscation_key ^= (i * 23 + 7) & 15
obfuscation_key = (obfuscation_key << 2) | (obfuscation_key >> 2)

# Output the required result
print(f"Result: {final_diagnostic}")