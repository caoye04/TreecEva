import math

# Simulated sensor data processing pipeline with diagnostic checks
def collect_samples():
    return [i * 0.5 + math.sin(i) for i in range(20)]

def filter_noise(data, threshold=0.75):
    # Irrelevant filtering logic (not used in final path)
    return [x for x in data if abs(x) > threshold]

def amplify_signal(data, factor=2.0):
    return [x * factor for x in data]

def integrate_over_window(data, window_size=4):
    integrated = []
    for i in range(0, len(data) - window_size + 1):
        integrated.append(sum(data[i:i+window_size]))
    return integrated

def compress_data(sequence):
    # Dead code path — never called
    return [sequence[i] for i in range(0, len(sequence), 2)]

def validate_frame(frame):
    # Misleading validation that isn't actually used
    checksum = sum(abs(x) for x in frame) % 7
    return checksum < 5

def generate_metadata(timestamp, length):
    # Distractor function with no impact on result
    return {"ts": timestamp % 1000, "size": length, "flag": (timestamp * length) % 3}

def rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def extract_features(segment):
    # Computes statistical features, only mean is later used
    mean_val = sum(segment) / len(segment)
    variance = sum((x - mean_val) ** 2 for x in segment) / len(segment)
    peak = max(abs(x) for x in segment)
    return {'mean': mean_val, 'variance': variance, 'peak': peak}

def transform_coordinates(features_list):
    # Unused transformation
    return [(f['mean'] * 0.9, f['peak'] * 1.1) for f in features_list]

def analyze_signal(feature_set):
    base_score = feature_set['mean'] * 100
    adjustment = 0
    if feature_set['peak'] > 5:
        adjustment += 25
    elif feature_set['variance'] < 0.5:
        adjustment -= 10
    else:
        adjustment += 5
    
    # Critical red herring: complex-looking but unused expression
    decoy_value = (base_score ** 2 + adjustment * 17) % 997
    
    # Actual contribution
    return int(base_score + adjustment)

# Begin main execution
raw_readings = collect_samples()

# Apply amplification (relevant)
amplified_readings = amplify_signal(raw_readings, factor=1.8)

# Break into frames (relevant)
frame_length = 5
segmented_frames = [amplified_readings[i:i+frame_length] for i in range(0, len(amplified_readings), frame_length)]

# Process each frame to extract features (only last frame matters)
extracted_features = []
for idx, frame in enumerate(segmented_frames):
    if len(frame) == frame_length:  # Filter incomplete frames
        feat = extract_features(frame)
        # Side computation that doesn't affect outcome
        meta = generate_metadata(idx * 13, len(frame))
        extracted_features.append(feat)

# Further signal refinement using rolling average (distractor usage)
temporal_trend = rolling_average([f['mean'] for f in extracted_features], window=2)

def compute_stability_index(trend):
    if len(trend) < 2:
        return 0
    diffs = [abs(trend[i+1] - trend[i]) for i in range(len(trend)-1)]
    return round(sum(diffs) / len(diffs), 3)

stability = compute_stability_index(temporal_trend)  # Computed but unused

# Integrate over larger windows — irrelevant to final result
integrated_signal = integrate_over_window(amplified_readings, window_size=6)

# Only the last processed frame is analyzed
final_diagnostic = analyze_signal(extracted_features[-1])

# Print required result
print(f"Target result: {final_diagnostic}")