from collections import defaultdict, Counter
import math

# Simulated sensor data collection with noise and redundancy
def acquire_signal(readings):
    signal_cache = defaultdict(float)
    noise_profile = [0.1, -0.2, 0.3, -0.1, 0.05]
    processed = []
    for i, val in enumerate(readings):
        if i % 4 == 0:
            val += noise_profile[i % len(noise_profile)]
        if val < 0:
            val = abs(val)
        signal_cache[f'entry_{i}'] = round(val * 1.02, 3)
        processed.append(val)
    return processed

# Legacy function - unused but looks relevant
def deprecated_normalization(x):
    return [v / max(x) for v in x]  # Dead path

# Advanced filtering using outlier suppression
def filter_outliers(data, threshold=2.0):
    count_freq = Counter(data)
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    
    # Distractor: spurious entropy calculation
    entropy = 0.0
    for k, freq in count_freq.items():
        prob = freq / len(data)
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return filtered

# Data fusion from multiple channels
def merge_channels(primary, secondary):
    fused = []
    for a, b in zip(primary, secondary):
        fused.append((a * 0.7) + (b * 0.3))
    return fused

# Check system integrity via checksum-like mechanism
def validate_integrity(sequence):
    checksum = 0
    for i, x in enumerate(sequence):
        checksum ^= int(x * 100) + i  # Bitwise distraction
    return checksum % 1000 == 42  # Rare condition, usually false

# Final computation with physical model approximation
def finalize_measurement(dataset, factor):
    temp_series = [math.sin(x / 10) + math.log(x + 1) for x in dataset]
    adjusted = [t * factor for t in temp_series]
    base_energy = sum(adjusted) / len(adjusted)
    
    # Critical nonlinear correction
    if base_energy > 5:
        base_energy = base_energy ** 0.9
    else:
        base_energy = base_energy ** 1.05
    
    # Red herring: unused transformation chain
    transformed = []
    for t in temp_series:
        if t > 1.0:
            transformed.append(t // 0.5)
        elif t > 0.5:
            transformed.append(t * 2)
        else:
            transformed.append(abs(t))
    
    # Actual result
    thermal_capacity = int(round(base_energy * 1000))
    return thermal_capacity

# Main execution sequence
if __name__ == '__main__':
    raw_readings = [12.1, 15.3, 9.8, 14.2, 16.7, 8.9, 13.4, 15.6, 10.1, 14.8]
    calib_factor = 1.08
    
    # Irrelevant preprocessing steps
    normalized = [x / 10 for x in raw_readings]
    scaled_copy = [x * 2.1 for x in normalized]
    
    acquired = acquire_signal(raw_readings)
    cleaned = filter_outliers(acquired, threshold=1.8)
    
    auxiliary_stream = [11.9, 15.1, 10.2, 14.0, 16.5, 9.1, 13.2, 15.4, 10.3, 14.6]
    refined = merge_channels(cleaned, auxiliary_stream[:len(cleaned)])
    
    # Spurious validation check (not used)
    is_valid = validate_integrity(refined)
    
    # Key statement
    thermal_capacity = finalize_measurement(refined, calib_factor)
    
    # Output the target result
    print(f"Result: {thermal_capacity}")