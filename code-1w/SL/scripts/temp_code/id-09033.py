import math

# Simulated sensor data processing with diagnostic pipeline
def collect_sensor_readings():
    raw_samples = [i * 0.5 + (i % 7) for i in range(100)]
    offset = sum(raw_samples) / len(raw_samples)
    normalized = [x - offset for x in raw_samples]
    return normalized

# Irrelevant auxiliary function – decoy
def compute_entropy(data):
    freq_map = {}
    total = len(data)
    for x in data:
        key = int(x * 10) % 5
        freq_map[key] = freq_map.get(key, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

# Signal filtering – relevant
def filter_noise(signal):
    filtered = []
    for i in range(2, len(signal) - 2):
        window = signal[i-2:i+3]
        sorted_window = sorted(window)
        median_val = sorted_window[2]
        filtered.append(median_val)
    return filtered[::2]  # Decimate by 2

# Data transformation with distractors
def extract_features(signal_chunk):
    magnitude = sum(abs(x) for x in signal_chunk)
    variance = sum((x - magnitude/len(signal_chunk))**2 for x in signal_chunk)
    peak_to_peak = max(signal_chunk) - min(signal_chunk)
    
    # Distractor computations
    dummy_sum = 0
    for x in signal_chunk:
        if x > 1.0:
            dummy_sum += int(x) ** 2
    temp_cache = {i: dummy_sum * i for i in range(3)}  # Unused dict
    
    return {
        'mag': magnitude,
        'var': variance,
        'pp': peak_to_peak,
        'count_high': len([x for x in signal_chunk if x > 0.5])
    }

# Red herring function – never called
def predict_failure_trend(features_list):
    trend_score = 0
    for features in features_list[-10:]:
        trend_score += features['var'] * 1.5
    return trend_score / 10 if features_list else 0

# Core analysis – relevant
def analyze_signal(dataset):
    stats_log = []  # Logged but mostly unused
    
    for i in range(0, len(dataset), 15):
        segment = dataset[i:i+15]
        if len(segment) < 5:
            continue
            
        # Real computation path
        transposed = [x * 1.8 + 32 for x in segment]  # To Fahrenheit (distractor context)
        clean_seg = [x for x in segment if abs(x) > 0.1]
        
        # Actual feature extraction
        feats = extract_features(clean_seg)
        
        # Key metric embedded in logic
        quality_metric = int(feats['mag'] * 10) % 1000
        adjustment = len(clean_seg) // 3
        intermediate = (quality_metric + adjustment) * 7
        
        # Dead branch – misleading
        if intermediate > 10000:
            intermediate = intermediate ^ 255
        elif intermediate < 100:
            intermediate = ~intermediate
        
        stats_log.append(intermediate)
    
    # Final calculation from accumulated log
    valid_entries = [x for x in stats_log if x > 0]
    if not valid_entries:
        return -1
        
    avg_intermediate = sum(valid_entries) / len(valid_entries)
    final_diagnostic = int(avg_intermediate + (valid_entries[-1] % 19))
    
    # DEAD CODE PATHS BELOW
    shadow_buffer = [0]*100
    for idx in range(len(shadow_buffer)):
        shadow_buffer[idx] = (idx * 17) % 251
    checksum = sum(shadow_buffer[i] for i in [10, 20, 30])  # Never used
    
    return final_diagnostic

# Orchestration
if __name__ == '__main__':
    raw_data = collect_sensor_readings()
    processed_data = filter_noise(raw_data)
    
    # Unused operations – red herrings
    sample_slice = raw_data[10:50:3]
    reversed_view = raw_data[::-1]
    slice_entropy = compute_entropy(sample_slice)
    
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")