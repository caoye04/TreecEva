import math

def preprocess_signal(raw_input, threshold=0.75):
    # Irrelevant preprocessing with decoy logic
    if len(raw_input) == 0:
        return [0]
    filtered = [x for x in raw_input if abs(x) > threshold]
    normalized = [(x + 1.0) / 2.0 for x in filtered]  # Not actually used later
    return filtered


def transform_coordinates(data_points):
    # Distractor function - looks important but unused
    polar = []
    for x in data_points:
        r = math.sqrt(x**2 + 1)
        theta = math.atan2(1, x)
        polar.append((r, theta))
    return polar


def generate_checksum(sequence):
    # Red herring: complex-looking but irrelevant computation
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum % 1000


def decode_frequency_pattern(signal):
    # Another decoy transformation
    pattern = []
    for s in signal:
        if s > 0:
            pattern.append(math.log(s + 1e-5))
        else:
            pattern.append(-math.log(abs(s) + 1e-5))
    return [round(p, 3) for p in pattern]


def accumulate_energy(signal):
    # Relevant but obscured: computes cumulative energy
    energy_levels = []
    total = 0.0
    for val in signal:
        total += val ** 2
        energy_levels.append(total)
    return energy_levels


def extract_peaks(data, min_gap=3):
    # Dead code path - never called
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1] and len(peaks) < min_gap:
            peaks.append(i)
    return peaks


def compute_entropy(values):
    # Unused advanced math distractor
    probs = [v / sum(values) for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)


def rolling_window_average(series, window=3):
    # Unused data smoothing function
    smoothed = []
    for i in range(len(series) - window + 1):
        smoothed.append(sum(series[i:i+window]) / window)
    return smoothed


def count_transitions(signal, mode='zero_crossing'):
    # Mildly relevant but ultimately unused
    transitions = 0
    reference = 0 if mode == 'zero_crossing' else sum(signal)/len(signal)
    for i in range(1, len(signal)):
        if (signal[i-1] < reference) != (signal[i] < reference):
            transitions += 1
    return transitions


def classify_magnitude(value):
    # Simple lookup with string methods (required feature)
    category_map = {
        'high': lambda x: x > 50,
        'medium': lambda x: 20 < x <= 50,
        'low': lambda x: x <= 20
    }
    for cat, cond in category_map.items():
        if cond(abs(value)):
            return cat.upper().replace('H', 'h')  # Use of string method
    return 'unknown'


def aggregate_diagnostics(metrics_dict):
    # Dictionary operation (required feature): combines multiple metrics
    weights = {'energy': 0.6, 'stability': 0.3, 'noise': 0.1}
    score = 0.0
    for key, val in metrics_dict.items():
        if key in weights:
            score += weights[key] * val
    return round(score, 4)


def analyze_signal(cleaned_signal):
    # Core logic buried among distractions
    
    # Step 1: Compute energy accumulation over signal
    energy_profile = accumulate_energy(cleaned_signal)
    
    # Step 2: Derive stability metric from variance proxy
    avg_energy = sum(energy_profile) / len(energy_profile)
    variance_proxy = sum((e - avg_energy) ** 2 for e in energy_profile) / len(energy_profile)
    stability_index = 100 / (1 + variance_proxy)  # Higher is more stable
    
    # Step 3: Count significant fluctuations (not zero crossings)
    fluctuation_count = 0
    for i in range(1, len(cleaned_signal)):
        if abs(cleaned_signal[i] - cleaned_signal[i-1]) > 0.5:
            fluctuation_count += 1
    
    # Step 4: Compute noise ratio based on small-magnitude values
    small_values = [x for x in cleaned_signal if abs(x) < 0.3]
    noise_ratio = len(small_values) / len(cleaned_signal)
    
    # Step 5: Build diagnostic dictionary
    diagnostics = {
        'energy': energy_profile[-1],
        'stability': stability_index,
        'noise': 1 - noise_ratio  # Invert because less noise is better
    }
    
    # Step 6: Aggregate into final score
    final_score = aggregate_diagnostics(diagnostics)
    
    # Step 7: Apply nonlinear transformation
    adjusted = math.tanh(final_score / 10) * 100
    
    # Step 8: Final diagnostic calculation
    final_diagnostic = int(round(adjusted))
    
    return final_diagnostic

# Main execution block with misleading setup
raw_sensor_data = [
    0.12, -0.33, 0.88, 1.05, -0.09, 0.11, 1.92, -1.11, 0.76, 0.22,
    -0.44, 0.99, 1.33, -0.21, 0.55, 0.67, -0.89, 1.01, 0.34, -0.12
]

# Distractor variables
checksum_value = generate_checksum(raw_sensor_data)
decoded_patterns = decode_frequency_pattern(raw_sensor_data)
frequency_entropy = compute_entropy([abs(x) for x in raw_sensor_data if x > 0])

data_stats = {
    'count': len(raw_sensor_data),
    'positive_ratio': len([x for x in raw_sensor_data if x > 0]) / len(raw_sensor_data),
    'magnitude_class': classify_magnitude(sum(raw_sensor_data))
}

# Actual processing begins here — the only relevant pipeline
processed_data = preprocess_signal(raw_sensor_data, threshold=0.2)

# Key statement
final_diagnostic = analyze_signal(processed_data)

# Output result
print(f"Target result: {final_diagnostic}")