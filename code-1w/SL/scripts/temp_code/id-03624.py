import math

# Simulated sensor data preprocessing with multiple distractors
def fetch_raw_readings():
    return [127, 255, 89, 150, 200, 64, 180, 95]

def calibrate_sensor(x, factor=1.05):
    return int(x * factor) if x > 100 else int(x * 1.01)

def compute_checksum(data):
    # Irrelevant checksum function (not used in final result)
    return sum(data) % 256

def filter_outliers(data, limit=200):
    return [x for x in data if x <= limit]

def enhance_resolution(data):
    # Bit manipulation to simulate resolution boost (some relevant)
    return [(x << 2) & 0xFF for x in data]

def derive_temporal_weights(n):
    # Dead code path — not used
    return [math.sin(i * 0.5) + 1 for i in range(n)]

def generate_frequency_bins(data):
    # Distractor: creates unused frequency analysis
    bins = [0] * 4
    for x in data:
        bins[x // 64] += 1
    return bins

def normalize_signal(data):
    max_val = max(data)
    return [round(x / max_val * 255) for x in data] if max_val > 0 else data

def build_threshold_map(config_level):
    # Complex but meaningful configuration map
    base = {'low': 100, 'mid': 150, 'high': 200}
    adj = {'low': 0.9, 'mid': 1.0, 'high': 1.2}[config_level]
    return {k: int(v * adj) for k, v in base.items()}

def evaluate_stability_index(seq):
    # Decoy function: calculates stability but unused
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 2) if diffs else 0

def preprocess_segment(segment, mode='aggressive'):
    # Multi-step processing with conditional logic
    temp = [calibrate_sensor(x) for x in segment]
    
    if mode == 'conservative':
        temp = [x for x in temp if x > 50]
    else:
        temp = [x + 5 for x in temp]  # Minor boost
    
    temp = filter_outliers(temp)
    temp = normalize_signal(temp)
    extended = enhance_resolution(temp)
    
    # Early return red herring
    if sum(extended) < 500:
        return [0] * 8
    
    # Real processing continues
    return [max(0, min(x, 255)) for x in extended]  # Clamp values

def analyze_signal(data, thresholds):
    # Core analysis logic
    count_mid = sum(1 for x in data if thresholds['low'] <= x < thresholds['mid'])
    count_high = sum(1 for x in data if x >= thresholds['mid'])
    score = count_mid * 1.5 + count_high * 2.5
    
    # Conditional expression used as required
    adjustment = 1.1 if count_high > count_mid else 0.9
    
    # Final diagnostic calculation
    return int(score * adjustment)

# Main execution flow
if __name__ == "__main__":
    raw_data = fetch_raw_readings()
    
    # Irrelevant temporal weight array (dead assignment)
    weights = derive_temporal_weights(len(raw_data))
    
    # Real processing begins
    calibrated = [calibrate_sensor(x) for x in raw_data]
    processed = preprocess_segment(calibrated, mode='aggressive')
    
    # Unused frequency binning (distractor)
    freq_bins = generate_frequency_bins(processed)
    
    # Stability index computed but not used (misleading intermediate)
    stability = evaluate_stability_index(processed)
    
    # Threshold map is actually used
    threshold_map = build_threshold_map('high')
    
    # Key statement: final diagnostic computation
    final_diagnostic = analyze_signal(processed, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")