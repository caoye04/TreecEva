from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant metrics
data_stream = [
    {'temp': 23.5, 'pressure': 101.3, 'vibration': 0.45, 'status': 'active'},
    {'temp': 25.1, 'pressure': 102.0, 'vibration': 0.67, 'status': 'active'},
    {'temp': 22.8, 'pressure': 99.8, 'vibration': 0.33, 'status': 'idle'},
    {'temp': 24.6, 'pressure': 100.9, 'vibration': 0.55, 'status': 'active'},
    {'temp': 26.3, 'pressure': 103.1, 'vibration': 0.78, 'status': 'active'},
    {'temp': 21.9, 'pressure': 98.7, 'vibration': 0.29, 'status': 'idle'}
]

# Irrelevant aggregation - distractor
status_count = defaultdict(int)
for entry in data_stream:
    status_count[entry['status']] += 1

# Noise filter threshold (red herring)
noise_floor = 0.3
filtered_vibrations = [d['vibration'] for d in data_stream if d['vibration'] > noise_floor]

# Compute rolling average of temperature - misleading intermediate
rolling_temp_avg = sum(d['temp'] for d in data_stream) / len(data_stream)

# Bitwise diagnostic check on pressure values (decoy logic)
diagnostic_flags = 0
for d in data_stream:
    scaled_pressure = int(d['pressure'] * 10)
    diagnostic_flags ^= (scaled_pressure & 0xFF)  # XOR into diagnostic register

# Real processing begins: extract performance metric
metric_data = []
for d in data_stream:
    raw_metric = d['temp'] * (d['pressure'] / 100.0)
    adjusted = math.log(raw_metric) if raw_metric > 0 else 0
    metric_data.append(adjusted)

# Auxiliary calculation: vibration-weighted coefficient (unused)
vibration_counter = Counter([round(d['vibration'], 1) for d in data_stream])
vibration_coeff = 0
for v, cnt in vibration_counter.items():
    vibration_coeff += v * cnt * 0.1

# Base threshold derived from logical combination
is_stable = len([d for d in data_stream if d['status'] == 'active']) >= 4
high_vib = any(d['vibration'] > 0.7 for d in data_stream)
base_threshold = 3.15 if is_stable and not high_vib else 2.95

# Decoy function that is never called
def analyze_failure_modes(seq):
    """Unused diagnostic function - dead code path"""
    failures = 0
    for i in range(1, len(seq)):
        if seq[i-1] > seq[i]:
            failures += 1
    return failures if failures > 0 else -1

# Another red herring: complex unpacking and reassignment
temp_vals = [d['temp'] for d in data_stream]
a, b, *rest = temp_vals
b_recalibrated = b * 1.02

# Core evaluation logic with conditional expression and nesting
def evaluate_performance(metrics, threshold):
    if not metrics:
        return 0
    
    cumulative = 0.0
    count = 0
    
    for val in metrics:
        # Nested filtering and transformation
        if val > threshold:
            # Bit manipulation distraction within relevant function
            shifted = int(val * 100)
            masked = shifted & 0xFFFF
            signed = -(masked ^ 0x8000) if (masked & 0x8000) else masked
            
            # Actual contribution uses only simple transform
            contribution = val ** 1.1
            cumulative += contribution
            count += 1
            
            # Early break under rare condition (not triggered)
            if count > 10:
                break
    
    # Final adjustment using logical operations
    override_flag = (count >= 3) and (cumulative > 10.0) or (threshold > 3.0)
    final_value = cumulative * 1.2 if override_flag else cumulative * 0.8
    
    # Additional decoy computation (never used)
    synthetic_peak = max(metrics) * (count // 2 + 1) if count > 0 else 0
    
    return int(final_value)  # Discretize to integer result

# Key execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Distractor: secondary analysis with no effect
outlier_count = 0
for d in data_stream:
    if d['temp'] > rolling_temp_avg + 1.5:
        outlier_count += 1

# Print result as required
print(f"Result: {final_score}")