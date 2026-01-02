import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_samples = [0.1, 0.3, 0.4, 0.8, 1.2, 1.5, 2.1, 2.7, 3.0, 3.5]
    scale_factor = 2.5
    calibrated = [x * scale_factor for x in raw_samples]
    return calibrated

# Irrelevant helper: format timestamp (distractor)
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f'{hours:02}:{mins:02}:{secs:06.3f}'

timestamp_log = []
for t in range(10):
    timestamp_log.append(format_timestamp(t * 30))

# Noise filter (actually unused path - red herring)
def apply_noise_gate(signal, threshold=0.5):
    return [x if abs(x) > threshold else 0.0 for x in signal]

# Real preprocessing chain
def preprocess(signal_chunk):
    filtered = [x for x in signal_chunk if x > 1.0]  # Only values above threshold
    normalized = [math.log(x + 1) for x in filtered]
    shifted = [x - 0.5 for x in normalized]
    return shifted

# Data transformation with string-based tagging (uses string method)
def tag_series(data_list):
    tags = []
    for i, val in enumerate(data_list):
        bin_label = 'HIGH' if val > 1.0 else 'LOW'
        tag = f'SENSOR_{i:03d}'.lower() + f'_{bin_label}'
        tags.append(tag)
    return tags

# Core analysis function
def compute_magnitude_profile(values):
    profile = []
    cumulative = 0.0
    for v in values:
        adjusted = abs(v) ** 1.5
        cumulative += adjusted
        profile.append(cumulative)
    return profile

# Secondary metric (decoy - not used in final result)
def calculate_entropy(signal):
    from collections import Counter
    rounded = [round(x, 1) for x in signal]
    counts = Counter(rounded)
    total = len(rounded)
    entropy = -sum((count / total) * math.log2(count / total) 
                   for count in counts.values())
    return round(entropy, 4)

# Main diagnostic engine
def analyze_signal(data_sequence):
    if not data_sequence:
        return -999.0
    
    # Transform and extract features
    magnitude_trace = compute_magnitude_profile(data_sequence)
    latest_magnitude = magnitude_trace[-1]
    
    # Evaluate stability (string method used in filtering)
    status_flags = tag_series(data_sequence)
    critical_events = [flag for flag in status_flags if 'HIGH' in flag.upper()]
    event_count = len(critical_events)
    
    # Final computation
    base_score = latest_magnitude * 1.75
    penalty = event_count * 0.25
    diagnostic_value = base_score - penalty
    
    # Dead code branch (misleading)
    if len(data_sequence) > 20:
        fallback = sum(data_sequence) / len(data_sequence)
        diagnostic_value = fallback  # never reached
    
    return round(diagnostic_value, 6)

# --- Execution Flow ---
sensor_data = collect_samples()
processed_data = preprocess(sensor_data)

# Unused intermediate results (distractors)
decoy_filtered = apply_noise_gate(sensor_data)
decoy_entropy = calculate_entropy(sensor_data)
series_tags = tag_series(processed_data)

# Key statement
final_diagnostic = analyze_signal(processed_data)

# Print result
print(f"Result: {final_diagnostic}")