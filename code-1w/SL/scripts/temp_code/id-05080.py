import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_samples = [0.8, 1.2, 3.1, 2.9, 4.0, 5.8, 6.1, 7.9, 8.0, 9.1]
    return [x * 1.05 for x in raw_samples if x > 2.5]

def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= 2 * std_dev]

def generate_checksum(sequence):
    # Irrelevant function - simulates metadata computation
    return sum(i * val for i, val in enumerate(sequence)) % 1000

def encrypt_sequence(seq):
    # Dead path: obfuscation not used in main logic
    return [int((val * 113) % 47) for val in seq]

def decode_signal(signal):
    # Unused decoding logic - red herring
    return [round(math.cos(x) * 100) for x in signal]

def normalize_stream(stream):
    min_val, max_val = min(stream), max(stream)
    if max_val == min_val:
        return [0.0] * len(stream)
    return [(x - min_val) / (max_val - min_val) for x in stream]

def apply_window(signal, window_size=3):
    # Applies moving average - partially relevant but only one result is used
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        segment = signal[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

def transform_signal(raw):
    # Real transformation chain
    filtered = filter_outliers(raw)
    normalized = normalize_stream(filtered)
    windowed = apply_window(normalized, 3)
    # Only last three elements are used downstream
    return windowed[-3:]

def evaluate_stability(pattern):
    # Computes variance-like metric
    mean_p = sum(pattern) / len(pattern)
    return sum((x - mean_p) ** 2 for x in pattern) / len(pattern)

def assess_complexity(seq):
    # Distractor metric - never actually used
    return sum(1 for i in range(1, len(seq)) if seq[i] > seq[i-1])

def derive_entropy(values):
    # Redundant complexity measure
    return -sum(x * math.log(x + 1e-8) for x in values)

def analyze_pattern(seq, cfg):
    base_metric = evaluate_stability(seq)
    
    # Conditional branching with misleading intermediate assignments
    if cfg['mode'] == 'deep':
        adjustment = 0.5 if base_metric > 0.1 else 0.1
        temp_debug = derive_entropy(seq)  # Computed but unused
        extra_weight = assess_complexity(seq)  # Another unused metric
        refined = base_metric * (1 + adjustment)
        
        # Nested condition with decoy variables
        if len(seq) >= 3:
            peak_ratio = seq[-1] / (seq[0] + 1e-5)
            if peak_ratio > 0.8:
                correction = math.sqrt(peak_ratio)
                refined -= correction * 0.05
    else:
        refined = base_metric
    
    # Final computation uses only refined and constant offsets
    final_score = (refined * 1000) + 17
    return int(round(final_score))

# Misleading auxiliary computations
idle_cycles = 127
diagnostic_trace = [encrypt_sequence([1,2,3,4]), decode_signal([0.1, 0.5, 0.9])]
metadata_checksum = generate_checksum([8, 6, 7, 5, 3, 0, 9])

# Configuration with plausible but selectively used fields
config = {
    'mode': 'deep',
    'version': '2.1.0',
    'threshold': 0.5,
    'sampling_rate': 100,
    'debug_mode': False
}

# Main execution flow
sensor_data = collect_readings()
transformed_data = transform_signal(sensor_data)

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, config)

# Print result as required
print(f"Result: {final_diagnostic}")