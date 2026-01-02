from collections import defaultdict, Counter
import math

# Simulated sensor data from multiple IoT devices
temperature_readings = [23.4, 24.1, 22.8, 25.6, 26.7, 21.9, 24.3, 23.0]
humidity_readings = [45, 48, 52, 58, 61, 44, 49, 50]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1014, 1016, 1010]

# Irrelevant auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offset_table = {k: v % 7 for k, v in zip(dummy_labels, range(100, 108))}

# Signal preprocessing functions
def normalize(data):
    mean = sum(data) / len(data)
    return [(x - mean) * 1.5 for x in data]  # Amplified normalization

def detect_spikes(signal, factor=2.0):
    mean = sum(signal) / len(signal)
    std = (sum((x - mean) ** 2 for x in signal) / len(signal)) ** 0.5
    return [i for i, x in enumerate(signal) if abs(x - mean) > factor * std]

# Misleading function (dead path - never called in logic chain)
def deprecated_filter(data_stream):
    """Old filtering method, no longer used."""
    return [x for x in data_stream if x > 0.5]

# Core processing pipeline
normalized_temp = normalize(temperature_readings)
normalized_humid = normalize(humidity_readings)
spike_indices = detect_spikes(normalized_temp, factor=1.8)

# Combine relevant signals at spike locations
combined_at_spike = []
for i in spike_indices:
    if i < len(normalized_humid):
        combined_at_spike.append(normalized_temp[i] + normalized_humid[i])

# Construct multi-dimensional feature map (with red herring components)
feature_map = defaultdict(float)
for idx, val in enumerate(combined_at_spike):
    feature_map[f'event_{idx}'] = math.sin(val) * math.cos(val * 0.5)

# Add decoy entries to feature map (irrelevant)
for i in range(5):
    feature_map[f'decoy_key_{i}'] = i ** 3 - 10 * i

# Bit manipulation layer for obfuscation (partially relevant)
bit_flags = 0
for val in spike_indices:
    bit_flags ^= val << 1  # Left shift and XOR across indices

# Threshold configuration (some entries are misleading)
threshold_map = {
    'base': 0.45,
    'noise_floor': 0.1,
    'amplification': 2.1,
    'legacy_mode': 0.0,  # Unused parameter
    'bit_shift_guard': 3
}

# Data transformation using lambda and zip (core step)
processed_data = list(map(
    lambda pair: (pair[0] * threshold_map['amplification']) + (pair[1] * 0.1),
    zip(normalized_temp, normalized_humid)
))

# Another irrelevant counter (distractor)
event_counter = Counter([f'class_{i % 3}' for i in range(len(processed_data))])

# Critical analysis function with internal distractions
def analyze_signal(signal_data, thresholds):
    base_threshold = thresholds['base']
    guard_shift = thresholds['bit_shift_guard']
    
    # Internal decoy calculation
    shadow_accumulator = 0
    for i in range(10):
        shadow_accumulator += (i * 17) % 11
    
    # Real signal integration
    active_segments = [x for x in signal_data if abs(x) > base_threshold]
    
    # Spurious bit operation (looks important but only one part matters)
    signature = 0
    for x in active_segments:
        int_x = int(abs(x) * 10) % 256
        signature ^= (int_x << (guard_shift % 4)) | (int_x >> (8 - (guard_shift % 4)))
    
    # Final diagnostic depends only on this computation
    diagnostic_score = sum(math.tanh(x) for x in active_segments) * 100
    
    # Dead code branch (never reached due to prior logic)
    if len(active_segments) > 20:
        fallback = sum(signature.to_bytes(4, 'little'))
        diagnostic_score = fallback / 10.0
    
    return diagnostic_score

# Execute critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")