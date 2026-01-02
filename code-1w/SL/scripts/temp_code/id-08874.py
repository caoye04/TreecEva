import math

# Simulated sensor data and diagnostic system with multiple processing layers
def collect_sensor_readings():
    raw_readings = [0.78, 0.91, 0.22, 0.45, 0.63, 0.87, 0.33, 0.51]
    scale_factor = 1.05
    adjusted = [x * scale_factor for x in raw_readings]
    return adjusted

# Irrelevant auxiliary function - decoy
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 3)

# Signal baseline correction - relevant
def remove_noise(signal):
    threshold = 0.25
    filtered = [x if x > threshold else 0.0 for x in signal]
    norm_factor = sum(filtered) / len(filtered) if any(filtered) else 0.0
    normalized = [x / norm_factor for x in filtered] if norm_factor != 0 else filtered
    return normalized

# Frequency domain approximation - partially relevant but misleading
def estimate_dominant_frequency(series):
    n = len(series)
    fourier = []
    for k in range(n // 2):
        re = im = 0
        for t in range(n):
            angle = 2 * math.pi * k * t / n
            re += series[t] * math.cos(angle)
            im += series[t] * math.sin(angle)
        magnitude = math.sqrt(re*re + im*im)
        fourier.append(magnitude)
    peak = max(fourier) if fourier else 0
    return round(peak, 4)

# Data windowing - irrelevant
def apply_hamming_window(data):
    N = len(data)
    windowed = [data[i] * (0.54 - 0.46 * math.cos(2 * math.pi * i / (N-1))) for i in range(N)]
    return windowed  # never used in final path

# Core transformation - critical
def transform_magnitude(values):
    transformed = []
    for v in values:
        if v == 0:
            transformed.append(0)
        else:
            transformed.append(math.exp(math.sqrt(v)))
    return [round(x, 4) for x in transformed]

# Secondary filter - red herring
def smooth_data(seq):
    if len(seq) < 3:
        return seq
    smoothed = [seq[0]]
    for i in range(1, len(seq)-1):
        smoothed.append(round((seq[i-1] + seq[i] + seq[i+1]) / 3, 4))
    smoothed.append(seq[-1])
    return smoothed

# Final analysis engine - contains key logic
def analyze_signal(data_chunk):
    # Step 1: Extract features
    feature_set = []
    for val in data_chunk:
        if val > 1.0:
            feature_set.append(int(val * 10) % 7)
    
    # Step 2: Generate checksum (distraction)
    temp_checksum = 0
    for i, v in enumerate(feature_set):
        temp_checksum += v * (i + 1)
    temp_checksum = temp_checksum % 11
    
    # Step 3: Real computation path
    base_accum = 0
    for x in data_chunk:
        if x > 0:
            base_accum += math.log(x) * 100
    intermediate = int(abs(base_accum))
    
    # Step 4: Apply combinatoric adjustment
    length = len(data_chunk)
    combos = 0
    for i in range(1, length + 1):
        combos += math.comb(length, i) if i <= 5 else 0  # limit to avoid overflow
    
    # Step 5: Final mapping
    result = intermediate - (combos % 100)
    scaling_offset = len([x for x in data_chunk if x > 0.5])  # list comprehension
    final_score = result + (scaling_offset ** 2)
    
    # Dead code branch - misleading
    if temp_checksum > 15:
        final_score = -999  # unreachable
    
    return final_score

# Orchestration with distractions
if __name__ == '__main__':
    readings = collect_sensor_readings()  # initial data
    
    # Distractor block 1: Entropy analysis (unused)
    entropy_value = compute_entropy(readings)
    frequency_peak = estimate_dominant_frequency(readings)
    
    # Critical path starts here
    cleaned = remove_noise(readings)
    processed_data = transform_magnitude(cleaned)
    
    # Distractor block 2: Smoothing and windowing (not used)
    smoothed_data = smooth_data(processed_data)
    windowed_data = apply_hamming_window(processed_data)
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")