import itertools

# Simulate a data transmission pipeline with noise filtering and signal correction

def detect_anomaly(sequence):
    return sum(1 for a, b in itertools.pairwise(sequence) if abs(a - b) > 30)

def apply_filter(raw_data):
    filtered = [x for x in raw_data if 0 <= x <= 255]
    padding = [255] * (4 - len(filtered) % 4) if len(filtered) % 4 != 0 else []
    return filtered + padding

def generate_checksum(data_chunk):
    checksum = 0
    for i, val in enumerate(data_chunk):
        checksum ^= (val + i) % 256
    return checksum

def extract_features(signal):
    features = {}
    features['peak'] = max(signal)
    features['trough'] = min(signal)
    features['delta'] = features['peak'] - features['trough']
    features['slope'] = (signal[-1] - signal[0]) / len(signal) if len(signal) > 1 else 0
    return features

def validate_frame(header, payload):
    expected_length = header & 0xFF
    return len(payload) == expected_length

def merge_segments(pieces):
    flat = []
    for piece in pieces:
        flat.extend(piece)
    return flat

def process_transmission(buffer, alpha):
    # Real processing begins here
    segments = [buffer[i:i+8] for i in range(0, len(buffer), 8)]
    cleaned_segments = [apply_filter(seg) for seg in segments]
    merged = merge_segments(cleaned_segments)
    
    # Irrelevant feature extraction (distractor)
    dummy_features = extract_features(merged)
    anomaly_count = detect_anomaly(merged)
    
    # Core transformation
    adjusted = [(val * alpha) % 256 for val in merged]
    
    # Checksum-based validation (only some paths matter)
    chk = generate_checksum(adjusted[:16] if len(adjusted) >= 16 else adjusted)
    
    # Dead code path - never alters outcome
    if chk < 100:
        backup = adjusted.copy()
        for i in range(len(backup)):
            backup[i] = (backup[i] + 10) % 256
    
    # Actual answer derivation
    magnitude = sum(x for x in adjusted if x > 100)
    penalty = sum(1 for x in adjusted if x < 10) * 15
    base_score = magnitude - penalty
    
    # Final nonlinear transformation
    final_signal = int((base_score * 0.87) + (chk * 0.13))
    
    # Unused intermediate variables (distraction)
    normalized = [x / 255.0 for x in adjusted]
    entropy_approx = sum(-p * p for p in normalized if p > 0)
    
    return final_signal

# Simulated input data
raw_input = [120, 150, 200, 5, 230, 180, 25, 170, 90, 210, 15, 160, 190, 240, 10, 140]
noise_spike = [-10, 300, 500, -20]  # Invalid values to be filtered
extended_buffer = raw_input + noise_spike + [220, 110]

# Add irrelevant string processing (distractor using string methods)
log_tag = "TX_LOG_2024"
if log_tag.startswith("TX") and log_tag.endswith("2024"):
    encoded_tag = ''.join(f'{ord(c):02x}' for c in log_tag)
    tag_sum = sum(int(encoded_tag[i:i+2], 16) for i in range(0, len(encoded_tag), 2))

# Dictionary operations for metadata tracking (mostly unused)
system_state = {
    'version': '3.7.1',
    'mode': 'transmit',
    'priority': 5,
    'flags': {'secure': True, 'debug': False}
}

# Critical parameter - only this affects result meaningfully
correction_factor = 1.15

# Signal buffer used in main computation
signal_buffer = extended_buffer

# Key execution point
final_signal = process_transmission(signal_buffer, correction_factor)

# Output result as required
print(f"Result: {final_signal}")