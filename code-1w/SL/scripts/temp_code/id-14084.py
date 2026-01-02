import itertools

# Sensor simulation and diagnostic system
# Real problem: Analyze composite signal readings for anomaly detection

# Irrelevant constants (distractors)
BASELINE_SENSITIVITY = 0.87
CALIBRATION_OFFSET = -0.03
MAX_BUFFER_SIZE = 256
TEMPORAL_WINDOW = 15

# Relevant signal parameters
signal_frequencies = [3, 7, 11]
signal_amplitudes = [4.2, 2.8, 1.6]
phase_shifts = [0.1, 0.5, 0.9]

# Simulate sensor readings over time
def generate_signal(frequency, amplitude, phase, duration=10, sample_rate=50):
    import math
    samples = []
    for t in range(duration * sample_rate):
        time_point = t / sample_rate
        value = amplitude * math.sin(2 * math.pi * frequency * time_point + phase)
        samples.append(value)
    return samples

# Generate raw signals (relevant)
raw_signals = []
for freq, amp, phase in zip(signal_frequencies, signal_amplitudes, phase_shifts):
    signal = generate_signal(freq, amp, phase)
    raw_signals.append(signal)

# Irrelevant function - dead code path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data[:100]]

# Another irrelevant utility
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0.0] * size
    def flush(self):
        pass

# Signal processing chain
buffer_handler = DataBuffer(MAX_BUFFER_SIZE)

# Flatten all signals into a single stream using itertools
combined_stream = list(itertools.chain.from_iterable(raw_signals))

# Apply moving average filter (relevant)
def moving_average(data, window_size=5):
    if len(data) < window_size:
        return data
    averaged = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        averaged.append(sum(window) / window_size)
    return averaged

filtered_signal = moving_average(combined_stream, window_size=4)

# Extract peaks above threshold (relevant)
def extract_peaks(data, threshold=2.0):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > threshold and data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append((i, data[i]))
    return peaks

# Misleading peak extraction with high threshold (distractor)
spurious_peaks = extract_peaks(filtered_signal, threshold=3.5)

# Actual relevant peak extraction
valid_peaks = extract_peaks(filtered_signal, threshold=1.8)

# Compute peak statistics (relevant)
total_peak_count = len(valid_peaks)
peak_magnitudes = [mag for _, mag in valid_peaks]
avg_peak_magnitude = sum(peak_magnitudes) / total_peak_count if total_peak_count > 0 else 0.0
max_peak_value = max(peak_magnitudes) if peak_magnitudes else 0.0

# Frequency domain analysis via simple binning (relevant)
bin_edges = [-4.0, -2.0, -1.0, 0.0, 1.0, 2.0, 4.0]
histogram = [0] * (len(bin_edges) - 1)
for val in filtered_signal:
    for i in range(len(bin_edges) - 1):
        if bin_edges[i] <= val < bin_edges[i+1]:
            histogram[i] += 1
            break

# Compute entropy of distribution (relevant)
from math import log
signal_probabilities = [count / len(filtered_signal) for count in histogram if count > 0]
entropy = -sum(p * log(p, 2) for p in signal_probabilities)

# Construct processed features (relevant)
processed_signals = {
    'peak_count': total_peak_count,
    'avg_peak': avg_peak_magnitude,
    'max_peak': max_peak_value,
    'entropy': entropy,
    'signal_length': len(filtered_signal),
    'baseline_ratio': avg_peak_magnitude / (max_peak_value + 1e-8)
}

# Irrelevant class - decoy
class LegacyAnalyzer:
    def __init__(self):
        self.active = False
    def analyze(self, data):
        return sum(data.values()) * 0.1

# Diagnostic logic (relevant)
def analyze_readings(features):
    # Complex decision logic with nested conditions
    score = 0
    
    if features['peak_count'] > 100:
        score += 25
    elif features['peak_count'] > 50:
        score += 15
    else:
        score += 5
        
    if features['avg_peak'] > 1.5:
        score += 20
    
    if features['max_peak'] > 3.0:
        score += 30
    
    if features['entropy'] > 2.0:
        score += 15
    
    # Compound condition with bitwise manipulation (relevant)
    peak_flag = features['peak_count'] > 75
    magnitude_flag = features['avg_peak'] > 1.2
    entropy_flag = features['entropy'] > 1.8
    
    flag_register = (peak_flag << 2) | (magnitude_flag << 1) | entropy_flag
    
    if flag_register & 0b101:  # Binary pattern match
        score += 10
    
    # Final adjustment based on ratio
    if features['baseline_ratio'] > 0.4:
        score *= 1.1
    
    return int(score)

# Execute main analysis
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")