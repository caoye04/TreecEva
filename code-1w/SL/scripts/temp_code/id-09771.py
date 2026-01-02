import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 4.1, 2.8, 5.6, 3.9, 4.4, 2.1, 6.3]
threshold = 4.0
calibration_factor = 0.92
noise_floor = 0.15

# Irrelevant constants (distractors)
battery_level = 87
temperature_k = 298
packet_count = 1024
redundant_flag = True
sync_interval = 15

# Step 1: Filter readings above threshold
critical_readings = [x for x in raw_readings if x > threshold]

# Step 2: Apply calibration and noise correction
adjusted_readings = [(x * calibration_factor) - noise_floor for x in critical_readings]

# Step 3: Compute statistical moments
mean_val = sum(adjusted_readings) / len(adjusted_readings)
variance = sum((x - mean_val) ** 2 for x in adjusted_readings) / len(adjusted_readings)
std_dev = math.sqrt(variance)

# Step 4: Normalize readings
normalized = [(x - mean_val) / std_dev for x in adjusted_readings]

# Step 5: Detect anomalies using z-score > 1.0
anomalies = [x for x in normalized if abs(x) > 1.0]

# Step 6: Transform into frequency domain (simulated DFT)
frequencies = []
for k in range(3):
    real = sum(normalized[n] * math.cos(2 * math.pi * k * n / len(normalized)) for n in range(len(normalized)))
    imag = -sum(normalized[n] * math.sin(2 * math.pi * k * n / len(normalized)) for n in range(len(normalized)))
    magnitude = math.sqrt(real**2 + imag**2)
    frequencies.append(magnitude)

# Step 7: Apply non-linear compression
compressed = list(map(lambda x: math.log(1 + x ** 2), frequencies))

# Step 8: Build diagnostic profile using dictionary and set operations
profile_keys = {'baseline', 'variance', 'peak_freq', 'compression_ratio', 'stability'}
required_keys = {'baseline', 'peak_freq', 'stability', 'diagnostics'}
discovered_features = profile_keys.intersection(required_keys)

feature_score = {
    'baseline': mean_val,
    'peak_freq': max(compressed) if compressed else 0,
    'stability': 1 / (std_dev + 0.1),
    'compression_ratio': len(anomalies) / len(normalized) if normalized else 0,
    'diagnostics': len(discovered_features)
}

# Dead code path - never executed (red herring)
def legacy_diagnostic(data):
    return sum(math.sin(x) for x in data) % 7

# Unused helper (distractor)
conversion_table = {i: round(math.tan(i * 0.1), 3) for i in range(10)}

# Step 9: Process data through multiple conditional layers
def process_signal(signal_chunk):
    if not signal_chunk:
        return [0]
    
    # Intermediate transformation
    transformed = [math.exp(-x*x) for x in signal_chunk]
    
    # Conditional amplification
    if len(transformed) > 2:
        amplified = [x * 1.5 for x in transformed]
    else:
        amplified = [x * 0.8 for x in transformed]
    
    # Early return based on length
    if len(amplified) == 0:
        return [999]  # dead branch
    
    # Final smoothing
    smoothed = [round(x, 3) for x in amplified]
    return smoothed

# Step 10: Analyze signal recursively
def analyze_signal(data):
    if len(data) <= 1:
        return data[0] if data else 0
    
    # Split and recurse
    mid = len(data) // 2
    left = analyze_signal(data[:mid])
    right = analyze_signal(data[mid:])
    
    # Combine with weighting
    weight = feature_score['stability']
    combined = (left * 0.4 + right * 0.6) * weight
    
    # Introduce subtle bias correction
    if combined > 5:
        combined -= 0.25
    elif combined < -5:
        combined += 0.25
    
    return round(combined, 4)

# Step 11: Execute main processing pipeline
interim_results = []
for val in adjusted_readings:
    if val > mean_val:
        processed = process_signal([val])
        interim_results.extend(processed)

# Add irrelevant post-processing
buffer_size = len(interim_results) * 2
checksum = sum(interim_results[i] * (i + 1) for i in range(len(interim_results)))

# Step 12: Final diagnostic computation
final_diagnostic = analyze_signal(interim_results)

# Output result as required
print(f"Target result: {final_diagnostic}")