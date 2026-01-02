import itertools
import math

# Simulated sensor data preprocessing pipeline for environmental monitoring system
def preprocess_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if -50 <= x <= 50]
    normalized = [round(x / max(filtered), 6) for x in filtered if x != 0]
    return normalized

# Signal windowing using sliding window technique
def create_signal_windows(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i + size])
    return windows

# Misleading auxiliary function - never called in execution path
def legacy_calculate_entropy(arr):
    total = 0.0
    for x in arr:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 6)

# Decoy transformation - looks important but unused
intermediate_weights = [0.1, 0.2, 0.3, 0.4]
weight_map = {i: w for i, w in enumerate(intermediate_weights)}

# Red herring: Historical threshold values from deprecated system
THRESHOLDS_V1 = {
    'low': 0.15,
    'medium': 0.35,
    'high': 0.65
}

# Unused signal smoothing (distractor)
def smooth_signal(signal, factor=0.8):
    smoothed = [signal[0]]
    for i in range(1, len(signal)):
        smoothed.append(factor * smoothed[-1] + (1 - factor) * signal[i])
    return smoothed

# Core computation chain
raw_sensor_input = [12, -8, 44, 0, -23, 31, 17, 55, -41, 29, 3, -14, 49]

# Step 1: Preprocess valid readings
cleaned_data = preprocess_sensor_data(raw_sensor_input)

# Step 2: Generate overlapping windows
signal_blocks = create_signal_windows(cleaned_data, 3)

# Step 3: Compute geometric mean for each window
geometric_means = []
for block in signal_blocks:
    product = 1.0
    for val in block:
        product *= abs(val) + 1e-6  # Avoid zero multiplication
    gm = product ** (1/len(block))
    geometric_means.append(round(gm, 6))

# Step 4: Apply frequency weighting based on position (simulated sensor bias)
frequency_weighted = []
for idx, val in enumerate(geometric_means):
    weight = (math.sin(idx * 0.5) + 1.5)  # Oscillating weight pattern
    frequency_weighted.append(val * weight)

# Step 5: Filter by dynamic threshold (adaptive)
dynamic_threshold = sum(frequency_weighted) / len(frequency_weighted)
filtered_dominant = [v for v in frequency_weighted if v >= dynamic_threshold]

# Step 6: Pairwise difference analysis
pairwise_diffs = []
for i in range(len(filtered_dominant) - 1):
    pairwise_diffs.append(abs(filtered_dominant[i+1] - filtered_dominant[i]))

# Step 7: Detect oscillation patterns using itertools.cycle simulation
pattern_cycle = list(itertools.islice(itertools.cycle([1, -1]), len(pairwise_diffs)))
adjusted_diffs = [diff * pattern_cycle[i] for i, diff in enumerate(pairwise_diffs)]
net_oscillation = sum(adjusted_diffs)

# Step 8: Compute harmonic components
reciprocals = [1 / (abs(v) + 1e-6) for v in filtered_dominant]
harmonic_sum = sum(reciprocals)
effective_rank = len(filtered_dominant) / harmonic_sum  # harmonic mean denominator

# Step 9: Final aggregation function
def compute_harmonic_aggregate(values):
    if not values:
        return 0.0
    reciprocal_total = sum(1 / (abs(x) + 1e-6) for x in values)
    base_harmonic = len(values) / reciprocal_total
    
    # Apply correction based on oscillation signature
    correction_factor = (1 + math.tanh(net_oscillation)) / 2  # Normalize to [0,1]
    corrected = base_harmonic * correction_factor
    
    # Final adjustment using integer division logic
    int_component = int(corrected)
    frac_component = corrected - int_component
    final_value = int_component + (frac_component * 0.75)
    
    return round(final_value, 6)

# Processed signals after multiple transformations
processed_signals = [v for v in frequency_weighted if v > 0.1]  # Re-filter for significance

# Critical execution point
final_yield = compute_harmonic_aggregate(processed_signals)

# Output result
print(f"Result: {final_yield}")