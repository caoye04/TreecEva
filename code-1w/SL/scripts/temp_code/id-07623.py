def analyze_signal(pattern, threshold=0.65):
    """Irrelevant signal analysis function (dead code path)."""
    return [p * 1.05 for p in pattern if p > threshold]

# Misleading intermediate variables
dummy_buffer = [0.1, 0.3, 0.4]
synthetic_peak = max(dummy_buffer) * 120
temp_offset = sum([synthetic_peak / 3 for _ in range(2)])

# Real data: Sensor readings over time (simulated)
readings = [0.88, 0.91, 0.85, 0.94, 0.90, 0.87, 0.95, 0.89]

# Auxiliary transformation map (partly used)
factor_map = {i: val ** 0.5 for i, val in enumerate(readings)}

# Decoy statistical calculation (distractor)
rolling_avg = sum(readings[i:i+3]) / 3 for i in range(len(readings)-2)]
avg_variance = sum((x - 0.9) ** 2 for x in rolling_avg) / len(rolling_avg)

# Core health signature generation (uses slicing and zip)
indices = list(range(len(readings)))
segments = readings[1:6]  # Slice of interest
paired_data = list(zip(segments, indices[1:6]))

# Apply lambda-based transformation
transform_fn = lambda x, idx: round(x * (idx + 1) * 10, 2)
scaled_values = [transform_fn(val, i) for val, i in paired_data]

# Secondary filter using enumerate and conditional logic
filtered_weights = []
for i, w in enumerate(scaled_values):
    if i % 2 == 0:
        adjusted = w * 1.1
    else:
        adjusted = w * 0.95
    filtered_weights.append(round(adjusted, 2))

# Simulate diagnostic signature with min/max logic
extreme_bias = max(filtered_weights) - min(filtered_weights)
baseline_shift = sum(filtered_weights[:3]) / 3

# Critical health signature vector
health_signature = [
    round(baseline_shift, 2),
    round(extreme_bias, 2),
    len([v for v in readings if v >= 0.9])
]

# Unused but plausible decoy function
def compute_stability_index(seq):
    return sum(abs(seq[i] - seq[i-1]) for i in range(1, len(seq)))

# Core processing function (actually used)
def process_metrics(signature, raw):
    a, b, c = signature
    # Composite logic with arithmetic and control flow
    if a > 50:
        multiplier = 1.2
    elif b < 40:
        multiplier = 0.8
    else:
        multiplier = 1.0  # Correct path taken
    
    # Additional logic with bit manipulation red herring
    flag_check = (c << 2) ^ 3  # Computed but not impactful
    dummy_flag = flag_check & 0xFF
    
    # Mean of specific subset using slicing
    subset = raw[-4:]
    local_mean = sum(subset) / len(subset)
    
    # Final composite calculation
    contribution = a * 0.3 + b * 0.4 + (local_mean * 100) * 0.3
    adjusted_contribution = contribution * multiplier
    
    # Final diagnostic score
    result = round(adjusted_contribution - 15.7, 2)
    
    # Dead code branch (never reached)
    if dummy_flag < 0:
        result += 1000
        
    return int(result)

# Execution point of interest
final_diagnostic = process_metrics(health_signature, readings)
print(f"Result: {final_diagnostic}")