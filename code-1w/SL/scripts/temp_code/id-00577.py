import math

# Simulated sensor data processing with red herrings and complex flow
def preprocess_signal(raw_input):
    filtered = [x for x in raw_input if x > 0.1]
    normalized = [val / max(filtered) for val in filtered]
    return normalized

# Irrelevant transformation chain (dead path)
def deprecated_filter(seq):
    temp = [math.sin(x) for x in seq]
    return [t for t in temp if t > 0.5]

# Unused helper function (decoy)
def calculate_entropy(data):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    probabilities = [count / len(data) for count in freq_map.values()]
    return -sum(p * math.log2(p) for p in probabilities)

# Core logic: pattern detection using slicing and thresholds
def extract_segments(signal):
    segments = []
    i = 0
    while i < len(signal) - 5:
        window = signal[i:i+6]
        if sum(window) / len(window) > 0.5:
            segments.append(window)
        i += 3  # Overlapping stride
    return segments

# Data augmentation (distractor - never called)
def augment_data(samples):
    augmented = []
    for s in samples:
        augmented.append([x * 1.1 for x in s])
        augmented.append([x * 0.9 for x in s])
    return augmented

# Main analysis pipeline
def analyze_pattern(input_stream):
    # Step 1: Noise thresholding
    cleaned = [x for x in input_stream if 0.05 < x < 0.95]
    
    # Step 2: Generate multiple derived sequences (some irrelevant)
    squared_values = [x**2 for x in cleaned]
    shifted_phase = [math.cos(x) for x in cleaned]  # unused downstream
    inverted = [1 - x for x in cleaned]  # decoy calculation
    
    # Step 3: Critical slicing-based feature extraction
    mid_third = cleaned[len(cleaned)//3 : 2*len(cleaned)//3]
    if len(mid_third) == 0:
        mid_third = [0.5]
    
    # Step 4: Apply moving average via slicing
    smoothed = []
    for j in range(2, len(mid_third)):
        window_avg = sum(mid_third[j-2:j+1]) / 3
        smoothed.append(window_avg)
    
    # Step 5: Detect anomaly clusters
    anomalies = []
    for val in smoothed:
        if val > 0.65 or val < 0.35:
            anomalies.append(val)
    
    # Step 6: Compute diagnostic metric
    trigger_count = 0
    history_log = []  # unused logging array (distraction)
    for a in anomalies:
        if a > 0.65:
            trigger_count += 2
        else:
            trigger_count += 1
        history_log.append(f'Anomaly: {a:.4f}')
    
    # Step 7: Final nonlinear transformation (key result)
    base_score = trigger_count * (sum(smoothed) / len(smoothed))
    adjustment_factor = math.sqrt(len(anomalies)) if anomalies else 1.0
    final_diagnostic = int(base_score * adjustment_factor * 100)
    
    return final_diagnostic

# --- Execution Body ---
if __name__ == '__main__':
    # Simulated telemetry input (real source)
    raw_telemetry = [
        0.05, 0.82, 0.33, 0.71, 0.29, 0.88, 0.11, 0.76,
        0.65, 0.24, 0.70, 0.31, 0.83, 0.19, 0.67, 0.26,
        0.74, 0.34, 0.69, 0.22, 0.78, 0.30, 0.66, 0.27
    ]
    
    # Irrelevant preprocessing trace
    processed_signal = preprocess_signal(raw_telemetry)
    legacy_output = deprecated_filter(processed_signal)  # dead assignment
    
    # Core execution path
    transformed_data = extract_segments(processed_signal)
    flattened = []
    for segment in transformed_data:
        flattened.extend(segment)
    
    # Critical statement
    final_diagnostic = analyze_pattern(flattened)
    
    # Output target variable
    print(f"Result: {final_diagnostic}")