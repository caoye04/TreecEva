import itertools

# Simulate sensor data with noise and valid signals
def generate_data_stream():
    raw_values = [x * 0.5 for x in range(20)]
    noise_layer = [(i % 3 - 1) * 0.1 for i in range(20)]
    return [raw_values[i] + noise_layer[i] for i in range(20)]

data_stream = generate_data_stream()

# Irrelevant helper: computes statistical moments (not used in final path)
def compute_moments(series):
    mean = sum(series) / len(series)
    variance = sum((x - mean) ** 2 for x in series) / len(series)
    skewness = sum((x - mean) ** 3 for x in series) / (len(series) * (variance ** 1.5))
    kurtosis = sum((x - mean) ** 4 for x in series) / (len(series) * (variance ** 2)) - 3
    return {'mean': mean, 'variance': variance, 'skewness': skewness, 'kurtosis': kurtosis}

# Distractor function: operates on unrelated data structure
def analyze_frequency_distribution(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

# Unused transformation chain (red herring)
transform_history = []
def legacy_filter(x):
    if x < 0:
        return 0
    result = x ** 0.5
    transform_history.append(result)
    return result

# Real processing begins here — but buried under distractions
def apply_window_mask(signal, window_size=4):
    masked = []
    for i in range(0, len(signal), window_size):
        segment = signal[i:i + window_size]
        if len(segment) == window_size:
            # Apply Hann window approximation
            weights = [0.5 * (1 - (-1)**j) for j in range(window_size)]  # Simplified
            weighted = [segment[j] * (0.5 - 0.5 * (-1)**j) for j in range(window_size)]
            masked.extend(weighted)
    return masked

# Core logic hidden among decoys
def extract_peaks(series):
    peaks = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            peaks.append(series[i])
    return peaks

# Bit manipulation red herring (never called)
def scramble_bits(n):
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    return n ^ 0xFFFFFFFF

def decode_sequence(num_list):
    binary_accum = 0
    for num in num_list:
        if num > 0.5:
            binary_accum = (binary_accum << 1) | 1
        else:
            binary_accum = (binary_accum << 1)
    return binary_accum % 1000  # Truncate to manageable size

# Real pipeline — but hard to trace due to noise
def process_transformations(stream):
    # Step 1: Masking with window function
    masked_signal = apply_window_mask(stream)
    
    # Step 2: Find local maxima (peaks)
    candidate_peaks = extract_peaks(masked_signal)
    
    # Step 3: Filter peaks above threshold
    significant_peaks = [p for p in candidate_peaks if p > 0.7]
    
    # Step 4: Accumulate using dictionary-based frequency count (relevant)
    peak_count = {}
    for pk in significant_peaks:
        rounded = round(pk, 1)
        peak_count[rounded] = peak_count.get(rounded, 0) + 1
    
    # Step 5: Use itertools to group by value (only counts matter)
    sorted_peaks = sorted(peak_count.keys())
    grouped = {k: list(g) for k, g in itertools.groupby(sorted_peaks, key=lambda x: x)}
    
    # Step 6: Compute final metric: sum of peak values weighted by occurrence
    total_weight = 0.0
    for val, count in peak_count.items():
        total_weight += val * count
    
    # Step 7: Transform through unused bit path (but only conceptually — skip)
    # Note: scramble_bits is not applied; this is a distraction
    
    # Step 8: Final adjustment using combinatorics (sum over combinations of 2)
    if len(significant_peaks) >= 2:
        pairs = list(itertools.combinations(significant_peaks, 2))
        pair_sum = sum(abs(a - b) for a, b in pairs) / len(pairs) if pairs else 0
        total_weight += pair_sum * 0.1
    
    return round(total_weight, 6)

# Dead code path — looks important but unused
class DataProcessor:
    def __init__(self, buffer):
        self.buffer = buffer
        self.checksum = sum(int(x * 10) for x in buffer) % 100
    
    def validate_integrity(self):
        return self.checksum % 7 == 0

# Another red herring: complex dictionary flattening
nested_metrics = {
    'stage1': {'a': 1, 'b': 2},
    'stage2': {'c': {'x': 3}, 'd': 4}
}
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Actual execution buried in middle of noise
final_output = process_transformations(data_stream)

# Print result as required
print(f"Result: {final_output}")