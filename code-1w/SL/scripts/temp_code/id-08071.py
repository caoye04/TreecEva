import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3, 7, 12, 15, 21, 24, 30, 35]
offset_threshold = 18
scaling_factor = 0.75

def apply_filter(sequence, method='lowpass'):
    """Irrelevant filtering function (distractor)"""
    return [x for x in sequence if x % 2 == 1]

def compute_entropy(data):
    """Dead-end computation: calculates entropy but unused later"""
    total = sum(data)
    probs = [v / total for v in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Irrelevant transformation chain (red herring)
filtered_data = apply_filter(raw_readings)
entropy_value = compute_entropy(filtered_data)
adjusted_readings = [x * scaling_factor for x in raw_readings]

# Core data transformation pipeline
transformation_shift = 5
effective_weights = list(map(lambda x: (x + transformation_shift) ** 0.5, adjusted_readings))

# Mask generation based on threshold (partially relevant but misleading intermediate)
mask_flags = [int(x >= offset_threshold * scaling_factor) for x in raw_readings]

# Real signal extraction (hidden in noise of other operations)
signal_peaks = []
for i, val in enumerate(adjusted_readings):
    if i > 0 and i < len(adjusted_readings) - 1:
        if adjusted_readings[i-1] < val > adjusted_readings[i+1]:
            signal_peaks.append(val)

# Decoy statistical summary (unused)
mean_peak = sum(signal_peaks) / len(signal_peaks) if signal_peaks else 0
deviation_score = sum(abs(p - mean_peak) for p in signal_peaks)

# Actual critical transformation
transformed_data = []
for x in effective_weights:
    transformed_data.append(int(x * 10) % 7)

# Configuration object with distracting fields
config = {
    'version': '2.1',
    'active': True,
    'thresholds': {'low': 2, 'high': 5},
    'mode': 'diagnostic',
    'debug_trace': deviation_score,  # Misleading assignment
    'window_size': len(raw_readings)//2
}

# Diagnostic engine that appears complex but relies on simple logic
status_codes = {0: 'OK', 1: 'WARN', 2: 'FAIL'}

def analyze_pattern(seq, cfg):
    count_zeros = seq.count(0)
    count_sixes = seq.count(6)
    rolling_sum = sum(seq[i] * seq[i+1] for i in range(len(seq)-1) if seq[i] != 0)
    
    # Dead code branch due to condition always false in this context
    if cfg.get('validate_checksum', False):
        checksum = sum(seq)
        return checksum % 100
    
    # Actual decision logic (well-hidden among distractions)
    if count_sixes > count_zeros:
        base_score = 420
    else:
        base_score = 210
    
    adjustment = (rolling_sum % 13) - 6
    return base_score + adjustment

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, config)

print(f"Result: {final_diagnostic}")