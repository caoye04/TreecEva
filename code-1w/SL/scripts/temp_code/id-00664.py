import math

# Simulated sensor array data processing for environmental monitoring system
data_stream = [14.2, 18.7, 25.3, 9.8, 22.1, 30.5, 11.9, 16.4, 27.8, 13.6]

# Irrelevant calibration constants (distractors)
calibration_factor_a = 0.87
reference_offset = 273.15
temp_conversion_coeff = [1.02, 0.98, 1.01, 0.99]
baseline_registry = {'sensor_a': 12.5, 'sensor_b': 15.0, 'sensor_c': 17.5}

# Real processing parameters
effective_threshold = 15.0
drift_compensation = lambda x: x * 1.05 if x < 20.0 else x * 0.98

# Simulated timestamp alignment (unused but plausible)
timestamps = [1634567890 + i*30 for i in range(len(data_stream))]
normalized_times = [t % 3600 for t in timestamps]

# Data transformation pipeline
def apply_filter(raw_values, method='moving_avg', window=2):
    if method == 'moving_avg':
        filtered = []
        for i in range(len(raw_values)):
            start = max(0, i - window + 1)
            filtered.append(sum(raw_values[start:i+1]) / (i - start + 1))
        return filtered
    elif method == 'exponential':
        # Dead code path — never used
        alpha = 0.3
        result = [raw_values[0]]
        for val in raw_values[1:]:
            result.append(alpha * val + (1 - alpha) * result[-1])
        return result
    return raw_values

# Irrelevant signal decomposition (decoy function)
def decompose_signal(signal):
    amplitude = max(signal) - min(signal)
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val)**2 for x in signal) / len(signal)
    return {'amplitude': amplitude, 'mean': mean_val, 'variance': variance}

# Unused frequency analysis
signal_stats = decompose_signal(data_stream)
frequency_bins = [0.1, 0.5, 1.0, 2.0]
harmonic_pattern = [math.sin(f * 3.14) for f in frequency_bins]

# Actual filtering with distraction
processed_readings = apply_filter(data_stream, method='moving_avg')

# Secondary adjustment using lambda (relevant)
adjusted_readings = list(map(drift_compensation, processed_readings))

# Filtering logic with misleading comparisons
high_alert_zone = [x for x in adjusted_readings if x > 25.0]
low_operational_band = [x for x in adjusted_readings if x < 12.0]

# Real working subset
filtered_data = [x for x in adjusted_readings if x >= effective_threshold]

# Complex condition function with red herring components
def generate_threshold_function(base_limit):
    security_override = False  # Unused control flag
    audit_log = []  # Dead storage
    
    def check_tolerance(x):
        # Mixed logic with irrelevant branches
        if x > base_limit * 1.2:
            category = 'critical'
            risk_score = 9.7
        elif x > base_limit * 1.1:
            category = 'elevated'
            risk_score = 6.4
        else:
            category = 'normal'
            risk_score = 2.1  # This path is taken by most values
            
        # Distractor computation
        normalized_risk = risk_score / 10.0
        confidence_weight = math.log(2 + normalized_risk)
        
        return x >= base_limit  # Only this matters
    
    return check_tolerance

threshold_func = generate_threshold_function(effective_threshold)

# Decoy statistical summary (never used)
summary_stats = {
    'count': len(adjusted_readings),
    'mean': sum(adjusted_readings) / len(adjusted_readings),
    'std_dev': math.sqrt(sum((x - sum(adjusted_readings)/len(adjusted_readings))**2 for x in adjusted_readings) / len(adjusted_readings)),
    'median': sorted(adjusted_readings)[len(adjusted_readings)//2]
}

# Core diagnostic processor
memoization_cache = {}  # Unused caching layer

# Actual final computation
final_diagnostic = 0
for reading in filtered_data:
    # Apply bit manipulation as part of checksum (real usage)
    int_component = int(reading * 10)  # Scale to avoid decimals
    checksum = int_component ^ 0xAAAA  # XOR with fixed pattern
    checksum = (checksum >> 2) & 0x3FFF  # Shift and mask
    final_diagnostic += checksum

# Additional irrelevant aggregation
collision_count = 0
seen = {}
for val in filtered_data:
    key = int(val * 100)
    if key in seen:
        collision_count += 1
    seen[key] = True

# Output the actual answer
print(f"Result: {final_diagnostic}")