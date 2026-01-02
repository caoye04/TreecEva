from itertools import compress, cycle
import math

# Simulated sensor array data (real values)
sensor_ids = [101, 102, 103, 104, 105, 106, 107, 108]
base_readings = [23.4, 19.1, 45.6, 31.8, 37.2, 29.5, 41.0, 33.3]
status_flags = [True, False, True, True, False, True, True, False]

def analyze_stability(value, index):
    """Irrelevant stability heuristic (distractor)"""
    adjusted = value * (1 + math.sin(index))
    return adjusted > 25

# Irrelevant transformation pipeline
stability_mask = [analyze_stability(v, i) for i, v in enumerate(base_readings)]
decoys = list(compress(base_readings, stability_mask))  # Unused later

# Real processing begins: filter by status and threshold
active_readings = [v for i, v in enumerate(base_readings) if status_flags[i]]
temp_offset = sum([abs(x - 30.0) for x in base_readings]) / len(base_readings)  # Distractor calc

# Threshold map generation (mix of logic and arithmetic)
threshold_map = {}
for sid in sensor_ids:
    if sid % 2 == 0:
        threshold_map[sid] = 30.5 + (sid % 7)
    else:
        threshold_map[sid] = 28.0 - (sid % 5)

# Mapping sensor ID to reading (only active ones)
assigned_pairs = list(zip(sensor_ids, base_readings))
filtered_pairs = [pair for pair in assigned_pairs if pair[0] % 3 != 0]  # Remove sensors divisible by 3

# Extract cleaned data
filtered_data = [p[1] for p in filtered_pairs]

# Decoy function with early return (dead path)
def validate_integrity(data):
    if len(data) < 5:
        return False
    checksum = sum(data)
    if checksum < 100:
        return False
    return True  # Never used

# Real processing function
def process_readings(data, thresholds):
    # Create rotating weight pattern using itertools.cycle
    weights = [w / 10.0 for w in cycle([7, 5, 9])]
    weighted_sum = 0.0
    temp_cache = []  # Unused accumulator (distractor)

    for i, val in enumerate(data):
        # Apply dynamic threshold adjustment
        adj_threshold = thresholds.get(sensor_ids[i % len(sensor_ids)], 30.0)
        if val > adj_threshold:
            # Bitwise manipulation for 'encoding' (red herring)
            encoded = int(val * 10) ^ 0xFF
            decoded = (encoded ^ 0xFF) / 10.0
            temp_cache.append(decoded)  # Collected but unused
            weighted_sum += val * next(weights)
        elif val < 25.0:
            weighted_sum += val * 0.5
        else:
            weighted_sum += val * 0.8
    
    # Final nonlinear transformation
    raw_result = weighted_sum * (1.0 + 0.01 * temp_offset)
    final_score = int(raw_result) & 0xFFFF  # Mask to simulate truncation
    
    # Critical computation: XOR folding
    folded = final_score
    while folded > 1000:
        high_part = folded >> 8
        low_part = folded & 0xFF
        folded = high_part ^ low_part
    
    return folded

# Execute main logic
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")