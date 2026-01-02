import math

# Simulated sensor data preprocessing with distractions
def collect_samples(base_freq, duration):
    samples = []
    for t in range(duration * 10):
        time_point = t / 10.0
        raw_value = math.sin(2 * math.pi * base_freq * time_point)
        noise = 0.1 * math.cos(2 * math.pi * 25 * time_point + 7)  # Irrelevant high-frequency noise
        samples.append(raw_value + noise)
    return samples

# Distractor function - never used
def legacy_filter(data):
    return [x * 0.9 for x in data if abs(x) > 0.05]

# Real processing pipeline
def preprocess_signal(raw_data, threshold=0.08):
    filtered = [x for x in raw_data if abs(x) > threshold]  # List comprehension
    normalized = []
    max_val = max(map(abs, filtered)) if filtered else 1.0
    for val in filtered:
        normalized.append(val / max_val)
    
    # Bit manipulation red herring (unused path)
    checksum = 0
    for i in range(len(normalized)):
        if i % 3 == 0:
            checksum ^= int(abs(normalized[i]) * 100) & 255
    
    # Actual relevant transformation
    envelope = []
    for i in range(1, len(normalized)):
        diff = abs(normalized[i] - normalized[i-1])
        envelope.append(min(diff * 3, 1.0))
    
    # Slicing distraction
    mid_section = envelope[len(envelope)//4 : len(envelope)//2]
    average_mid = sum(mid_section) / len(mid_section) if mid_section else 0
    
    # Final processed form (this is what matters)
    return [x * (1 + average_mid) for x in envelope]

# Another decoy function
def calculate_entropy(arr):
    from collections import Counter
    counts = Counter([round(x, 1) for x in arr])
    total = len(arr)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy if total > 0 else 0

# Core analysis logic
def analyze_signal(cleaned_signal):
    if not cleaned_signal:
        return -1
    
    # Compute moving statistics
    window_size = 3
    trends = []
    for i in range(len(cleaned_signal) - window_size + 1):
        window = cleaned_signal[i:i+window_size]
        trend = sum(window[j+1] - window[j] for j in range(window_size-1))
        trends.append(trend)
    
    # Conditional expression distraction
    dominant_trend = sum(trends) / len(trends) if trends else 0
    adjustment = 1.5 if dominant_trend > 0.1 else (0.8 if dominant_trend < -0.1 else 1.0)
    
    # Critical computation path
    magnitude = sum(x**2 for x in cleaned_signal) ** 0.5
    stability = 1 / (1 + sum(abs(trends[i+1] - trends[i]) for i in range(len(trends)-1))) if len(trends) > 1 else 1
    
    # Decoy metric using bitwise (irrelevant)
    magic_flag = 0
    sample_val = int(magnitude * 10)
    for shift in [1, 3, 5]:
        magic_flag |= ((sample_val >> shift) & 1) << (shift//2)
    
    # The actual answer determinant
    diagnostic_score = magnitude * stability * adjustment
    
    # Early return red herring (never triggered in this case)
    if len(cleaned_signal) < 5:
        return round(diagnostic_score * 0.5, 4)
    
    return round(diagnostic_score, 4)

# Unused auxiliary function
def generate_report(data):
    return {"count": len(data), "peak": max(data, default=0)}

# Global distractor variables
CALIBRATION_OFFSET = 0.023
REFERENCE_PATTERN = [0.1, -0.3, 0.7, -0.6]
system_status = {'active': True, 'version': '2.1.5', 'debug': False}

# Main execution flow
raw_sensor_data = collect_samples(base_freq=2.5, duration=4)
processed_samples = preprocess_signal(raw_sensor_data, threshold=0.07)
final_diagnostic = analyze_signal(processed_samples)
print(f"Target result: {final_diagnostic}")