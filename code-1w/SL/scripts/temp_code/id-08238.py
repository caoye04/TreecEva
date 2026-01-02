import math

# Simulated sensor data processing with embedded logic chain
raw_readings = [32.1, 15.7, 22.5, 41.3, 8.9, 54.2, 11.6]
baseline_shift = 17.3
calibration_factor = 0.88
noise_threshold = 10.5

# Irrelevant calibration constants (distractor)
calibration_map = {"a": 0.1, "b": 0.2, "c": 0.3}
scaling_matrix = [[1, 2], [3, 4]]

# Preprocess: normalize and filter
normalized = []
for val in raw_readings:
    adjusted = (val - baseline_shift) * calibration_factor
    if abs(adjusted) > noise_threshold:
        normalized.append(round(adjusted, 2))

# Dead code path: never executed due to condition (red herring)
if len(normalized) < 5:
    fallback_mode = True
    recovery_state = sum(normalized) / len(normalized)
else:
    fallback_mode = False  # This runs, but variables are unused
    recovery_state = None

# Transform via bit manipulation and combinatorics (core logic)
shifted_values = []
for num in normalized:
    integer_part = int(abs(num))
    # Bitwise manipulation for diagnostic signature
    flipped = integer_part ^ 255  # XOR with mask
    shifted = (flipped << 1) & 511  # Left shift and mask
    shifted_values.append(shifted)

# Set operations: detect unique pattern orbits (core logic + python idiom)
value_set = set(shifted_values)
duplicate_check = len(shifted_values) - len(value_set)
signature_pool = {i ** 2 % 100 for i in range(1, 50)}  # Combinatoric residue set
reference_set = value_set.intersection(signature_pool)

# Decoy transformation chain (unused)
temp_sequence = []
for x in value_set:
    temp = (x + 13) * 7 % 1000
    temp_sequence.append(temp)
transform_attempt = sorted(temp_sequence, reverse=True)[::2]

# Real transformation: map to diagnostic space
transformed_data = []
for v in value_set:
    angle_rad = math.radians(v % 90)
    trig_component = math.sin(angle_rad) * 100
    combined = int(trig_component + (v % 10))
    transformed_data.append(combined)

# String-based flag encoding (irrelevant but plausible)
status_flags = ['OK', 'WARN', 'ERR']
flag_summary = "|".join(status_flags).lower().replace("warn", "review")
summary_hash = len(flag_summary) * 1000  # Looks important, unused

# Core analysis function with short-circuit logic
def analyze_patterns(data, ref):
    if not data or not ref:
        return -1
    
    # Multi-step reasoning: statistical moments
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    # Logical combination with set cardinality
    set_influence = len(ref) * 100
    deviation_score = int(std_dev * 10) * 10
    
    # Critical dependency on both statistical spread and set overlap
    if deviation_score > set_influence:
        primary_factor = deviation_score
    else:
        primary_factor = set_influence
    
    # Final computation: weighted diagnostic
    penalty = 0
    for d in data:
        if d > mean_val + std_dev:
            penalty += 1
    
    # Answer derived here
    result = primary_factor - (penalty * 50)
    return result

# Execution point of interest
final_diagnostic = analyze_patterns(transformed_data, reference_set)

# Output requirement
print(f"Result: {final_diagnostic}")