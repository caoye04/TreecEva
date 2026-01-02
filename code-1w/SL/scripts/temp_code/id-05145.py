from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
def fetch_sensor_stream():
    raw_samples = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    timestamps = list(range(100, 210, 10))
    metadata = {'source': 'alpha', 'version': '2.1', 'calibrated': False}
    return raw_samples, timestamps, metadata

# Irrelevant auxiliary function - decoy for signal processing
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed  # Never used in actual computation path

# Noise floor estimation - looks important but unused
def estimate_noise_floor(samples):
    return sum(1 for x in samples if x < 3) * 0.5

# Core transformation: apply squaring and modulo pattern
def transform_readings(samples):
    result = []
    for i, val in enumerate(samples):
        if i % 2 == 0:
            result.append((val ** 2) % 7)
        else:
            result.append((val + 3) % 7)
    return result

# Filter out values based on dynamic threshold (unused branch)
def adaptive_filter(seq, threshold=4):
    return [x for x in seq if x >= threshold]

# Frequency analysis using Counter (distractor computation)
def frequency_insights(seq):
    freq = Counter(seq)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    return modes  # Computed but not used

# Main analysis pipeline with red herrings
def analyze_signal(data_packet):
    readings, labels = data_packet['values'], data_packet['labels']
    
    # Step 1: Map labels to numeric scores (some are irrelevant)
    label_score = defaultdict(int)
    for lbl in labels:
        if lbl.startswith('A'):
            label_score['A_group'] += 1
        elif lbl.startswith('B'):
            label_score['B_group'] += 2
    
    # Step 2: Transform readings through multi-stage logic
    stage1 = [(x * 2 + 1) % 10 for x in readings]
    stage2 = [math.ceil(x * 0.5) for x in stage1]
    stage3 = [x for i, x in enumerate(stage2) if i % 3 != 2]  # Skip every third
    
    # Step 3: Accumulate conditional sum
    accumulator = 0
    for i, val in enumerate(stage3):
        if val in {2, 4, 6}:
            accumulator += val * (i + 1)
        elif val == 3:
            accumulator -= 5
    
    # Step 4: Apply bit manipulation chain
    temp = accumulator ^ 255
    temp = temp & 127
    temp = (temp >> 3) | 17
    
    # Step 5: Conditional adjustment based on length parity
    if len(stage3) % 2 == 0:
        temp = int(temp * 1.5)
    else:
        temp = int(temp * 0.8)
    
    # Final diagnostic computed from transformed data
    final_diagnostic = abs(temp - 44) * 3
    
    # === DISTRACTOR BLOCK: Unused but plausible computations ===
    decoy_1 = [x for x in stage1 if x > 5]
    decoy_2 = sum(readings[i] for i in range(0, len(readings), 2))
    _ = estimate_noise_floor(readings)
    _ = smooth_signal(readings)
    _ = adaptive_filter(stage3)
    _ = frequency_insights(stage1)
    # ==========================================================
    
    return final_diagnostic

# Setup and execution
raw_data, time_stamps, meta_info = fetch_sensor_stream()

# Build processed data structure
processed_labels = ['A_' + str(i) if i % 2 == 0 else 'B_' + str(i) for i in range(len(raw_data))]
transformed_values = transform_readings(raw_data)

# Construct input packet (note: time_stamps and meta_info not used)
data_context = {
    'values': transformed_values,
    'labels': processed_labels,
    'timestamp': 150  # Only partial use
}

# Execute main analysis
final_diagnostic = analyze_signal(data_context)

# Output target result
print(f"Target result: {final_diagnostic}")