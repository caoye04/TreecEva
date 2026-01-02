import itertools

# Simulated sensor data processing pipeline with red herrings
def fetch_raw_sensors():
    return [127, 85, 191, 43, 213]

def apply_mask(data, mask=0x1F):
    # Only lower 5 bits are valid due to hardware constraints
    return [d & mask for d in data]

def calculate_checksum(seq):
    # Irrelevant checksum for deprecated protocol
    return sum(seq) % 256

def legacy_calibrate(x):
    # Obsolete calibration curve, not used in current path
    return int(x * 0.87 + 2.1)

def evaluate_thresholds(values, t_low=15, t_high=25):
    # Dead code path — thresholds changed in v3
    counts = {'low': 0, 'high': 0}
    for v in values:
        if v < t_low:
            counts['low'] += 1
        elif v > t_high:
            counts['high'] += 1
    return counts

def transform_signal(x, factor=1.25, offset=3.7):
    # Main transformation function (used)
    return x * factor + offset

def pack_into_frame(data_list):
    # Misleading frame packaging (not used in result)
    return bytes([len(data_list)] + data_list)

def extract_valid_windows(sequence, window_size=3):
    # Generates sliding windows but only one is actually processed
    return list(itertools.sliding_window(sequence, window_size)) if hasattr(itertools, 'sliding_window') else [sequence[i:i+window_size] for i in range(len(sequence)-window_size+1)]

def filter_anomalies(windows):
    # Removes windows where any value exceeds 30 (distraction)
    return [w for w in windows if all(v <= 30 for v in w)]

def compute_entropy(values):
    # Unused advanced metric
    from math import log2
    if not values:
        return 0.0
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    return -sum((count/total) * log2(count/total) for count in freq.values())

def process_transformed_data(data, cfg):
    base_shift = cfg.get('base_shift', 0)
    multiplier = cfg.get('multiplier', 1)
    temp_result = 0
    for idx, val in enumerate(data):
        if idx % 2 == 0:
            # Every even index contributes positively
            temp_result += (val + base_shift) * multiplier
        else:
            # Odd indices are XOR-masked due to firmware quirk
            temp_result -= int(val ^ 0x0F)
    return int(abs(temp_result))

# Entry point
if __name__ == "__main__":
    raw_values = fetch_raw_sensors()  # [127,85,191,43,213]
    masked_data = apply_mask(raw_values)  # Apply bit mask -> [31,21,31,11,21]
    
    # Irrelevant legacy path
    calibrated = [legacy_calibrate(v) for v in raw_values]
    chksum = calculate_checksum(masked_data)
    
    # Transform each value using correct signal model
    transformed_data = [transform_signal(v) for v in masked_data]  # float values
    
    # Round to nearest integer for digital processing
    transformed_data = [round(x) for x in transformed_data]  # [42, 30, 42, 17, 30]
    
    # Create sliding windows (but unused)
    windows = extract_valid_windows(transformed_data, 2)
    clean_windows = filter_anomalies(windows)  # This will be empty due to values >30
    
    # Configuration dict with decoy keys
    config = {
        'base_shift': 5,
        'multiplier': 3,
        'debug_mode': True,
        'version': '3.1.0',
        'checksum': chksum,
        'window_count': len(windows)
    }
    
    # Critical execution point
    final_output = process_transformed_data(transformed_data, config)
    
    # Print result as required
    print(f"Result: {final_output}")