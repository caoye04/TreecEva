import math

# Simulated sensor data processing with embedded logic distractions
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Irrelevant signal smoothing (dead path)
smoothed = list(map(lambda x: round(x * 0.9 + 0.5), data_stream))

# Core transformation: extract peaks and apply logarithmic scaling
def find_peaks(seq):
    peaks = []
    for i in range(1, len(seq) - 1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            peaks.append(seq[i])
    return peaks

# Distractor: frequency analysis (unused)
def dominant_frequency(signal):
    counts = {}
    for s in signal:
        counts[s] = counts.get(s, 0) + 1
    return max(counts.values())

# Misleading entropy calculation (never called)
calc_entropy = lambda vals: sum(-v/len(vals)*math.log(v/len(vals)) for v in vals if v > 0)

# Real processing chain
raw_peaks = find_peaks(data_stream)

# Apply log only to values > 1 to avoid domain error
logged_peaks = [math.log(p) for p in raw_peaks if p > 1]

# Transform via cumulative summation with offset
accumulated = 0
transformed_data = []
for val in logged_peaks:
    accumulated += val
    transformed_data.append(round(accumulated, 3))

# Dead code: hypothetical FFT simulation (irrelevant)
fft_magnitudes = [abs(transformed_data[0] - transformed_data[-1])] * 3

# Another red herring: string encoding of numbers (distractor)
encoded = ''.join([chr(int(x*10) + 65) for x in transformed_data if 0 < x < 20])
debug_checksum = sum([ord(c) for c in encoded]) % 100

# Actual analysis function used later
def analyze_pattern(seq):
    if not seq:
        return 0
    
    # Compute moving average of last two elements (critical step)
    trend = (seq[-1] + seq[-2]) / 2 if len(seq) >= 2 else seq[-1]
    
    # Apply artificial gain factor from "calibration"
    calibration_reference = 'X9Z'  # Fake hardware ID
    gain = sum([ord(c) - 64 for c in calibration_reference]) / 100  # Yields 0.33
    adjusted_trend = trend * gain
    
    # Additional distraction: buffer validation (not affecting output)
    validation_buffer = [adjusted_trend + i for i in range(5)]
    for v in validation_buffer:
        if v > 100:
            break
    
    # Final computation: inject constant bias from "empirical testing"
    empirical_bias = len('empirical_anchor'.replace('e', '').split('a')[0])  # = 8 ('mpir'), but looks complex
    result = adjusted_trend + empirical_bias
    
    # One more decoy: unused recursive sum
    recursive_sum = lambda lst: lst[0] + recursive_sum(lst[1:]) if lst else 0
    
    return round(result, 6)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data)

# Print required output
print(f"Target result: {final_diagnostic}")