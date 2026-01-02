import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration_ms, sample_rate):
    return [int(50 * math.sin(i * 0.1) + 25) for i in range(0, int(duration_ms / sample_rate))]

def apply_noise_filter(raw_samples, strength=0.9):
    filtered = []
    for i in range(len(raw_samples)):
        neighbor_avg = 0
        count = 0
        for j in [-1, 0, 1]:
            if 0 <= i + j < len(raw_samples):
                neighbor_avg += raw_samples[i + j]
                count += 1
        filtered.append(int((raw_samples[i] * strength) + (neighbor_avg / count) * (1 - strength)))
    return filtered

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_checksum(sequence):
    # Irrelevant cryptographic checksum (distractor)
    chk = 0
    for val in sequence:
        chk = (chk * 31 + val) % 65537
    return chk

def evaluate_stability_metric(signal):
    # Misleading stability metric (dead-end computation)
    diffs = [abs(signal[i] - signal[i-1]) for i in range(1, len(signal))]
    return sum(diffs) / len(diffs) if diffs else 0

def extract_peaks(data, min_magnitude=30):
    # Unused peak detection (red herring function)
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > min_magnitude and data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append((i, data[i]))
    return peaks

def build_frequency_bands(signal):
    # Distractor: frequency band energy calculation
    bands = {'low': 0, 'mid': 0, 'high': 0}
    avg = sum(signal) / len(signal)
    for val in signal:
        diff = abs(val - avg)
        if diff < 10:
            bands['low'] += 1
        elif diff < 20:
            bands['mid'] += 1
        else:
            bands['high'] += 1
    return bands

def normalize_range(data):
    if not data:
        return []
    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        return [0] * len(data)
    return [round((x - min_val) / (max_val - min_val) * 100) for x in data]

def classify_pattern(normalized):
    # Complex pattern classification with nested conditions
    if len(normalized) < 5:
        return 'insufficient'
    rising = sum(1 for i in range(1, len(normalized)) if normalized[i] > normalized[i-1])
    falling = sum(1 for i in range(1, len(normalized)) if normalized[i] < normalized[i-1])
    stable = sum(1 for i in range(1, len(normalized)) if normalized[i] == normalized[i-1])
    total_transitions = rising + falling + stable
    
    if total_transitions == 0:
        return 'flat'
    
    rising_ratio = rising / total_transitions
    falling_ratio = falling / total_transitions
    
    if rising_ratio > 0.7:
        return 'ascending'
    elif falling_ratio > 0.7:
        return 'descending'
    elif rising_ratio > 0.4 and falling_ratio > 0.4:
        return 'oscillatory'
    else:
        return 'irregular'

def analyze_signal(data, thresholds):
    base_metric = sum(x ** 0.5 for x in data if x > 0)  # Core calculation component
    adjustment_factor = 0
    pattern = classify_pattern(data)
    
    if pattern == 'ascending':
        adjustment_factor = thresholds['alpha']
    elif pattern == 'descending':
        adjustment_factor = thresholds['beta']
    elif pattern == 'oscillatory':
        adjustment_factor = thresholds['gamma']
    else:
        adjustment_factor = thresholds['delta']
    
    intermediate = base_metric * adjustment_factor
    
    # Secondary transformation using bit manipulation (non-obvious but relevant)
    shifted = int(intermediate) ^ 0xAA  # XOR with magic number
    adjusted_shift = (shifted << 2) >> 1  # Left shift by 2, then right logical shift by 1
    
    # Final nonlinear transformation
    final_score = math.cos(math.radians(adjusted_shift % 180)) * adjusted_shift
    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    # Generate initial sensor readings
    raw_sensor_data = collect_samples(500, 50)
    
    # Apply primary filtering
    cleaned_signal = apply_noise_filter(raw_sensor_data)
    
    # Compute irrelevant diagnostics (distractors)
    signal_checksum = generate_checksum(cleaned_signal)
    stability_index = evaluate_stability_metric(cleaned_signal)
    peak_analysis = extract_peaks(cleaned_signal, min_magnitude=20)
    frequency_profile = build_frequency_bands(cleaned_signal)
    entropy_value = compute_entropy(cleaned_signal)
    
    # Normalize for pattern analysis
    normalized_readings = normalize_range(cleaned_signal)
    
    # Define threshold map for analysis (critical parameter set)
    threshold_map = {
        'alpha': 1.8,
        'beta': 0.9,
        'gamma': 2.1,
        'delta': 1.2
    }
    
    # Processed data used in key statement
    processed_data = [x + 1 for x in normalized_readings]  # Minor adjustment
    
    # --- KEY EXECUTION POINT ---
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")