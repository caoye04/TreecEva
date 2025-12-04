def calculate_checksum(data):
    # Calculate checksum for validation
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val * (i + 1)) & 0xFF
    return checksum

def apply_noise_reduction(signal, threshold=15):
    # Apply noise reduction filter
    filtered = []
    noise_profile = [3, 7, 2, 9, 4]
    
    for i, val in enumerate(signal):
        noise = noise_profile[i % len(noise_profile)]
        if abs(val) > threshold:
            filtered.append(val - noise if val > 0 else val + noise)
        else:
            filtered.append(0)  # Suppress low signals
    
    return filtered

def extract_features(signal):
    # Extract key features from signal
    if not signal:
        return 0
    
    peaks = [signal[i] for i in range(1, len(signal)-1) 
             if signal[i] > signal[i-1] and signal[i] > signal[i+1]]
    
    valleys = [signal[i] for i in range(1, len(signal)-1)
               if signal[i] < signal[i-1] and signal[i] < signal[i+1]]
    
    # Feature calculation is peak-valley difference
    if peaks and valleys:
        return max(peaks) - min(valleys)
    elif peaks:
        return max(peaks)
    elif valleys:
        return -min(valleys)
    return 0

def normalize_signal(data):
    # Normalize signal to standard range
    if not data:
        return []
    
    max_val = max(map(abs, data))
    if max_val == 0:
        return data
    
    return [round((x / max_val) * 100) for x in data]

def process_signal(data):
    # Main signal processing function
    if calculate_checksum(data) % 2 == 0:
        # Even checksum path
        harmonic_factors = [0.5, 1.0, 1.5, 2.0, 2.5]
        harmonics = [sum(x * factor for factor in harmonic_factors) for x in data]
        strength = sum(harmonics) / len(harmonics) if harmonics else 0
    else:
        # Odd checksum path - the one that matters
        signal_range = max(data) - min(data)
        frequency = sum(1 for i in range(1, len(data)) if (data[i] > 0) != (data[i-1] > 0))
        strength = signal_range * frequency / (len(data) if len(data) > 0 else 1)
    
    # Apply final calibration
    return int(strength) ^ 0x2F

# Signal data (raw measurements from sensor)
raw_signal = [23, -15, 42, -8, 31, -19, 27, -5, 16]

# Preprocessing
processed_signal = [x + 5 if x < 0 else x - 5 for x in raw_signal]

# Calculate baseline statistics (not used in final calculation)
baseline_mean = sum(processed_signal) / len(processed_signal)
baseline_variance = sum((x - baseline_mean) ** 2 for x in processed_signal) / len(processed_signal)

# Apply transformation based on variance (distractor)
transformed_data = lambda data, var: [x * (var / 100) if var > 50 else x for x in data]
transformed_signal = transformed_data(processed_signal, baseline_variance)

# Signal filtering - the important step
filtered_data = []
for i, val in enumerate(raw_signal):
    # Complex filtering logic with bitwise operations
    filter_mask = (i & 0x3) + 1
    if i % 2 == 0:
        # Even indices - apply one transformation
        adjusted = (val + filter_mask) & 0xFF
        filtered_data.append(adjusted)
    else:
        # Odd indices - apply different transformation
        adjusted = (val - filter_mask) & 0xFF
        filtered_data.append(adjusted)

# Calculate noise profile (distractor)
noise_profile = apply_noise_reduction(filtered_data)
feature_score = extract_features(noise_profile)

# Normalize for visualization (distractor)
normalized = normalize_signal(filtered_data)

# Process the filtered data to get final signal strength
final_signal_strength = process_signal(filtered_data)

print(f"Result: {final_signal_strength}")