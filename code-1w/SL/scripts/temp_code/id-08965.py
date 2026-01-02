import math

# Simulated sensor fusion module for aerospace telemetry
def analyze_vibration_patterns(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    spectrum = [abs(x) ** 2 for x in filtered]
    return sum(spectrum) / len(spectrum) if spectrum else 0.0

# Legacy calibration function (partially deprecated)
def apply_legacy_compensation(data, factor=0.93):
    compensated = []
    for val in data:
        compensated.append(val * factor if val > 0 else val / factor)
    return compensated

# Core health assessment engine
def generate_health_signature(telemetry_stream):
    base_magnitude = sum(abs(x) for x in telemetry_stream) / len(telemetry_stream)
    
    # Irrelevant secondary processing (distractor)
    outlier_count = 0
    temp_buffer = []
    for reading in telemetry_stream:
        if abs(reading - base_magnitude) > 2 * base_magnitude:
            outlier_count += 1
            temp_buffer.append(reading * 0.1)
    
    # Meaningful computation path
    squared_energy = sum(x * x for x in telemetry_stream)
    normalized_rms = math.sqrt(squared_energy / len(telemetry_stream))
    
    # Destructuring assignment (relevant)
    peak, trough = max(telemetry_stream), min(telemetry_stream)
    dynamic_range = peak - trough
    
    # Bit manipulation for status encoding (relevant)
    status_flags = 0
    if normalized_rms > 1.5:
        status_flags |= (1 << 3)
    if dynamic_range < 0.5:
        status_flags |= (1 << 1)
    
    # Tuple unpacking with lambda transformation (required feature)
    transform = lambda a, b: round((a + b) * 0.75, 3)
    adjusted_pair = transform(peak, normalized_rms)
    
    # Dead code path - never accessed due to logic (distractor)
    debug_snapshot = None
    if False and len(temp_buffer) > 5:
        debug_snapshot = {"buffer": temp_buffer.copy(), "outliers": outlier_count}
    
    # Composite diagnostic vector
    return (base_magnitude, normalized_rms, dynamic_range, status_flags, adjusted_pair)

# System load processor with red herring computations
def calculate_system_load(intensity_vector, mode='active'):
    # Irrelevant pre-processing
    scaling_map = {'low': 0.8, 'medium': 1.0, 'high': 1.4, 'critical': 2.0}
    scale = scaling_map.get(mode, 1.0)
    
    # Real computation
    load_score = sum(x ** 1.8 for x in intensity_vector) * scale
    
    # Decoy metrics (never used)
    entropy_proxy = 0.0
    for x in intensity_vector:
        if x > 0:
            entropy_proxy -= x * math.log(x + 1e-8)
    temporal_variance = sum((intensity_vector[i+1] - intensity_vector[i])**2 
                           for i in range(len(intensity_vector)-1))
    
    # Unused set operations (distractor)
    unique_contributions = set()
    for idx, val in enumerate(intensity_vector):
        if idx % 3 == 0:
            unique_contributions.add(round(val * 1.1, 2))
    
    return int(load_score)

# Main diagnostic orchestrator
def process_metrics(signature, load):
    base_level, rms, span, flags, pairing = signature
    
    # Multi-concept reasoning chain
    risk_numerator = rms * (span + 0.1)
    risk_denominator = base_level + (load / 1000.0)
    preliminary_index = risk_numerator / risk_denominator
    
    # Conditional bit analysis (relevant)
    instability_indicated = bool(flags & (1 << 3))
    restricted_dynamics = bool(flags & (1 << 1))
    
    # Complex adjustment logic with early exit (distractor branch)
    if restricted_dynamics and load < 50:
        return round(preliminary_index * 0.3, 4)  # Early return never taken
    
    # Actual execution path
    adjustment_curve = lambda x: 1.8 - (1.0 / (1 + math.exp(-x / 10)))
    nonlinear_factor = adjustment_curve(load)
    
    # Final composition with tuple-based dispatch
    modifiers = {
        (True, True): 2.1,
        (True, False): 1.8,
        (False, True): 1.3,
        (False, False): 1.0
    }
    context_multiplier = modifiers[(instability_indicated, restricted_dynamics)]
    
    final_score = preliminary_index * nonlinear_factor * context_multiplier
    
    # Dead code - misleading post-processing
    if final_score > 100:
        saturation_log = []
        for _ in range(5):
            saturation_log.append("OVERFLOW_GUARD")
    
    return round(final_score, 4)

# Simulated input data
sensor_data = [0.12, -0.34, 0.56, 0.23, -0.45, 0.67, 0.18, -0.22]
vibration_profile = analyze_vibration_patterns(sensor_data)

# Apply irrelevant compensation (result not used)
calibrated_input = apply_legacy_compensation(sensor_data, 0.88)

# Generate core health signature
health_signature = generate_health_signature(sensor_data)

# System load parameters (mix of relevant and irrelevant)
operational_loads = [2.1, 3.3, 1.9, 4.2, 2.8]
system_load = calculate_system_load(operational_loads, mode='high')

# Critical statement containing the answer
temp_diagnostic = process_metrics(health_signature, system_load + 10)
final_diagnostic = process_metrics(health_signature, system_load)

print(f"Result: {final_diagnostic}")