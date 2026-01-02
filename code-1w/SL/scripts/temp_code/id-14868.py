import math

# Irrelevant sensor constants (distractors)
SENSOR_THRESHOLD_ALPHA = 0.87
SENSOR_NOISE_FLOOR = 0.0034
CALIBRATION_OFFSET_BETA = -0.021

# Real data inputs
time_series = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
raw_signals = {'channel_a': [1.2, 1.5, 0.9, 2.1, 1.8], 'channel_b': [0.8, 1.0, 1.4, 1.6, 2.0]}

# Misleading preprocessing path (dead code - never called)
def legacy_filter(data):
    return [x * 0.95 for x in data if x > 1.0]

def transform_signal(values):
    # Applies logarithmic scaling and squares odd-indexed elements
    transformed = []
    for i, v in enumerate(values):
        base_val = math.log(v + 1)  # Avoid log(0)
        if i % 2 == 1:
            base_val = base_val ** 2
        transformed.append(round(base_val, 4))
    return transformed

def compute_entropy(data_list):
    total = sum(data_list)
    if total == 0:
        return 0.0
    # Normalize and compute Shannon-style entropy
    probabilities = [x / total for x in data_list]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def detect_spike_pattern(seq):
    # Detects rising-falling pattern: up, up, down
    count = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2]:
            count += 1
    return count

def integrate_time_series(times, signal):
    # Numerical integration using trapezoidal rule
    integral = 0.0
    for i in range(1, len(times)):
        dt = times[i] - times[i-1]
        avg_height = (signal[i] + signal[i-1]) / 2
        integral += dt * avg_height
    return round(integral, 4)

def generate_synthetic_noise(level, length):
    # Unused function — red herring
    return [level * (i % 2) for i in range(length)]

# Decoy diagnostic flags (irrelevant)
ANOMALY_FLAG_X1 = False
ANOMALY_FLAG_X2 = True
ANOMALY_FLAG_X3 = False

# Real processing begins here
filtered_a = [x for x in raw_signals['channel_a'] if x >= 1.0]  # Filter noise
filtered_b = list(filter(lambda x: x > 0.9, raw_signals['channel_b']))  # Another filter

# Apply transformation
transformed_a = transform_signal(filtered_a)
transformed_b = transform_signal(filtered_b)

# Compute auxiliary metrics (some irrelevant)
entropy_a = compute_entropy(transformed_a)
entropy_b = compute_entropy([x * 1.1 for x in transformed_b])  # Slight variation, not used later
spike_count_a = detect_spike_pattern(filtered_a)
spike_count_b = detect_spike_pattern(filtered_b)

# Core integration on time series using transformed_a as signal
integral_result = integrate_time_series(time_series[:len(transformed_a)], transformed_a)

# Intermediate diagnostic mix (complex combination)
diagnostic_score = (
    (integral_result * 2.5) + 
    (spike_count_a * 100) + 
    int(sum(transformed_b[:3]) * 10) - 
    int(entropy_a * 10)
)

# Secondary derived values (some misleading)
signal_power = sum(x**2 for x in transformed_a)  # Not directly used
data_density = len(filtered_a) / (max(time_series) - min(time_series))  # Distractor

# Simulated gain adjustment (unused path)
current_gain = 1.0
for _ in range(3):
    current_gain *= 0.95  # Decays but unused

# Data fusion via dictionary aggregation (relevant structure)
fused_metrics = {
    'primary': integral_result,
    'spikes': spike_count_a,
    'entropy': entropy_a,
    'auxiliary': sum(transformed_b) // 1  # Floor sum
}

# Processed data container (key input to final function)
processed_data = [
    fused_metrics['primary'],
    fused_metrics['spikes'] * 50,
    len(transformed_a) * 200,
    int(fused_metrics['auxiliary'] * 2)
]

# Final analysis function
def analyze_signal(metrics):
    base = metrics[0]  # integral_result
    spike_bonus = metrics[1]  # scaled spike count
    length_penalty = metrics[2]  # length-based penalty
    aux_factor = max(metrics[3], 1)  # prevent div by zero
    
    # Complex formula with conditional twist
    if base > 1.0:
        result = (base * aux_factor) + spike_bonus - length_penalty
    else:
        result = (base + spike_bonus) * (length_penalty / aux_factor)
    
    # Additional obfuscation: bit manipulation on float components
    integer_part = int(result)
    fractional_bits = int((result - integer_part) * 10000)
    mixed = (integer_part ^ 12345) & (fractional_bits | 9876)  # Bitwise red herring
    final = integer_part + (mixed % 1)  # Only integer part matters due to truncation
    
    return int(final)  # Deterministic integer output

# Execute key statement
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")