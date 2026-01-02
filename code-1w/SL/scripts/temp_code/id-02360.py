import math

# Simulated sensor data processing with diagnostic analysis
raw_signals = [3.2, 1.8, 4.5, 0.9, 6.7, 2.3, 8.1, 5.4, 9.0, 7.2]
noise_floor = 1.5
decay_factor = 0.85
sample_rate = 100  # Hz

# Irrelevant constants for distraction
max_iterations = 1000
scaling_constant = 0.0034
buffer_limit = 512
temp_offset = -0.7

# Real-time filter configuration (some fields are red herrings)
filter_config = {
    'type': 'butterworth',
    'order': 4,
    'cutoff': 30,
    'passband_ripple': 0.5,
    'stopband_attenuation': 40,
    'group_delay': 2.1  # unused distractor
}

# Decoy function - looks relevant but never called
def deprecated_filter(x):
    return [val * 0.9 for val in x if val > 1.0]

# Auxiliary transformation map (partially used)
case_transform = lambda s: s.upper().replace('X', 'Y')

# Generate time vector (only used for frequency masking)
time_vector = [i / sample_rate for i in range(len(raw_signals))]

# Apply decay envelope - only some components are meaningful
enveloped_signal = [
    raw_signals[i] * (decay_factor ** i) + temp_offset 
    for i in range(len(raw_signals))
]

# Noise suppression below floor (this step is critical)
suppressed_noise = [val if val >= noise_floor else 0.0 for val in enveloped_signal]

# Frequency-domain mask based on time index parity (distractor logic)
frequency_mask = [
    1.0 if int(time_vector[i] * sample_rate) % 2 == 0 else 0.75 
    for i in range(len(time_vector))
]

# Apply mask (partially affects result)
applied_mask = [
    suppressed_noise[i] * frequency_mask[i] 
    for i in range(len(suppressed_noise))
]

# Filter out zero values - creates filtered_data (key intermediate)
filtered_data = [val for val in applied_mask if abs(val) > 0.1]

# Create threshold map using complex expression (some entries unused)
threshold_map = {}
for idx, val in enumerate(filtered_data):
    key_char = chr(97 + (idx % 26))
    base_threshold = math.log(val + 2) if val > 1.0 else 0.5
    hysteresis = 0.1 * (idx % 3)  # minor variation
    deadband = 0.05 if key_char in 'aeiou' else 0.0  # mostly irrelevant
    threshold_map[key_char] = round(base_threshold + hysteresis - deadband, 4)

# Unused data structure - creates illusion of state management
calibration_registry = {
    'status': 'verified',
    'checksum': sum(int(ord(c) * 1.5) for c in threshold_map.keys()) % 1000,
    'version': '2.1a',
    'timestamp': '2023-11-05T14:32:10Z'
}

# Critical analysis function with embedded logic
def analyze_signal(data, thresholds):
    # Local normalization factor (derived from data length)
    norm_factor = len(data) / (sum(data) + 1e-8)
    
    # Transform data through nonlinear compression
    compressed = [math.tanh(x * norm_factor) for x in data]
    
    # Compute weighted score using threshold keys (only first 3 matter)
    sorted_chars = sorted(thresholds.keys())
    weight_sequence = [0.7, 0.2, 0.1]  # weights for first three
    
    # Extract top 3 threshold values by key order
    top_weights = []
    for i in range(min(3, len(sorted_chars))):
        char = sorted_chars[i]
        top_weights.append(thresholds[char] * weight_sequence[i])
    
    # Combine with compressed signal mean (only even indices used)
    signal_component = sum(
        compressed[i] for i in range(0, len(compressed), 2)
    ) / len(compressed)
    
    # Misleading entropy calculation (unused)
    entropy = -sum(p * math.log(p + 1e-9) for p in [0.1, 0.2, 0.7])
    
    # Final diagnostic is combination of weighted thresholds and signal
    final_score = sum(top_weights) * 100 + signal_component * 50
    
    # Additional adjustment based on string slicing of dummy ID
    device_id = "SNX-8675309"
    slice_val = int(device_id[-4:-2])  # extracts '30'
    final_score += slice_val  # adds 30
    
    return round(final_score, 4)

# Execute main analysis
final_diagnostic = analyze_signal(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")