from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition
def acquire_signal():
    raw_samples = [i * 0.1 for i in range(100)]
    noise_floor = [0.05 * math.sin(x) for x in raw_samples]
    return [math.cos(x) + noise + 0.02 * math.sin(5 * x) for x, noise in zip(raw_samples, noise_floor)]

# Irrelevant auxiliary function – dead code path
def deprecated_filter_chain(signal):
    temp_buffer = []
    for x in signal:
        if x > 0.5:
            temp_buffer.append(x * 0.9)
    return temp_buffer

# Unused transformation
def frequency_shift(signal, factor=2.0):
    return [math.sin(factor * math.asin(max(-0.99, min(0.99, x)))) for x in signal]

# Signal preprocessing with red herring steps
def preprocess_signal(data):
    window_size = 5
    smoothed = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i+window_size]
        avg = sum(segment) / window_size
        smoothed.append(avg)
    
    # Distractor: irrelevant statistical measures
    mean_val = sum(smoothed) / len(smoothed)
    variance = sum((x - mean_val) ** 2 for x in smoothed) / len(smoothed)
    peak_to_peak = max(smoothed) - min(smoothed)
    
    # Actual relevant transformation
    normalized = [(x - mean_val) / (variance ** 0.5 + 1e-8) for x in smoothed]
    
    # More distractions: unused metrics
    zero_crossings = sum((normalized[i] * normalized[i+1]) < 0 for i in range(len(normalized)-1))
    energy = sum(x**2 for x in normalized)
    
    return normalized

# Core analysis logic
def compute_entropy(values):
    count_map = Counter()
    for v in values:
        bin_id = int((v + 3.0) * 10)  # Normalize to bins (-3 to +3 -> 60 bins)
        count_map[bin_id] += 1
    total = len(values)
    entropy = 0.0
    for count in count_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Misleading intermediate diagnostic
def legacy_diagnostic(signal_chunk):
    score = 0
    for x in signal_chunk:
        if abs(x) > 0.7:
            score += 1.5
        elif abs(x) > 0.3:
            score += 0.5
    return score * 0.1

# Main analysis pipeline
def analyze_signal(cleaned_signal):
    # Extract key features
    amplitude_modulation = [abs(cleaned_signal[i+1] - cleaned_signal[i]) for i in range(len(cleaned_signal)-1)]
    high_freq_component = [a*b for a,b in zip(amplitude_modulation[::2], amplitude_modulation[1::2])] 
    
    # Red herring: complex but unused structure
    feature_matrix = defaultdict(lambda: defaultdict(float))
    for idx, val in enumerate(amplitude_modulation):
        sector = idx // 10
        feature_matrix[sector]['sum'] += val
        feature_matrix[sector]['max'] = max(feature_matrix[sector]['max'], val)
        feature_matrix[sector]['count'] += 1
    
    # Unused recursive helper
    def integrate_recursive(arr, depth=0):
        if depth >= 3 or len(arr) <= 1:
            return arr[0] if arr else 0
        return arr[0] + 0.5 * integrate_recursive(arr[1:], depth+1)
    
    # Real computation begins here
    entropy_measure = compute_entropy(cleaned_signal)
    modulation_entropy = compute_entropy([round(x, 3) for x in amplitude_modulation])
    
    # Critical decision logic with nesting
    if entropy_measure > 3.0:
        if modulation_entropy > 2.0:
            base_rating = 85
        else:
            base_rating = 60
    else:
        if modulation_entropy > 2.5:
            base_rating = 70
        else:
            base_rating = 45
    
    # Final adjustment using list comprehension and set logic
    significant_peaks = {i for i, x in enumerate(cleaned_signal) if x > 1.5}
    suppression_zones = {i for i, x in enumerate(cleaned_signal) if x < -1.5}
    interference_count = len(significant_peaks.intersection(suppression_zones))
    
    adjustment_factor = len([x for x in amplitude_modulation if x > 0.4]) // 10
    
    # Final diagnostic score
    final_rating = base_rating + adjustment_factor * 5 - interference_count * 10
    
    # Decoy assignment
    temp_result = legacy_diagnostic(cleaned_signal[:20])
    
    # Actual answer carrier
    final_diagnostic = int(final_rating)
    return final_diagnostic

# Orchestration
if __name__ == '__main__':
    raw_data = acquire_signal()
    processed_data = preprocess_signal(raw_data)
    final_diagnostic = analyze_signal(processed_data)
    print(f"Target result: {final_diagnostic}")