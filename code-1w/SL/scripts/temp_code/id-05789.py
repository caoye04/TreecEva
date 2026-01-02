from collections import defaultdict
import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [14, 19, 24, 17, 28, 31, 13, 22]
    offset = 5
    adjusted = [x - offset for x in raw_samples]
    return adjusted

def compute_baseline(readings):
    total = 0
    count = 0
    for val in readings:
        if val > 10:
            total += val
            count += 1
    return total / count if count else 0

def generate_frequency_map(data):
    # Irrelevant function - simulates signal harmonics but not used in final result
    freq_map = defaultdict(int)
    for d in data:
        freq_map[d % 7] += 1
    return freq_map

def encrypt_sequence(seq):
    # Dead code path - looks important but unused
    encrypted = []
    for i, s in enumerate(seq):
        encrypted.append((s ^ 24) + i)
    return encrypted

def build_threshold_map(baseline):
    # Creates mapping of sensitivity levels based on baseline
    t_map = {}
    levels = ['low', 'mid', 'high']
    factors = [0.85, 1.12, 1.45]
    for l, f in zip(levels, factors):
        t_map[l] = round(baseline * f, 3)
    
    # Decoy entries
    t_map['debug_mode'] = 999
    t_map['override_flag'] = True
    return t_map

def extract_features(signal):
    # Feature engineering with distractors
    features = {
        'peak': max(signal),
        'trough': min(signal),
        'range': max(signal) - min(signal),
        'median_guess': signal[len(signal)//2],
        'checksum': sum(x * (i+1) for i, x in enumerate(signal)) % 1000
    }
    
    # Red herring computations
    temp_buffer = [math.sin(x/10) for x in signal]
    avg_sin = sum(temp_buffer) / len(temp_buffer)
    features['sin_proxy'] = round(avg_sin, 4)
    
    return features

def validate_integrity(features, t_map):
    # Misleading validation logic that appears critical but isn't directly used
    flags = []
    if features['peak'] > t_map['high']:
        flags.append('OVERPEAK')
    if features['trough'] < t_map['low'] * 0.5:
        flags.append('UNDERFLOW')
    if features['checksum'] in [456, 789, 123]:
        flags.append('CHECKSUM_MATCH')
    return len(flags) > 0

def analyze_signal(signal, thresholds):
    # Core analysis with key computation buried in distractions
    
    # Real feature extraction
    feat = extract_features(signal)
    
    # Irrelevant transformation chain
    transformed = []
    for x in signal:
        temp_val = (x << 2) ^ 15
        temp_val = temp_val >> 1
        transformed.append(temp_val)
    
    # Dummy counter object
    stat_counter = defaultdict(int)
    for t in transformed:
        stat_counter[t % 5] += 1
    
    # Key logic hidden among noise
    reference = thresholds['mid']
    deviation = abs(feat['peak'] - reference)
    tolerance = thresholds['high'] - thresholds['low']
    
    # Secondary signal analysis
    sorted_sig = sorted(signal)
    mid_index = len(sorted_sig) // 2
    median_val = (sorted_sig[mid_index] + sorted_sig[~mid_index]) / 2
    
    # Actual answer computation - subtle and non-obvious
    quality_score = 0
    if feat['range'] > tolerance:
        quality_score += 150
    if median_val > reference:
        quality_score += 88
    if feat['peak'] < thresholds['high']:
        quality_score += 44
    
    # Final diagnostic derived from multiple indirect factors
    final_diagnostic = int((quality_score * 1.75) - (deviation * 2.1))
    
    # More red herrings
    debug_payload = f"DIAG:{final_diagnostic^24}", "ENC_MODE_OFF"
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect sensor data
    samples = collect_sensor_readings()  # [9, 14, 19, 12, 23, 26, 8, 17]
    
    # Step 2: Compute baseline for scaling
    base_level = compute_baseline(samples)  # Only values >10: 14,19,12,23,26,17 -> sum=111, count=6 -> 18.5
    
    # Step 3: Build threshold sensitivity map
    threshold_map = build_threshold_map(base_level)
    
    # Step 4: Prepare pattern buffer (just a copy with name change)
    pattern_buffer = [x for x in samples]
    
    # Step 5: Generate unused frequency profile (distractor)
    freq_analysis = generate_frequency_map(pattern_buffer)
    
    # Step 6: Attempt encryption (dead code)
    cipher_data = encrypt_sequence(pattern_buffer)
    
    # Step 7: Extract real features (used later)
    extracted_features = extract_features(pattern_buffer)
    
    # Step 8: Run integrity check (looks important, doesn't affect output)
    is_compromised = validate_integrity(extracted_features, threshold_map)
    
    # Step 9: Perform final diagnostic analysis (key statement)
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")