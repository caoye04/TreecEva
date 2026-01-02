import math

# Simulated sensor data from a thermal imaging array
temperature_readings = [23.5, 24.1, 25.0, 26.7, 27.3, 28.0, 29.1, 30.5, 31.2, 32.0]

def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def detect_outliers(values, threshold=0.8):
    # Irrelevant outlier detection (distractor)
    return [i for i, v in enumerate(values) if v > threshold]

def transform(signal):
    # Apply FFT-like transformation using basic math (simulated)
    N = len(signal)
    transformed = []
    for k in range(N // 2):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = -sum(signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(real**2 + imag**2)
        transformed.append(magnitude)
    return transformed

def filter_noise(data, cutoff=0.1):
    # Dummy filtering (not actually used in final path)
    return [x for x in data if x > cutoff]

# Preprocessing pipeline
normalized = normalize(temperature_readings)
smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)] + normalized[-2:]

# Decoy analysis branches
peak_indices = [i for i, x in enumerate(smoothed) if x > 0.7]
decoy_stats = {
    'avg_peak': sum(smoothed[i] for i in peak_indices) / len(peak_indices) if peak_indices else 0,
    'peak_count': len(peak_indices)
}

# Simulate frequency domain analysis (critical path begins here)
freq_components = transform(smoothed)
significant_freqs = [f for f in freq_components if f > 1.5]

# Red herring: entropy calculation (unused)
entropy = -sum(p * math.log(p + 1e-9) for p in normalized)

# Signal power calculation (misleading intermediate)
power_spectrum = [f ** 2 for f in freq_components]
total_power = sum(power_spectrum)

# Actual key transformation (hidden among distractors)
processed_data = [
    round(freq * 100) for freq in significant_freqs
]

# Dead code path - looks important but unused
def deprecated_analysis(arr):
    return tuple(sorted(arr)[::2])

# Lambda-based feature extractor (partial use)
feature_extractor = lambda seq: seq[::2] + [min(seq), max(seq)]
extras = feature_extractor(processed_data)

# String-based identifier generation (irrelevant but plausible)
device_id = "THM-ALPHA"
serial_checksum = sum(ord(c) for c in device_id) % 100
status_flag = device_id.lower().replace('-', '_') + f"_v{len(processed_data)}"

# Core diagnostic logic (depends on processed_data)
def analyze_signal(signal):
    if not signal:
        return -1
    
    # Complex conditional with slicing and arithmetic
    subset = signal[1:-1] if len(signal) > 2 else signal
    if len(subset) == 0:
        base_score = signal[0] if signal else 0
    elif len(subset) == 1:
        base_score = subset[0] * 1.5
    else:
        # Mix of min, max, and average
        trend = max(subset) - min(subset)
        center_avg = sum(subset) / len(subset)
        base_score = (center_avg + trend) * 0.8
    
    # Additional adjustment based on original length (tuple unpacking)
    orig_len = len(signal)
    multiplier = {1: 0.9, 2: 1.0}.get(orig_len, 1.1 + 0.05 * (orig_len - 2))
    
    # Final computation
    result = base_score * multiplier
    
    # Hidden rounding behavior
    return int(round(result))

# Execute critical statement
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")