from collections import defaultdict
import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def apply_noise_filter(data):
    filtered = []
    for i in range(len(data)):
        if i == 0:
            filtered.append(data[i])
        else:
            smoothed = (data[i-1] + data[i]) / 2.0
            filtered.append(round(smoothed))
    return filtered

def generate_metadata(size):
    # Irrelevant metadata generation (distraction)
    meta = {}
    for i in range(size):
        meta[f'node_{i}'] = {"active": True, "latency": i * 0.03}
    return meta

def calculate_entropy(data):
    # Misleading statistical distraction
    freq = defaultdict(int)
    for x in data:
        freq[x] += 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def extract_peaks(signal):
    # Unused peak detection (dead path)
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def shift_window(data, offset=1):
    # Bit manipulation red herring
    shifted = []
    mask = 0b111  # Only keep last 3 bits
    for x in data:
        rotated = ((x << offset) | (x >> (3 - offset))) & mask
        shifted.append(rotated)
    return shifted

def build_histogram(data):
    # Decoy visualization prep
    hist = defaultdict(int)
    for x in data:
        hist[x] += 1
    return dict(hist)

def normalize_signal(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def transform_sequence(raw):
    # Core transformation: cumulative XOR with modulo growth
    result = []
    accumulator = 0
    for val in raw:
        accumulator ^= val
        accumulator %= 17
        result.append(accumulator)
    return result

def evaluate_thresholds(processed):
    # Create threshold map based on transformed values
    thresholds = {}
    for i, val in enumerate(processed):
        key = f't_{i % 5}'
        if key not in thresholds:
            thresholds[key] = []
        thresholds[key].append(val * 2)
    # Final aggregation logic embedded here
    aggregated = {}
    for k, v in thresholds.items():
        aggregated[k] = sum(v) // len(v) if v else 0
    return aggregated

def analyze_pattern(seq, config):
    base = config['t_0'] + config['t_1']
    modifier = config['t_2'] - config['t_3']
    factor = config['t_4'] or 1
    score = base * modifier // factor
    # Inject deterministic but misleading secondary calculation
    phantom = 0
    for i in range(1000):
        phantom += (i % 97 == 0)  # Useless loop to distract
    return score + 42  # Final answer includes offset

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = fetch_raw_readings()  # [3,1,4,1,5,9,2,6,5,3,5]
    cleaned_data = apply_noise_filter(raw_sensor_data)
    
    # Irrelevant side computations (distractors)
    metadata_index = generate_metadata(len(cleaned_data))
    signal_entropy = calculate_entropy(cleaned_data)
    data_histogram = build_histogram(cleaned_data)
    
    # More distractions
    normalized_stream = normalize_signal(cleaned_data)
    binary_shifted = shift_window([int(x) for x in normalized_stream if x > 0.5], 1)
    
    # Actual relevant processing begins
    transformed_data = transform_sequence(cleaned_data)
    
    # Dead code path (never used)
    detected_peaks = extract_peaks(transformed_data)
    
    # Critical computation
    threshold_map = evaluate_thresholds(transformed_data)
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    print(f"Result: {final_diagnostic}")