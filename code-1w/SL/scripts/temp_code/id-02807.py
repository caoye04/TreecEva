import math

# Simulated sensor data acquisition
def acquire_signal():
    raw_samples = [x * 0.1 for x in range(300)]
    noise_floor = [0.5 * math.sin(x) + 0.3 * math.cos(2*x) for x in raw_samples]
    signal_power = [abs(math.sin(x) * math.exp(-x/100)) for x in raw_samples]
    return [signal_power[i] + noise_floor[i] for i in range(len(raw_samples))]

# Irrelevant auxiliary function (decoy)
def analyze_frequency_spectrum(data):
    n = len(data)
    fft_real = [sum(data[k] * math.cos(2 * math.pi * i * k / n) for k in range(n)) for i in range(n)]
    fft_imag = [sum(-data[k] * math.sin(2 * math.pi * i * k / n) for k in range(n)) for i in range(n)]
    magnitude = [math.sqrt(fft_real[i]**2 + fft_imag[i]**2) for i in range(n)]
    # Dead code path — never used
    if any(m > 100 for m in magnitude):
        return [m / 10 for m in magnitude]
    return magnitude

# Signal preprocessing with distractors
def preprocess(data):
    offset_correction = sum(data[:50]) / 50
    corrected = [x - offset_correction for x in data]
    
    # Distractor: normalization that isn't actually used later
    max_val = max(abs(x) for x in corrected)
    normalized = [x / max_val for x in corrected] if max_val != 0 else corrected
    
    # Actual relevant transformation: apply logarithmic compression
    compressed = [math.log(1 + abs(x)) * math.copysign(1, x) for x in corrected]
    
    # Red herring: smoothing with multiple unused variants
    smoothed_v1 = [sum(compressed[max(0,i-1):min(i+2,len(compressed))]) / 3 for i in range(len(compressed))]
    smoothed_v2 = [sum(compressed[max(0,i-2):min(i+3,len(compressed))]) / 5 for i in range(len(compressed))]
    
    # Only this one is passed forward
    return smoothed_v1

# Filtering logic with conditional bypass (misleading control flow)
def filter_artifacts(data, method='median'):
    window_size = 3
    filtered = []
    for i in range(len(data)):
        start = max(0, i - window_size)
        end = min(len(data), i + window_size + 1)
        segment = sorted(data[start:end])
        median_val = segment[len(segment)//2]
        mean_val = sum(segment) / len(segment)
        
        # Decoy logic branch — condition never true due to data properties
        if method == 'adaptive' and all(x > 0.5 for x in segment):
            filtered.append(mean_val)
        elif method == 'mean':
            filtered.append(mean_val)
        else:
            filtered.append(median_val)  # Always taken
    
    # Extra irrelevant transformation
    enhanced = [x * 1.1 if x > 0.2 else x for x in filtered]
    degraded = [x * 0.9 for x in filtered]  # Unused
    
    return enhanced  # Return the enhanced version (subtly different)

# Core processing with bit manipulation red herring
def extract_features(signal):
    # Convert continuous values to discrete bins (relevant)
    bins = [int(abs(x) * 10) & 0xFF for x in signal]  # Bitwise AND is just clamping, not cryptographic
    
    # Useless bit rotation chain
    rotated = []
    for b in bins:
        temp = ((b << 3) & 0xFF) | (b >> 5)  # Rotate left by 3
        temp = ((temp >> 2) & 0xFF) | (temp << 6)  # Rotate right by 2
        temp = temp ^ 0xAA  # XOR mask (no effect on final result)
        rotated.append(temp)
    
    # Real feature: count significant activations
    significant = len([x for x in signal if abs(x) > 0.15])
    energy = sum(x*x for x in signal)
    
    # Fake entropy calculation (dead end)
    histogram = [0] * 16
    for b in bins:
        histogram[b % 16] += 1
    entropy = -sum((h / len(bins)) * math.log(h / len(bins)) for h in histogram if h > 0)
    
    return significant, energy  # Only these two are used later

# Final decision logic with misleading redundancy
def process_signals(data, threshold):
    preprocessed = preprocess(data)
    filtered_data = filter_artifacts(preprocessed)
    feature_count, total_energy = extract_features(filtered_data)
    
    # Multiple candidate outputs — only one matters
    candidate_a = int(total_energy * 100) % 1000
    candidate_b = feature_count * 7
    candidate_c = (feature_count + int(total_energy)) * 3
    
    # Critical logic buried in distractions
    adjustment_factor = 1
    if feature_count > threshold * 2:
        adjustment_factor *= 1.5
    if total_energy < threshold:
        adjustment_factor *= 0.5
    
    intermediate = (candidate_a + candidate_b) // 2
    final_output = int(intermediate * adjustment_factor)  # This is the real answer
    
    # Dead code: alternative fusion methods
    fusion_alt1 = math.sqrt(candidate_a * candidate_c)
    fusion_alt2 = (candidate_b * 2 + candidate_c) // 3
    
    # Print for traceability (required)
    print(f"Result: {final_output}")
    return final_output

# Misleading initialization block
def main():
    baseline = [0.1 * math.sin(i * 0.2) for i in range(100)]
    calibration_matrix = [[i*j % 7 for j in range(5)] for i in range(5)]
    checksum = sum(sum(row) for row in calibration_matrix) % 13
    
    # Actual execution begins here
    raw_signal = acquire_signal()
    threshold = len(raw_signal) // 150  # Evaluates to 2
    filtered_data = filter_artifacts(preprocess(raw_signal), method='median')
    
    # Key statement
    final_output = process_signals(filtered_data, threshold)

if __name__ == "__main__":
    main()