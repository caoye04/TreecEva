import math

# Simulated sensor array data processing with diagnostic evaluation
def preprocess_readings(raw_samples):
    filtered = [x for x in raw_samples if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    return normalized

# Irrelevant helper: spectral weight calculation (unused in final logic)
def compute_spectral_weight(seq):
    return sum(math.sin(x * math.pi / 4) for x in seq)

# Core transformation: apply exponential moving average
def smooth_sequence(data, alpha=0.3):
    if not data:
        return []
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(alpha * data[i] + (1 - alpha) * smoothed[-1])
    return smoothed

# Auxiliary function: detect volatility spikes (distractor)
def identify_spike_indices(ts):
    spikes = []
    for i in range(1, len(ts)):
        if abs(ts[i] - ts[i-1]) > 0.1:
            spikes.append(i)
    return spikes

# Real pattern analyzer: counts transitions above dynamic threshold
def analyze_pattern(series, limits):
    count = 0
    threshold = limits['primary']
    for i in range(1, len(series)):
        if series[i-1] < threshold <= series[i]:
            count += 1
    return count

# Decoy analysis function (never called)
def legacy_evaluation(stream):
    return len([x for x in stream if x > 0.5]) * 2

# Unused recursive peak finder
def find_peaks_recursive(arr, idx=0):
    if idx >= len(arr) - 1:
        return []
    if arr[idx] > arr[idx-1] and arr[idx] > arr[idx+1]:
        return [idx] + find_peaks_recursive(arr, idx + 1)
    return find_peaks_recursive(arr, idx + 1)

# Main execution workflow
raw_sensor_data = [5, 12, 18, 25, 30, 40, 60, 80, 95, 105, 45, 70, 88]
baseline_shift = sum(raw_sensor_data) / len(raw_sensor_data)  # Distractor value

# Apply preprocessing
cleaned_readings = preprocess_readings(raw_sensor_data)

# Smooth the sequence
smoothed_signal = smooth_sequence(cleaned_readings, alpha=0.4)

# Transform via nonlinear compression
compressed = [math.log(1 + x) for x in smoothed_signal]

# Further normalize using min-max scaling
min_val, max_val = min(compressed), max(compressed)
delta = max_val - min_val or 1
transformed_data = [(x - min_val) / delta for x in compressed]

# Generate various irrelevant metrics
spectral_score = compute_spectral_weight(smoothed_signal)
spike_locations = identify_spike_indices(transformed_data)

# Define decision thresholds (only 'primary' is used)
thresholds = {
    'primary': 0.42,
    'secondary': 0.68,  # unused
    'emergency': 0.91   # unused
}

# Slice only middle portion (simulates region of interest extraction)
roi_data = transformed_data[2:-1]

# Lambda-based outlier filter (not applied, distractor)
outlier_removal = lambda seq, t: [x for x in seq if abs(x - sum(seq)/len(seq)) < t]

# Dictionary mapping for state simulation (partially used)
state_registry = {
    'idle': 0,
    'active': 1,
    'standby': 2,
    'calibrating': lambda: baseline_shift % 7  # never invoked
}

# Key assignment statement
final_diagnostic = analyze_pattern(transformed_data, thresholds)

# Print result for evaluation
print(f"Result: {final_diagnostic}")