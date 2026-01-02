import itertools
from collections import defaultdict, Counter
from math import log, sin, floor

# Simulated sensor data preprocessing with red herrings
def load_sensor_metadata():
    # Irrelevant metadata loading (dead end)
    return {'version': '2.1', 'calibrated': False, 'units': 'mm'}

def parse_raw_stream(raw):
    # Real parsing logic mixed with distractions
    tokens = raw.split(',')
    values = []
    for t in tokens:
        try:
            num = float(t.strip())
            if num > -999:  # Filter invalid readings
                values.append(num)
        except ValueError:
            continue
    return values

def generate_frequency_map(data):
    # Distractor: computes frequencies but not used in final result
    freq = defaultdict(int)
    for d in data:
        freq[int(d)] += 1
    return freq

def compute_entropy(seq):
    # Misleading function - looks important but unused
    counter = Counter(seq)
    total = len(seq)
    entropy = 0.0
    for count in counter.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 6)

def filter_outliers(series, threshold=2.0):
    mean = sum(series) / len(series)
    std = (sum((x - mean) ** 2 for x in series) / len(series)) ** 0.5
    # Only include values within threshold
    filtered = [x for x in series if abs(x - mean) <= threshold * std]
    return filtered

def transform_nonlinear(signal):
    # Apply nonlinear transformation to amplify certain features
    return [round(100 * sin(x / 10) + 0.7 * x, 4) for x in signal]

def rolling_window_stat(data, size=3, stat='avg'):
    # Dead code path — never called in execution
    results = []
    for i in range(len(data) - size + 1):
        window = data[i:i+size]
        if stat == 'avg':
            results.append(sum(window)/size)
        elif stat == 'max':
            results.append(max(window))
    return results

def extract_peaks_and_troughs(ts):
    # Another decoy analysis function
    peaks = []
    troughs = []
    for i in range(1, len(ts)-1):
        if ts[i] > ts[i-1] and ts[i] > ts[i+1]:
            peaks.append(ts[i])
        elif ts[i] < ts[i-1] and ts[i] < ts[i+1]:
            troughs.append(ts[i])
    return peaks, troughs

def aggregate_metrics(dataset):
    # Complex-looking aggregation that feeds into nothing
    metrics = {}
    metrics['count'] = len(dataset)
    metrics['range'] = max(dataset) - min(dataset)
    metrics['skew_hint'] = (3*(sum(dataset)/len(dataset) - min(dataset))) / metrics['range'] if metrics['range'] != 0 else 0
    metrics['density'] = len([x for x in dataset if x > 0]) / len(dataset)
    return metrics

def calculate_intrinsic_dimension(data):
    # Completely irrelevant advanced calculation
    n = len(data)
    if n < 2:
        return 0
    diffs = sorted([abs(data[i] - data[j]) for i in range(n) for j in range(i+1, n)])
    median_diff = diffs[len(diffs)//2]
    return round(log(n) / log(median_diff + 1), 4) if median_diff > 0 else 0

def shift_phase_sequence(seq, phase=1):
    # Unused signal processing transformation
    shifted = [0]*len(seq)
    for i in range(len(seq)):
        shifted[(i + phase) % len(seq)] = seq[i]
    return shifted

def compress_dynamic_range(data, factor=0.5):
    # Looks useful but is a distractor
    mean_val = sum(data) / len(data)
    return [mean_val + factor * (x - mean_val) for x in data]

def analyze_signal(data_chunk):
    # Core actual computation buried in noise
    base_sum = sum(data_chunk)
    weighted = sum(i * val for i, val in enumerate(data_chunk))
    interaction_term = 0
    for a, b in itertools.combinations(data_chunk[:5], 2):  # Use only first 5
        interaction_term += int(a) & int(b)  # Bitwise AND of integer parts
    
    # This is the real formula
    diagnostic_score = base_sum * 2 - weighted + interaction_term
    
    # Multiple misleading intermediate variables
    dummy_normalization = diagnostic_score / (len(data_chunk) or 1)
    adjusted_for_noise = dummy_normalization + 17.3
    final_adjustment_factor = 1.0
    
    # Hidden conditional: only executed if sum exceeds threshold (it does)
    temp_accum = 0
    for v in data_chunk:
        if v > 50:
            temp_accum += 1
    if temp_accum >= 3:
        final_adjustment_factor = 0.9
    
    # Final result influenced by above
    final_diagnostic = int(diagnostic_score * final_adjustment_factor)
    
    # Never reached code branches (dead paths)
    if False:
        fallback = sum(compress_dynamic_range(data_chunk))
        final_diagnostic = int(fallback)
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_input = "12.7,88.3,45.1,103.6,67.2,23.5,91.8,55.4,77.9"
    
    # Irrelevant assignments and computations
    metadata = load_sensor_metadata()
    entropy_value = compute_entropy([1,2,2,3,3,3,4,4,5])
    fake_dimension = calculate_intrinsic_dimension([10,20,30])
    
    # Real processing begins here
    parsed_data = parse_raw_stream(raw_input)
    cleaned_data = filter_outliers(parsed_data, threshold=1.8)
    processed_data = transform_nonlinear(cleaned_data)
    
    # More red herring operations
    freq_map = generate_frequency_map(parsed_data)
    peaks, troughs = extract_peaks_and_troughs(processed_data)
    all_metrics = aggregate_metrics(processed_data)
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")