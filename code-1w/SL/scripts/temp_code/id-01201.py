import itertools

# Simulate sensor data stream with noise and valid signals
data_stream = [0.1, 0.4, 1.2, 0.8, 2.3, -0.5, 3.1, 2.7, 0.3, 1.9, 4.0, -1.2, 2.2]

def extract_peaks(sequence, sensitivity=1.0):
    """Extract rising peaks above sensitivity threshold."""
    peaks = []
    for i in range(1, len(sequence)):
        if sequence[i] > sensitivity and sequence[i] > sequence[i-1]:
            peaks.append(sequence[i])
    return peaks

def calculate_entropy(values):
    # Irrelevant helper function - not used in final computation
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Noise filtering using moving average (relevant)
window_size = 3
smoothed = [sum(data_stream[i:i+window_size]) / window_size 
            for i in range(len(data_stream) - window_size + 1)]

# Misleading transformation: FFT-like magnitude (unused red herring)
fake_fft_magnitudes = [abs(x) * 1.5 for x in smoothed if x < 0]

# Extract candidate signals above base threshold (relevant)
candidates = [x for x in smoothed if x > 1.0]

# Secondary filter based on rate of change (relevant)
deltas = [candidates[i+1] - candidates[i] for i in range(len(candidates)-1) if candidates[i] > 1.5]
filtered_data = list(itertools.compress(candidates, [True] + [d > 0 for d in deltas]))

# Auxiliary diagnostic metric (irrelevant)
avg_delta = sum(deltas) / len(deltas) if deltas else 0.0

# Threshold determined by mode approximation (semi-relevant)
mode_proxy = max(set([round(x, 1) for x in filtered_data]), key=[round(x, 1) for x in filtered_data].count)
threshold = mode_proxy * 0.75

# Core processing function
process_signals = lambda sigs, thresh: sum(map(lambda x: int(x / thresh), filter(lambda x: x > thresh, sigs)))

# Critical statement
final_output = process_signals(filtered_data, threshold)

# Debug prints (not affecting logic)
# print(f'Diagnostic: avg_delta={avg_delta}, entropy_est={calculate_entropy(smoothed)}')

print(f'Target result: {final_output}')