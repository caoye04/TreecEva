import itertools
from collections import defaultdict, Counter

# Simulated sensor data stream with noise and redundant metrics
def generate_noisy_readings():
    base_values = [i * 2 + (-1)**i for i in range(15)]
    noise_offset = [3, -1, 2, 0, -3] * 3
    return [base_values[i] + noise_offset[i] for i in range(15)]

# Irrelevant auxiliary function - dead code path (distractor)
def legacy_calibrate(x):
    return sum([i**2 for i in x if i > 0]) // max(1, len(x))

# Unused transformation (red herring)
def frequency_envelope(signal):
    envelope = []
    for i in range(1, len(signal)-1):
        slope_fwd = signal[i+1] - signal[i]
        slope_bwd = signal[i] - signal[i-1]
        envelope.append((slope_fwd + slope_bwd) / 2)
    return envelope

# Core processing: filter anomalies using moving window
def sliding_window_anomalies(data, window_size=4, tolerance=2.5):
    anomalies = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        mean_val = sum(window) / len(window)
        variance = sum((x - mean_val)**2 for x in window) / len(window)
        std_dev = variance ** 0.5
        # Detect outlier based on deviation
        for val in window:
            if abs(val - mean_val) > tolerance * std_dev:
                anomalies.append(val)
    return list(set(anomalies))  # deduplicate

# Transform data by applying bit manipulation filters (real path)
def bitwise_condition_mask(data):
    masked = []
    for x in data:
        # Apply XOR mask with prime-based pattern
        masked_val = x ^ 7  # arbitrary prime key
        if (masked_val & 3) == 0:  # divisible by 4 after mask?
            masked.append(masked_val)
    return masked

# Main pattern analyzer (critical function)
def analyze_pattern(seq, config):
    if not seq:
        return 0
    
    # Step 1: Count frequency of values
    freq_map = Counter(seq)
    
    # Step 2: Extract high-frequency cores
    core_elements = [k for k, v in freq_map.items() if v >= config['min_freq']]
    
    # Step 3: Compute entropy-like measure
    total = len(seq)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0  # natural log approximation
    
    # Step 4: Use itertools to generate pairwise products (combinatorics)
    pairs = list(itertools.combinations(core_elements, 2))
    product_sum = sum(a * b for a, b in pairs) if pairs else 0
    
    # Step 5: Apply final weighting
    adjustment = config['scale'] * (product_sum % 17)
    return int(abs(entropy * 100) + adjustment)

# ==================== MAIN EXECUTION ====================

# Generate raw input
diagnostic_stream = generate_noisy_readings()

# Dead-end analysis (distractor)
baseline_score = legacy_calibrate(diagnostic_stream)

# Real pipeline begins
filtered_anomalies = sliding_window_anomalies(diagnostic_stream, window_size=3, tolerance=1.8)

# Secondary filtering via bit logic
refined_diagnostics = bitwise_condition_mask(filtered_anomalies)

# Construct transformed data using list comprehension and filtering
even_shifted = [x for x in refined_diagnostics if x % 2 == 0]
doubled_signal = [val * 2 for val in even_shifted]

# Add dummy container (misleading structure)
data_junction = defaultdict(list)
for item in doubled_signal:
    data_junction['buffer'].append(item)  # never used again

transformed_data = doubled_signal.copy()

# Setup configuration map (mix of relevant and irrelevant keys)
thresholds = {
    'min_freq': 1,
    'scale': 3.7,
    'debug_mode': True,
    'timeout': 5000,
    'version': '2.1a'
}

# Introduce decoy intermediate result (misleading)
temp_diagnostic = sum(refined_diagnostics) * 0.1

# Key execution point
final_diagnostic = analyze_pattern(transformed_data, thresholds)

# Output result
print(f"Result: {final_diagnostic}")