import math

# Simulated bio-signal processing pipeline with extensive distractors
def preprocess_signals(raw_readings):
    filtered = []
    noise_floor = 0.041
    gain_boost = 1.87
    temp_cache = []  # Dead storage - unused later

    for reading in raw_readings:
        if abs(reading) < noise_floor:
            continue
        boosted = reading * gain_boost
        if boosted > 1.0:
            boosted = 1.0
        elif boosted < -1.0:
            boosted = -1.0
        filtered.append(boosted)
    
    # Distractor: irrelevant transformation
    normalized = [math.tanh(x * 2) for x in filtered]
    scaled = [x * 100 for x in normalized]  # Never used

    return filtered

# Irrelevant auxiliary function (decoy)
def analyze_harmonics(signal_list):
    total_power = 0.0
    for s in signal_list:
        total_power += s * s
    rms = math.sqrt(total_power / len(signal_list)) if signal_list else 0
    harmonics = [rms * 0.15, rms * 0.30]  # Unused result
    return rms  # Not used in main flow

# Core data transformation chain
def encode_features(data_stream):
    encoded = []
    window_size = 3
    
    for i in range(len(data_stream)):
        window = data_stream[max(0, i - window_size + 1):i + 1]
        avg = sum(window) / len(window)
        variance = sum((x - avg) ** 2 for x in window) / len(window)
        encoded.append((avg, variance))
    
    return encoded

# Higher-order mapping with lambda (required feature)
def apply_transfer(mapped_data):
    transfer_fn = lambda x, y: x + math.sin(y * math.pi / 4) if y != 0 else x
    applied = []
    
    for avg_val, var_val in mapped_data:
        transformed = transfer_fn(avg_val, var_val)
        applied.append(transformed)
    
    return applied

# Red herring function: looks important but unused
def compute_entropy(arr):
    from collections import Counter
    counts = Counter([round(x, 1) for x in arr])
    total = len(arr)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy

# Another decoy - operates on sets (suggested paradigm)
def detect_anomalies(readings):
    threshold_set = {x for x in readings if abs(x) > 0.8}
    baseline_set = {x for x in readings if abs(x) <= 0.3}
    anomalies = threshold_set - baseline_set
    return len(anomalies)  # Computed but not used

# Main processing workflow with multiple steps and distractions
def process_metrics(data, cfg):
    stage1 = preprocess_signals(data)
    
    # Distractor call - result ignored
    _ = analyze_harmonics(stage1)
    
    stage2 = encode_features(stage1)
    stage3 = apply_transfer(stage2)
    
    # Irrelevant set operation (distraction)
    unique_rounded = {round(x, 2) for x in stage3}
    suppression_factor = 0.91 if len(unique_rounded) > 5 else 1.0
    
    # Key computation path
    valid_range = [x for x in stage3 if -0.7 <= x <= 0.7]
    if not valid_range:
        return 0.0
    
    # Final diagnostic score based on filtered distribution
    mean_in_range = sum(valid_range) / len(valid_range)
    deviation_sum = sum(abs(x - mean_in_range) for x in valid_range)
    diagnostic_score = deviation_sum * cfg['sensitivity'] * suppression_factor
    
    # Dead code branch (never executed due to logic above)
    if len(valid_range) == 0:
        fallback = 0
        for z in stage3:
            fallback += z * 0.1
        diagnostic_score = fallback
    
    return diagnostic_score

# Configuration with misleading extra fields
cfg_params = {
    'sensitivity': 12.4,
    'sampling_rate': 256,
    'buffer_size': 1024,
    'calibration': 'auto',
    'mode': 'diagnostic'
}

# Input data - simulated neural interface readings
neural_readings = [
    0.012, -0.031, 0.055, 0.124, -0.301, 0.678, -0.812, 0.421, 
    0.103, -0.022, 0.291, 0.503, -0.721, 0.319, 0.087, -0.192,
    0.384, 0.615, -0.203, 0.074, 0.115, -0.064, 0.283, 0.492
]

# Distractor: tuple unpacking and unused assignment
primary_signal, *redundant_segments = neural_readings[::5]
shadow_copy = neural_readings.copy()
shadow_copy.reverse()  # Never used

# Transform pipeline entry point
transformed_data = encode_features(preprocess_signals(neural_readings))

# Another red herring: combinatorics-inspired counting (unused)
def count_transition_pairs(seq):
    up = down = stable = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            up += 1
        elif seq[i] < seq[i-1]:
            down += 1
        else:
            stable += 1
    return {'up': up, 'down': down, 'stable': stable}

_ = count_transition_pairs(neural_readings)  # Result discarded

# Critical execution point
final_diagnostic = process_metrics(transformed_data, cfg_params)

print(f"Result: {final_diagnostic}")