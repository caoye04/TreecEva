import math

# Simulated sensor array data from environmental monitoring system
def fetch_sensor_data():
    return [12.4, 15.6, 13.2, 18.9, 14.3, 16.7, 19.1, 11.8, 14.0, 15.2]

# Legacy function – not used in current pipeline (red herring)
def legacy_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Irrelevant transformation - used to distract
def frequency_shift(signal_list, shift_factor=2.1):
    shifted = []
    for val in signal_list:
        shifted.append(val * shift_factor + 0.5)
    return shifted

# Signal smoothing using moving average (used)
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window = signal[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Outlier detection (not actually used in final chain)
def detect_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return {i for i, x in enumerate(data) if abs(x - mean_val) > threshold * std_dev}

# Character analysis from metadata tags (decoy function)
def analyze_tag_characters(tags):
    char_count = {}
    for tag in tags:
        for char in tag.lower():
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Used to generate side information, but not part of main result
tags_metadata = ['SIG_A', 'RAW_B', 'FLT_C', 'MON_D']
side_info = analyze_tag_characters(tags_metadata)

# Transform readings into discrete bands (critical step)
def quantize_readings(readings, bins=5):
    min_r, max_r = min(readings), max(readings)
    span = (max_r - min_r) / bins
    if span == 0: span = 1
    bands = []
    for r in readings:
        band = int((r - min_r) // span)
        bands.append(min(band, bins - 1))
    return bands

# Core analysis logic
seen_combinations = set()
def accumulate_patterns(banded_data, history_window=4):
    patterns = []
    for i in range(len(banded_data) - history_window + 1):
        window = tuple(banded_data[i:i + history_window])
        if window not in seen_combinations:
            seen_combinations.add(window)
            patterns.append(window)
    return len(patterns)

# Main processing pipeline
raw_signals = fetch_sensor_data()

# Apply smoothing - relevant
processed_signals = smooth_signal(raw_signals)

# Quantize the processed signals - relevant
quantized = quantize_readings(processed_signals, bins=6)

# Unused outlier map - misleading intermediate
outlier_map = detect_outliers(processed_signals)

# Frequency-shifted copy - dead end
shifted_spectrum = frequency_shift(processed_signals, 1.7)

# Some arbitrary accumulations to mislead
phantom_sum = sum(shifted_spectrum[i] for i in range(0, len(shifted_spectrum), 2))
decoy_metric = math.log(phantom_sum + 1) * 0.3

# Set-based filtering of quantized states (uses set operations - required feature)
available_states = set(quantized)
required_states = {0, 1, 2, 3}
missing_count = len(required_states - available_states)

# Analyze the actual diagnostic
previous_diagnostics = [(1,1,0,2), (0,1,1,3)]  # historical cache
for item in previous_diagnostics:
    seen_combinations.add(item)

# Key function that computes final result
def analyze_readings(cleaned_signal):
    binned = quantize_readings(cleaned_signal, bins=6)
    unique_pattern_count = accumulate_patterns(binned, history_window=3)
    
    # Secondary factor: entropy-like measure
    freq_map = {}
    for val in binned:
        freq_map[val] = freq_map.get(val, 0) + 1
    total = len(binned)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    
    # Tertiary influence: stability score based on set dispersion
    unique_values = len(set(binned))
    stability = unique_values * 10
    
    # Final composition
    result = unique_pattern_count * 17 + int(stability + entropy * 10) - missing_count * 5
    return result

# Critical assignment point
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")