import math

# Simulated sensor fusion system for environmental monitoring
base_threshold = 42.5
noise_floor = 0.087

def generate_reference_grid(size):
    # Irrelevant function - dead code path
    return [[i * j for j in range(size)] for i in range(size)]

def deprecated_filter(data):
    # Outdated signal processing - never called
    return [x for x in data if x > sum(data) / len(data)]

def normalize_signal(raw_data, scale_factor=1.0):
    normalized = []
    offset = 0.112
    for val in raw_data:
        adjusted = (val + offset) * scale_factor
        if adjusted > base_threshold:
            adjusted = base_threshold + (adjusted - base_threshold) * 0.3
        normalized.append(round(adjusted, 3))
    return normalized

def detect_peaks(signal, sensitivity=0.75):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            if signal[i] > base_threshold * sensitivity:
                peaks.append(i)
    return set(peaks)

def compute_entropy(values):
    # Unused complexity - distractor
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def fuse_sensors(primary, secondary, weights=(0.7, 0.3)):
    # Sensor fusion with weighted average
    fused = []
    for p, s in zip(primary, secondary):
        fused.append(round(weights[0] * p + weights[1] * s, 3))
    return fused

def flag_anomalies(readings):
    # Misleading intermediate logic
    alerts = []
    for r in readings:
        if r < 20 or r > 80:
            alerts.append(True)
        else:
            alerts.append(False)
    return alerts

def validate_integrity(checkpoints):
    # Red herring function - not part of main flow
    cumulative = 0
    for cp in checkpoints:
        cumulative = (cumulative * 31 + cp) % 10007
    return cumulative == 128

def transform_coordinates(indices, dimension=2):
    # Decoy transformation
    if dimension == 2:
        return [(i // 10, i % 10) for i in indices]
    return []

def analyze_readings(processed):
    # Core analysis logic
    peak_set_a = detect_peaks(processed, sensitivity=0.75)
    inverted = [100 - p for p in processed]
    peak_set_b = detect_peaks(inverted, sensitivity=0.68)
    
    # Key intersection operation
    confirmed_events = peak_set_a & peak_set_b  # Set intersection
    
    # Secondary validation
    magnitude_check = sum(1 for p in processed if p > 45) >= 3
    
    # Critical computation path
    if confirmed_events and magnitude_check:
        avg_position = sum(confirmed_events) / len(confirmed_events)
        base_value = processed[int(avg_position)]
        adjustment = len(confirmed_events) * 1.75
        result = base_value + adjustment
    else:
        fallback_set = detect_peaks(processed, sensitivity=0.9)
        if fallback_set:
            result = min(fallback_set) * 2.5
        else:
            result = 42.0
    
    # Final scaling
    final_score = result * 1.6
    return round(final_score, 3)

# Main execution flow
if __name__ == "__main__":
    # Raw sensor inputs
    sensor_a = [38.2, 45.1, 52.3, 39.8, 47.6, 53.2, 44.1, 37.5]
    sensor_b = [40.1, 43.8, 50.7, 41.2, 46.3, 51.8, 42.9, 38.7]
    
    # Normalize signals
    norm_a = normalize_signal(sensor_a, scale_factor=1.02)
    norm_b = normalize_signal(sensor_b, scale_factor=0.98)
    
    # Fuse sensor data
    fused_signal = fuse_sensors(norm_a, norm_b)
    
    # Apply additional filtering (distractor)
    filtered_peaks = flag_anomalies(fused_signal)
    reference_grid = generate_reference_grid(5)
    
    # Processed signal used in analysis
    processed_signals = [round(x * 1.05, 3) for x in fused_signal]
    
    # Dead code assignments - irrelevant variables
    entropy_metric = compute_entropy(processed_signals)
    validation_hash = validate_integrity([int(x) for x in processed_signals])
    coordinate_map = transform_coordinates(list(range(5, 20, 3))))
    
    # Critical analysis point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output result
    print(f"Result: {final_diagnostic}")