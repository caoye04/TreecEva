import math

# Simulated environmental sensor data processing with noise filtering
raw_readings = [3.2, 1.7, 4.9, 0.5, 2.1, 6.3, 5.8, 2.4, 3.6, 4.1]

def apply_window_filter(data, window_size=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window = data[start:end]
        avg = sum(window) / len(window)
        smoothed.append(avg)
    return smoothed

# Irrelevant transformation: frequency domain mock (distractor)
def compute_spectral_energy(signal):
    energy = 0
    for x in signal:
        energy += x * math.sin(x)  # Not actually used in final result
    return energy

# Core purification logic
def extract_high_quality(data, threshold=2.5):
    return [x for x in data if x > threshold]

def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

# Decoy function: looks important but unused in critical path
def analyze_trend(sequence):
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    trend_score = sum(1 for d in diffs if d > 0)
    return trend_score * 1.5

# Real processing begins
filtered_readings = apply_window_filter(raw_readings)

# Misleading intermediate: looks like feature engineering
amplitude_peaks = list(map(lambda x: x ** 2, filtered_readings))
spectral_signature = compute_spectral_energy(amplitude_peaks)  # Dead-end calculation

# Actual data refinement path
refined_stream = extract_high_quality(filtered_readings)

# Multiple distractor variables
normalization_factor = math.sqrt(sum([x**2 for x in refined_stream])) or 1
scaled_data = [x / normalization_factor for x in refined_stream]
baseline_offset = sum(scaled_data) / len(scaled_data) if scaled_data else 0

# Set operations to introduce complexity
unique_bands = set([int(x * 10) % 7 for x in raw_readings])
critical_bands = {1, 3, 5}
overlap_count = len(unique_bands & critical_bands)

# Secondary red herring: combinatorics distraction
from itertools import combinations
diagnostic_pairs = list(combinations(refined_stream, 2))
stability_metric = len(diagnostic_pairs) / (len(refined_stream) ** 2) if refined_stream else 0

# Key computation chain
entropy_value = calculate_entropy(refined_stream)
band_penalty = overlap_count * 0.3

# Central evaluation function
def evaluate_purity(elements):
    if not elements:
        return 0.0
    base_purity = sum([math.log(e) for e in elements if e > 1])
    adjustment = band_penalty
    purity_index = base_purity - adjustment
    return round(purity_index, 6)

# Critical execution point
filtration_score = evaluate_purity(processed_elements=refined_stream)

# Final output
print(f"Result: {filtration_score}")