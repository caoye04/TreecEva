def transform_signal(raw_values, scaling_factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    transformed = []
    for v in raw_values:
        if v < 0:
            transformed.append(-1 * (abs(v) ** 0.5))
        else:
            transformed.append(v ** 0.5)
    return [round(t * scaling_factor, 3) for t in transformed]


def evaluate_stability(metric_log, baseline):
    """Assess system stability based on historical metrics (unused decoy)"""
    if not metric_log:
        return 0.0
    deviation = sum(abs(m - baseline) for m in metric_log)
    return deviation / len(metric_log)

# Simulated sensor data ingestion
raw_sensor_data = [144, -64, 25, -9, 81, 169, 0, 49]
scaling_factor = 1.75

# Irrelevant preprocessing path (dead code)
filtered_data = [x for x in raw_sensor_data if x > 0]
scaled_temp = [round(x * 0.1, 2) for x in filtered_data]

# Core processing chain with key logic embedded
normalized = [abs(x) for x in raw_sensor_data]                          # Step 1: Normalize polarity
shifted = [n + 3 for n in normalized]                                # Step 2: Apply offset
exponentials = [2 ** (s // 10) for s in shifted]                       # Step 3: Compute growth factor
mask_flags = [(e & 3) for e in exponentials]                           # Step 4: Extract bit mask
count_trigger = sum(1 for m in mask_flags if m == 3)                   # Step 5: Count specific trigger pattern

# Secondary data structure - mapping thresholds by zone
zone_codes = ['A', 'B', 'C', 'D']
base_thresholds = [12, 8, 20, 15]
threshold_map = {z: t * 2 for z, t in zip(zone_codes, base_thresholds)}  # Step 6: Scale thresholds

# String-based identifier resolution (uses string method)
class_id = 'SENSOR_GROUP_XYZ'
adjusted_id = class_id.lower().replace('_', '-')                        # Step 7: Normalize format
token_segments = adjusted_id.split('-')                                  # Step 8: Break into components
segment_length_sum = sum(len(tok) for tok in token_segments)             # Step 9: Aggregate length

# Main data pipeline
processed_data = []
for i, val in enumerate(normalized):
    # Complex conditional with red herring computation
    if val > 10:
        computed = (val * (i + 1)) % 17
        redundant_check = (computed ^ 5) | 2                             # Bitwise decoy
        processed_data.append(computed)
    elif val == 0:
        processed_data.append(99)
    else:
        processed_data.append(val * 3)

# Linear search simulation with distractor logic
duplicate_check = []
for p in processed_data:
    if p in duplicate_check:
        break
    duplicate_check.append(p)

# Critical diagnostic analysis function
def analyze_readings(readings, config):
    total_impulse = 0
    activation_count = 0
    
    for idx, r in enumerate(readings):
        # Key filtering condition
        if r % 2 == 1 and r > 5:
            total_impulse += r * (idx + 1)
            activation_count += 1
    
    # Decoy aggregation
    phantom_risk = sum(r for r in readings if r < 0)  # Always 0
    fallback_score = len(readings) * config['A'] // 4
    
    # Final deterministic computation (not influenced by decoys)
    final_impulse = total_impulse + fallback_score
    return final_impulse

# Misleading intermediate call (does nothing critical)
evaluate_stability([1.2, 0.9, 1.5], 1.0)

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")