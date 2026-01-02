from itertools import combinations

# Simulate sensor data calibration and anomaly detection
raw_readings = [127, 255, 193, 64, 96, 150]
base_threshold = 100
calibration_factor = 0.75

# Irrelevant transformation (distractor)
distorted_readings = [x ^ 42 for x in raw_readings if x > 50]

# Extract features with meaningful and misleading computations
strong_signals = [x for x in raw_readings if x > base_threshold]
weak_signals = [x for x in raw_readings if x <= base_threshold]

# Misleading energy calculation (not used in final result)
total_energy = sum([x * calibration_factor for x in raw_readings])
adjusted_energy = total_energy * 1.23

# Signal pairing logic using itertools to generate candidate pairs
pair_candidates = list(combinations(strong_signals, 2))
pair_scores = []

for pair in pair_candidates:
    a, b = pair
    # Real computation: harmonic interaction score
    if a != b:
        score = (a * b) / (a + b)  # Harmonic mean component
        penalty = (a ^ b) & 0xFF  # Bitwise penalty based on XOR
        normalized_score = (score - penalty) * calibration_factor
        pair_scores.append(normalized_score)

# Secondary distractor: simulate unused noise profile
noise_floor = sum([x << 1 for x in weak_signals]) % 255
baseline_drift = lambda x: x ** 0.5 if x > 10 else 0
unused_correction = [baseline_drift(x) for x in raw_readings]

# Aggregation logic with red herring variables
raw_aggregate = sum(pair_scores)
scaling_constant = len(strong_signals) or 1
intermediate_metric = raw_aggregate / scaling_constant if scaling_constant > 0 else 0

# Final processing with conditional adjustment
processed_data = intermediate_metric + (len(pair_candidates) * 10)

def calculate_final_score(data):
    # Simulated multi-stage scoring
    stage1 = int(data)
    stage2 = stage1 ^ 255  # Obfuscation step
    stage3 = (stage2 + (stage2 >> 4)) & 0xFFFF
    return abs(stage3 - 1000)  # Deterministic final transformation

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")