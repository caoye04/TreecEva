import math

# Simulate sensor data processing with noise filtering and diagnostic logic
def acquire_sensor_readings():
    raw = [0.12, 0.35, 0.58, 0.71, 0.93, 0.24, 0.67, 0.89, 0.41, 0.76]
    noise_floor = 0.2
    filtered = [x for x in raw if x > noise_floor]
    return sorted(filtered, reverse=True)


def apply_hamming_window(signal):
    N = len(signal)
    windowed = []
    for i in range(N):
        window_factor = 0.54 - 0.46 * math.cos((2 * math.pi * i) / (N - 1))
        windowed.append(signal[i] * window_factor)
    return windowed


def compress_dynamic_range(data, ratio=4.0):
    # Apply logarithmic compression to dynamic range
    compressed = []
    for x in data:
        if x <= 0.1:
            compressed.append(x)
        else:
            compressed.append(math.log10(x * ratio + 1))
    return compressed


def calculate_entropy(values):
    # Irrelevant function - decoy for information-theoretic analysis
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 6)


def rolling_average(series, window_size=3):
    averages = []
    for i in range(len(series) - window_size + 1):
        avg = sum(series[i:i+window_size]) / window_size
        averages.append(avg)
    return averages  # Dead code path - not used in main flow


def detect_spike_sequence(pattern):
    # Misleading spike detection - not actually used in final decision
    spikes = []
    for i in range(1, len(pattern)-1):
        if pattern[i] > pattern[i-1] and pattern[i] > pattern[i+1]:
            spikes.append(i)
    return len(spikes) > 2


def analyze_signal(data, threshold=0.5):
    # Core diagnostic logic
    if len(data) == 0:
        return 0.0
    
    # Step 1: Normalize data to max value
    norm_factor = max(data)
    normalized = [x / norm_factor for x in data]
    
    # Step 2: Count how many samples exceed threshold
    strong_signals = [x for x in normalized if x >= threshold]
    weak_signals = [x for x in normalized if x < threshold]
    
    # Step 3: Compute weighted contribution
    high_weight = 1.7
    low_weight = 0.4
    weighted_sum = (
        sum(x * high_weight for x in strong_signals) + 
        sum(x * low_weight for x in weak_signals)
    )
    
    # Step 4: Adjust based on signal continuity
    sorted_norm = sorted(normalized, reverse=True)
    continuity_score = 0.0
    for i in range(1, len(sorted_norm)):
        if sorted_norm[i-1] - sorted_norm[i] < 0.15:
            continuity_score += 0.1
    
    # Step 5: Conditional adjustment using ternary-like logic
    adjustment = 1.25 if len(strong_signals) >= 3 else (0.85 if len(strong_signals) == 2 else 0.6)
    
    # Step 6: Final computation
    base_metric = weighted_sum * adjustment
    final_score = base_metric + continuity_score
    
    # Irrelevant transformations below (distractors)
    squared_values = [x**2 for x in data]  # Unused
    peak_to_peak = max(data) - min(data)     # Computed but irrelevant
    inversion_test = [1.0 - x for x in data] # Dead end
    
    return round(final_score, 6)

# --- Main execution with red herrings ---
data_stream = acquire_sensor_readings()
windowed_signal = apply_hamming_window(data_stream)

# Fake preprocessing chain
temp_analysis_1 = calculate_entropy(windowed_signal)
smoothed_buffer = rolling_average(windowed_signal, window_size=2)
spike_count = detect_spike_sequence(windowed_signal)

# Actual relevant transformation
compressed_data = compress_dynamic_range(windowed_signal, ratio=3.8)

# Key statement
final_diagnostic = analyze_signal(compressed_data, threshold=0.65)

# Print result as required
print(f"Target result: {final_diagnostic}")