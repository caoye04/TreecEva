import math

# Simulated sensor data acquisition
def acquire_sensor_data():
    raw_samples = [i * 0.01 for i in range(1000)]
    noise_floor = sum([math.sin(x * 3.1415) * 0.5 for x in raw_samples])
    return [math.cos(sample * 5) + noise_floor * 0.1 for sample in raw_samples]

# Irrelevant auxiliary function (distractor)
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Signal conditioning with red herring computations
def precondition_signal(raw_signal):
    offset = sum(raw_signal[:50]) / 50
    normalized = [x - offset for x in raw_signal]
    
    # Distractor: energy calculation not used later
    signal_energy = sum([x*x for x in normalized])
    spectral_weight = math.sqrt(signal_energy) / len(normalized)
    
    # Actual relevant transformation
    filtered = []
    for i in range(2, len(normalized) - 2):
        avg = sum(normalized[i-2:i+3]) / 5
        filtered.append(avg)
    
    # Padding to maintain length (used)
    padded = [filtered[0]]*2 + filtered + [filtered[-1]]*2
    return padded

# Segment extraction with decoy logic
def extract_segments(signal):
    stride = 5
    window_size = 100
    segments = []
    
    # Dead code path (never taken due to fixed parameters)
    if window_size > len(signal):
        return [signal]
    
    # Actual segment generation
    for start in range(0, len(signal) - window_size + 1, stride):
        segment = signal[start:start + window_size]
        segments.append(segment)
    
    # Additional irrelevant processing branch
    if len(segments) % 2 == 0:
        mirror_copy = [list(reversed(s)) for s in segments]
        segments.extend(mirror_copy)  # This bloates but isn't used
    
    return segments[:10]  # Trim to first 10 segments only

# Data purification with slicing distraction
def purify_segments(segments):
    purified = []
    for seg in segments:
        # Focus on central portion using slice
        center_chunk = seg[len(seg)//4 : 3*len(seg)//4]
        
        # Distractor: statistical summary not used
        mean_val = sum(center_chunk) / len(center_chunk)
        variance = sum((x - mean_val)**2 for x in center_chunk) / len(center_chunk)
        peak_to_peak = max(center_chunk) - min(center_chunk)
        
        # Relevant normalization
        std_dev = math.sqrt(variance)
        if std_dev > 1e-8:
            normalized_chunk = [(x - mean_val) / std_dev for x in center_chunk]
        else:
            normalized_chunk = center_chunk
        
        purified.append(normalized_chunk)
    return purified

# Feature extraction with misleading intermediate values
def extract_features(segments):
    features = []
    for seg in segments:
        # Real feature: zero-crossing rate in purified segment
        zero_crossings = 0
        for i in range(1, len(seg)):
            if seg[i-1] < 0 < seg[i] or seg[i-1] > 0 > seg[i]:
                zero_crossings += 1
        zcr = zero_crossings / len(seg)
        
        # Decoy features (computed but unused)
        magnitude = math.sqrt(sum(x*x for x in seg))
        skewness = sum((x**3) for x in seg) / (len(seg) * magnitude**1.5 + 1e-8)
        kurtosis_estimate = (sum(x**4 for x in seg) / len(seg)) / (magnitude**2 + 1e-8)
        
        # Only zcr is actually carried forward
        features.append({'zcr': zcr, 'mag': magnitude})
    return features

# Final analysis incorporating accumulation and thresholds
def analyze_signal(segments):
    features_list = extract_features(segments)
    
    # Accumulate only the relevant metric
    total_zcr = 0.0
    valid_count = 0
    threshold = 0.15
    
    # Conditional filtering based on heuristic
    for feat in features_list:
        if feat['zcr'] > threshold:
            total_zcr += feat['zcr']
            valid_count += 1
    
    # Dead computation branch (looks important but unused)
    if valid_count == 0:
        fallback_score = -1 * sum(feat['mag'] for feat in features_list)
    else:
        fallback_score = math.log(valid_count)
    
    # Final diagnostic depends only on average of qualifying ZCRs
    if valid_count > 0:
        average_zcr = total_zcr / valid_count
    else:
        average_zcr = 0.0
    
    # Secondary adjustment based on count
    adjustment_factor = 1 + (valid_count / 100)
    final_diagnostic = average_zcr * adjustment_factor * 1000
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Step 1: Acquire raw data
    raw_input_signal = acquire_sensor_data()
    
    # Step 2: Precondition signal
    conditioned_signal = precondition_signal(raw_input_signal)
    
    # Step 3: Extract temporal segments
    extracted_segments = extract_segments(conditioned_signal)
    
    # Step 4: Purify each segment (focus on core pattern)
    processed_segments = purify_segments(extracted_segments)
    
    # Step 5: Analyze signal characteristics
    final_diagnostic = analyze_signal(processed_segments)
    
    # Output target result
    print(f"Result: {final_diagnostic}")