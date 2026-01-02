import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw_data = [i * 0.5 + (i % 3) for i in range(12)]
    offset = 2.5
    calibrated = [x + offset for x in raw_data]
    return calibrated

# Irrelevant helper - distractor
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total  # Unused in final computation

# Signal conditioning with red herring transformations
def filter_noise(signal):
    filtered = []
    noise_floor = 0.3
    for val in signal:
        adjusted = val * 0.9 + 0.1
        if abs(adjusted) > noise_floor:
            filtered.append(adjusted * (1 + 0.05))  # Minor amplification
        else:
            filtered.append(0.0)
    # Dead code path - misleading
    if len(filtered) > 100:
        filtered = filtered[:50]
    return filtered

# Data normalization - partially relevant, partially decoy
def normalize(data):
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val if max_val != min_val else 1
    # Decoy calculation
    avg_val = sum(data) / len(data)
    centered = [x - avg_val for x in data]  # Not used later
    # Actual used transformation
    normalized = [(x - min_val) / range_val for x in data]
    return normalized

# Complex multi-step analysis with conditional logic
def detect_anomaly_patterns(seq):
    anomalies = 0
    thresholds = [0.2, 0.4, 0.6, 0.8]
    cumulative = 0.0
    for i, val in enumerate(seq):
        # Bit manipulation red herring
        bit_flag = (i << 2) & 7
        if bit_flag == 4:
            cumulative += val * 0.1
        # Real condition
        if val > thresholds[i % 4]:
            anomalies += 1
        # Distractor: unused statistical moment
        if i > 0:
            delta = val - seq[i-1]
            jitter = delta ** 2  # Computed but not used
    return anomalies

# Core diagnostic logic - depends on prior steps
def analyze_signal(samples):
    # Initial transformation
    squared = [x**2 for x in samples]
    
    # Conditional expression (required Python feature)
    baseline = sum(squared) / len(squared) if len(squared) > 0 else 0
    
    # Multiple nested conditions with early exits (red herring)
    if baseline < 1.0:
        return -1
    elif baseline > 50.0:
        return -99
    
    # Real computation path
    adjusted = [math.sqrt(x + 1) for x in squared]
    smoothed = [sum(adjusted[i:i+3]) / 3 if i+2 < len(adjusted) else adjusted[i] for i in range(len(adjusted))]
    
    # Critical branching with meaningful logic
    if len(smoothed) >= 10:
        segment_a = smoothed[:6]
        segment_b = smoothed[6:]
        metric_x = sum(segment_a) / len(segment_a)
        metric_y = max(segment_b) - min(segment_b)
        
        # Final decision logic with arithmetic combination
        result = (metric_x * 2.5) + (metric_y * 1.75)
        
        # Distractor variables and operations
        temp_array = [result * i for i in range(3)]  # Unused
        checksum = 0
        for v in temp_array:
            checksum ^= int(v)  # Bitwise decoy
        
        # Key assignment - answer derived here
        final_diagnostic = int(result * 10 + 0.5)  # Round to nearest int
    else:
        final_diagnostic = 0
    
    return final_diagnostic

# Orchestration function
def main_pipeline():
    # Step 1: Collect data
    raw_samples = collect_samples()  # 12 elements
    
    # Step 2: Filter (relevant)
    cleaned = filter_noise(raw_samples)
    
    # Step 3: Normalize (relevant for downstream)
    processed_samples = normalize(cleaned)
    
    # Step 4: Detect anomalies (called but result unused - red herring)
    anomaly_count = detect_anomaly_patterns(processed_samples)
    
    # Step 5: Perform final analysis (contains key statement)
    final_diagnostic = analyze_signal(processed_samples)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    
    # Irrelevant cleanup
    del raw_samples, cleaned, processed_samples
    
    return final_diagnostic

# Execute
main_pipeline()