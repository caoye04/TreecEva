from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def generate_pattern_sequence(length, seed=42):
    # Irrelevant helper function - dead code path
    return [((i * seed) % 37) ^ (i % 5) for i in range(length)]

def apply_noise_filter(raw_data, level=3):
    # Distractor: complex-looking but unused filtering logic
    filtered = []
    for x in raw_data:
        if x & 1:
            filtered.append(x ^ (level << 1))
        else:
            filtered.append(x)
    return filtered

def compute_checksum(data):
    # Misleading intermediate computation
    chk = 0
    for val in data:
        chk = (chk + val * 31) % 997
    return chk

def rolling_window_avg(seq, size=3):
    # Unused advanced transformation
    if len(seq) < size:
        return []
    avgs = []
    for i in range(len(seq) - size + 1):
        avgs.append(sum(seq[i:i+size]) / size)
    return avgs

def evaluate_stability_metric(signal):
    # Red herring function that computes something irrelevant
    variance = sum((x - sum(signal)/len(signal))**2 for x in signal) / len(signal)
    return round(variance, 4)

def extract_features(data_stream):
    # Complex feature extraction with decoy outputs
    features = defaultdict(int)
    temp_flags = [0] * len(data_stream)
    
    for idx, val in enumerate(data_stream):
        features['peak_count'] += (val > 25)
        features['edge_case'] += ((val & (val - 1)) == 0)  # power of two
        features['modulo_cluster'] += (val % 7 == 0)
        
        # Bit manipulation distraction
        if val > 0:
            temp_flags[idx] = (val ^ (val >> 2)) & 3
    
    # Decoy aggregation
    features['flag_entropy'] = sum(f * f for f in temp_flags)
    return dict(features)

def analyze_signal(buffer, threshold):
    # Core logic embedded within distractions
    stats = Counter()
    
    # Key slicing operation (required)
    segment = buffer[5:15]
    
    # Relevant conditional logic chain
    for num in segment:
        if num < threshold:
            stats['low'] += 1
        elif num > threshold * 2:
            stats['high'] += 1
        else:
            stats['medium'] += 1
    
    # Critical bitwise and arithmetic combination
    base_score = (stats['medium'] << 2) + (stats['low'] ^ stats['high'])
    adjustment = len(segment) % 4
    
    # Final relevant calculation
    if base_score > threshold:
        result = (base_score * 3) - (adjustment * 5)
    else:
        result = (base_score * 2) + (adjustment * 3)
    
    # One more layer of logic
    if stats['high'] == 0 and stats['low'] > 2:
        result = result ^ 17  # XOR adjustment
    
    return result

# Main execution block
if __name__ == "__main__":
    # Initialize sensor input (deterministic)
    sensor_readings = [12, 15, 8, 33, 21, 9, 26, 14, 11, 38, 24, 7, 19, 31, 13, 42, 18]
    
    # Irrelevant transformations (distractions)
    noise_filtered = apply_noise_filter(sensor_readings, level=5)
    checksum = compute_checksum(sensor_readings)
    stability = evaluate_stability_metric(noise_filtered)
    window_avgs = rolling_window_avg(sensor_readings, size=4)
    
    # Feature extraction (decoy analysis)
    extracted_feats = extract_features(sensor_readings)
    
    # Variable assignments with meaningful names
    pattern_buffer = sensor_readings.copy()
    calibration_offset = 7
    filter_threshold = 15 + calibration_offset  # evaluates to 22
    debug_mode = False
    
    # Key statement containing the answer
    final_diagnostic = analyze_signal(pattern_buffer, filter_threshold)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")