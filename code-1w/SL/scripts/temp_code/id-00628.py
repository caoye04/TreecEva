import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_samples = [i * 0.5 + (i % 7) for i in range(120)]
    offset = 4.87
    calibrated = [x + offset for x in raw_samples]
    return calibrated

# Irrelevant transformation - red herring
def compute_harmonic_profile(data):
    if len(data) == 0:
        return 0
    inv_sum = sum(1 / (x + 1e-5) for x in data)
    return len(data) / inv_sum

# Distractor function - never called in execution path
def legacy_filter_chain(x):
    temp = x >> 2
    temp = temp ^ 0xAA
    temp = (temp + 17) % 256
    return temp

# Signal preprocessing with multiple layers
def preprocess_signal(raw):
    filtered = [x for x in raw if abs(x - 50) < 40]  # Bandpass filter via list comprehension
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    
    # Dead code branch - misleading intermediate result
    if sum(normalized) < 0:
        scaled = [x * 100 for x in normalized]
    else:
        scaled = [x * 10 for x in normalized]  # Actual path
    
    # Create decoy statistics
    avg_val = sum(scaled) / len(scaled)
    peak = max(scaled)
    dummy_metric = (avg_val * peak) ** 0.5
    
    # Frame segmentation
    frames = [scaled[i:i+8] for i in range(0, len(scaled), 8)]
    trimmed_frames = [f for f in frames if len(f) == 8]
    return trimmed_frames

# Core analysis logic
def analyze_frame_quality(frame):
    if not frame:
        return 0.0
    variance = sum((x - sum(frame)/len(frame))**2 for x in frame) / len(frame)
    return round(variance, 4)

# Misleading auxiliary function with bit manipulation red herring
def encode_diagnostic_code(code):
    encoded = ((code << 3) & 0xFF) | (code >> 5)
    encoded = encoded ^ 0xF0
    return encoded if encoded > 0 else 1

# Main analyzer - contains key logic
def analyze_signal(frames):
    qualities = []
    for frame in frames:
        quality = analyze_frame_quality(frame)
        if quality > 0.1:
            qualities.append(quality)
            if len(qualities) > 10:  # Early termination condition
                break
    
    # Complex conditional computation
    if len(qualities) == 0:
        base_score = 0
    elif len(qualities) == 1:
        base_score = qualities[0] * 100
    else:
        mid_vals = sorted(qualities)[1:-1]  # Exclude outliers
        if len(mid_vals) == 0:
            base_score = max(qualities) * 50
        else:
            base_score = (sum(mid_vals) / len(mid_vals)) * 100
    
    # Apply nonlinear transformation
    adjusted = int(base_score * math.log(base_score + 2))
    
    # Decoy operations
    checksum = 0
    for i, q in enumerate(qualities):
        checksum ^= int(q * 100) & 0xFF
    
    final_weight = len(frames) % 13
    adjusted += final_weight * 7
    
    # Final diagnostic calculation
    final_diagnostic = adjusted - 42  # Key assignment
    return final_diagnostic

# Unused but plausible-looking utility
def generate_synthetic_burst(n):
    return [math.sin(i * 0.1) * math.exp(-i/n) for i in range(n)]

# Execution flow
sensor_data = collect_readings()
processed_frames = preprocess_signal(sensor_data)
final_diagnostic = analyze_signal(processed_frames)
print(f"Result: {final_diagnostic}")