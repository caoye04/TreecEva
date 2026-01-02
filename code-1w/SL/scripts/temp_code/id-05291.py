import math

# Irrelevant utility function (decoy)
def normalize_signal(x):
    return [val / max(x) for val in x] if max(x) != 0 else x

# Misleading data preprocessing
temp_readings = [23.1, 24.5, 19.8, 26.7, 22.0, 20.3, 25.4]
offset = sum(temp_readings) / len(temp_readings)
adjusted_temps = [t - offset for t in temp_readings]
scaled_power = [round(t ** 1.5, 2) for t in adjusted_temps]

# Unused but plausible-looking transformation chain
def transform_sequence(seq):
    return [math.sin(x / 10) * 100 for x in seq if x > -5]

transformed = transform_sequence(scaled_power)

# Core system: Biomedical signal integrity analyzer
health_vector = [0.81, 0.93, 0.67, 0.45, 0.88, 0.76, 0.54, 0.91]

# Threshold configuration map (real usage ahead)
threshold_map = {
    'critical': 0.4,
    'warning': 0.65,
    'optimal': 0.85
}

# Distractor: Unused secondary mapping
evaluation_zones = {
    'low': lambda x: x < 0.3,
    'moderate': lambda x: 0.3 <= x < 0.7,
    'high': lambda x: x >= 0.7
}

# Complex processing with red herrings
status_flags = []
alert_count = 0

for idx, reading in enumerate(health_vector):
    # Simulated hysteresis logic (partially irrelevant)
    if reading > 0.9 and idx > 0 and health_vector[idx-1] > 0.85:
        status_flags.append('STABLE_HIGH')
        continue  # early skip - red herring path
    elif reading < 0.5:
        alert_count += 1

    # Real logic embedded here
    if reading >= threshold_map['optimal']:
        status_flags.append('OK')
    elif threshold_map['warning'] <= reading < threshold_map['optimal']:
        status_flags.append('CHECK')
    else:
        status_flags.append('ACTION')

# Unused list comprehension (distractor)
recovery_suggestions = [
    f'Reboot sensor {i}' 
    for i, flag in enumerate(status_flags) 
    if flag == 'ACTION'
]

# Decoy function that's defined but not used
def compute_rollback_point(data, safety_margin=0.1):
    sorted_vals = sorted(data, reverse=True)
    cutoff = sorted_vals[0] - safety_margin
    return len([x for x in data if x >= cutoff])

# Real core logic hidden among noise
def analyze_fragmentation(seq, limit):
    gaps = 0
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > limit:
            gaps += 1
    return gaps

fragmentation_score = analyze_fragmentation(health_vector, 0.2)

# Critical function with layered logic and distractions
def process_metrics(signal, config):
    # Irrelevant pre-checks
    if not signal or len(signal) == 0:
        return -1
    
    # Redundant normalization
    normalized = [x * (1 + 0.01) for x in signal]
    
    # Key metric: compliance ratio
    optimal_threshold = config['optimal']
    compliant_nodes = len([x for x in normalized if x >= optimal_threshold])
    compliance_ratio = compliant_nodes / len(normalized)
    
    # Secondary metric: risk density
    risky_nodes = len([x for x in signal if x < config['warning']])
    risk_density = risky_nodes / len(signal)
    
    # Tertiary: stability continuity
    stable_runs = 0
    current_run = 0
    for val in signal:
        if val >= config['warning']:
            current_run += 1
        else:
            if current_run >= 2:
                stable_runs += current_run
            current_run = 0
    if current_run >= 2:
        stable_runs += current_run
    
    # Final diagnostic calculation - only this matters
    raw_score = (compliance_ratio * 400) + ((1 - risk_density) * 300) + (stable_runs * 5)
    
    # Apply hidden calibration constant (non-obvious)
    calibration_key = len([x for x in set(signal) if x > 0.5])  # set operation
    final_value = raw_score * (calibration_key / 6)
    
    # Dead code branch (misleading)
    if final_value > 1000:
        return math.floor(final_value / 10) * 10
        
    return round(final_value, 4)

# Execute main logic
intermediate_diagnostic = sum(health_vector) / len(health_vector)  # distraction

# This is the key statement
final_diagnostic = process_metrics(health_vector, threshold_map)

# Additional decoy computation
entropy_metric = -sum(p * math.log2(p) for p in [0.25, 0.25, 0.25, 0.25])  # constant

print(f"Target result: {final_diagnostic}")