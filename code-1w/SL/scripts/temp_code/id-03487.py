def analyze_signal(pattern):
    if len(pattern) < 5:
        return sum(pattern) * 2
    else:
        transformed = [p ^ 3 for p in pattern if p % 2 == 1]
        return sum(transformed) + len(pattern)

# Irrelevant signal processing branch (dead path)
def deprecated_analysis(seq):
    return [s << 2 for s in seq]

# Sensor simulation constants (distractors)
CALIBRATION_OFFSET = 0.87
TEMPORAL_DAMPING = 0.91
REFERENCE_AMPLITUDE = 127

# Simulated raw sensor inputs (mixed data types)
sensor_a = [12, 7, 3, 8, 1, 4]
sensor_b = [5, 9, 2, 6, 11]
sensor_c = [4, 4, 4, 4]  # Uniform noise profile

# Misleading aggregation (unused)
avg_a = sum(sensor_a) / len(sensor_a) if sensor_a else 0
avg_b = sum(sensor_b) / len(sensor_b) if sensor_b else 0
composite_index = (avg_a * 0.6) + (avg_b * 0.4)

# Primary diagnostic chain
baseline_readings = {1, 3, 4, 7, 8}  # Normal state fingerprint
activation_sequence = [x * 2 for x in sensor_a if x > 5]
decay_filter = [y // 3 for y in sensor_b]

# Signal fusion with set operations
core_peaks = {x for x in activation_sequence if x in baseline_readings}
background_noise = {y for y in decay_filter} | {0, 1, 2}
health_signature = core_peaks - background_noise

# Red herring: unused transformation tree
transformed_noise = []
for val in background_noise:
    temp_val = val
    temp_val ^= 7
    temp_val += 5
    temp_val &= REFERENCE_AMPLITUDE
    transformed_noise.append(temp_val)

# Decoy function call (no side effects)
deprecated_analysis(transformed_noise)

# Real processing path
def process_metrics(peaks, baseline):
    if not peaks:
        return -999
    
    base_score = 0
    for p in peaks:
        if p in baseline:
            base_score += p ** 2
    
    # Additional logic layer
    adjustment_factor = len(baseline) - len(peaks)
    intermediate = base_score >> adjustment_factor if adjustment_factor >= 0 else base_score << abs(adjustment_factor)
    
    # Final nonlinear correction
    if intermediate > 100:
        intermediate = int(intermediate * 0.75)
    elif intermediate < 10:
        intermediate += 25
        
    return intermediate + 13

# Execution point of interest
final_diagnostic = process_metrics(health_signature, baseline_readings)

# Output result as required
print(f"Result: {final_diagnostic}")