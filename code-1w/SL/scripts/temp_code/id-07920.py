import math

# Simulated sensor array diagnostics with interference

def collect_diagnostics(raw_readings, bias_factor=1.05):
    readings_log = []
    temp_accum = 0
    for val in raw_readings:
        if val > 50:
            temp_accum += math.log(val) * bias_factor
        elif val < 10:
            temp_accum -= math.sqrt(abs(val))
        else:
            temp_accum += val * 0.1
    readings_log.append(temp_accum)
    return readings_log

# Irrelevant function: dead code path (decoy)
def legacy_compatibility_mode(data):
    checksum = 0
    for item in data:
        checksum ^= int(item * 3.14) % 256
    return checksum == 127

# Another decoy: complex but unused transformation
def spectral_decompose(signal):
    transformed = []
    for i, x in enumerate(signal):
        phase = math.sin(i * 0.5) + math.cos(x * 0.1)
        magnitude = abs(x) ** 0.5 * phase
        transformed.append(magnitude if magnitude > 0.1 else 0)
    return [sum(transformed[i:i+3]) for i in range(0, len(transformed), 3)]

# Real processing chain begins here
raw_sensor_data = [85, 12, 67, 5, 23, 91, 44, 3, 77]

# Step 1: Normalize data using modular arithmetic and scaling
normalized = [(x % 17) * 1.8 + 2.1 for x in raw_sensor_data]

# Step 2: Filter based on dynamic criteria
filtered_data = [x for x in normalized if x > 15 and x < 80]

# Step 3: Apply conditional transformation using lambda
transform_fn = lambda z: z * 1.5 if z < 30 else (z * 0.9 if z > 50 else z)
processed_data = [transform_fn(x) for x in filtered_data]

# Decoy dictionary with misleading metrics
system_state = {
    "voltage_stability": sum(math.cos(x) for x in raw_sensor_data) / len(raw_sensor_data),
    "phase_coherence": math.atan2(sum(normalized), len(normalized)),
    "legacy_flag": False,
    "spurious_alerts": [x for x in processed_data if 40 < x < 42]
}

# Threshold logic map – actually used
threshold_map = {
    'low': 25,
    'optimal': 45,
    'high': 60,
    'critical': 75
}

# Core analysis function with embedded logic
def analyze_readings(readings, thresholds):
    # Distractor: initialize many intermediate variables
    avg = sum(readings) / len(readings)
    peak = max(readings)
    noise_floor = min(readings) * 0.5
    fluctuation_index = (peak - noise_floor) / avg
    
    # Real decision logic (nested conditions)
    rating = 0
    if avg < thresholds['low']:
        rating += 10
    elif avg < thresholds['optimal']:
        rating += 25
    else:
        rating += 40
    
    if peak > thresholds['high']:
        if fluctuation_index > 1.3:
            rating += 17
        else:
            rating += 8
    
    if len(readings) > 5:
        # Additional check using set uniqueness (distractor use of sets)
        unique_bands = len(set(int(r // 10) for r in readings))
        if unique_bands >= 4:
            rating += 6
    
    # Final adjustment using bit manipulation (real usage)
    # Only lower 6 bits matter, apply XOR mask to stabilize
    final_rating = (rating ^ 0b101010) & 0b111111
    
    # Distractor: unused complex expression
    diagnostic_entropy = -sum((r / avg) * math.log(r / avg) for r in readings if r > 0)
    
    return final_rating

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")