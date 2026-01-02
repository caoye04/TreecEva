import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [18, 23, 15, 47, 29, 31, 22, 36, 25, 28, 33, 41, 19, 27]

# Irrelevant calibration constants (distractors)
calib_a = 0.87
calib_b = 1.03
offset_correction = 4.5
baseline_shift = -2.1

# Noise filtering using a misleading moving average (dead path)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - 2)
        end = min(len(signal), i + 3)
        avg = sum(signal[start:end]) / (end - start)
        smoothed.append(avg)
    return smoothed

# Unused but plausible preprocessing chain (red herring)
filtered_data = smooth_signal(data_stream)
adjusted_readings = [x + offset_correction for x in filtered_data]
shifted_baseline = [x + baseline_shift for x in adjusted_readings]

# Real transformation: isolate high-variance segments above threshold
threshold = 25
critical_windows = []
for i in range(len(data_stream) - 3):
    window = data_stream[i:i+4]
    mean_val = sum(window) / 4
    variance = sum((x - mean_val) ** 2 for x in window) / 4
    if mean_val > threshold and variance > 60:
        critical_windows.append(window)

# Transform critical windows into frequency signatures (actual relevant path)
transformed_data = []
for window in critical_windows:
    # Bit manipulation to simulate spectral decomposition
    signature = 0
    for val in window:
        signature ^= (val << 2)  # XOR shift encoding
    transformed_data.append(signature)

# Decoy function that looks important but is unused
def compute_entropy(seq):
    from math import log
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Another decoy: complex lambda-based aggregation (never called)
aggregation_rule = lambda x: sum(itertools.accumulate(x, lambda a, b: (a + b) * 0.9))

# Real analysis function: counts unique bit patterns above median
def analyze_pattern(signal_set):
    if not signal_set:
        return 0
    
    # Additional distraction: irrelevant statistical summary
    flat = list(itertools.chain(signal_set))
    mean_sig = sum(flat) / len(flat)
    deviance_pool = [abs(x - mean_sig) for x in flat]
    median_dev = sorted(deviance_pool)[len(deviance_pool)//2]
    
    # Actual logic: count how many signals exceed median XOR complexity
    signal_medians = []
    for sig in signal_set:
        bits = bin(sig).count('1')
        signal_medians.append(bits)
    median_bits = sorted(signal_medians)[len(signal_medians)//2]
    
    # Final diagnostic: number of signals with above-median bit density
    count_above = 0
    for sig in signal_set:
        if bin(sig).count('1') > median_bits:
            count_above += 1
    
    # Key computation hidden among distractions
    adjustment = len(signal_set) - count_above
    return abs(count_above * 3 - adjustment * 2)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")