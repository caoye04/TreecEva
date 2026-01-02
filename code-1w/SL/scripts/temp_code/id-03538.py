from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant channels
data_stream = [
    (1, [3.2, 1.8, 0.9, 5.5, 2.1, 1.8]),
    (2, [4.1, 2.0, 1.1, 6.3, 2.2, 1.9]),
    (3, [2.9, 1.7, 0.8, 5.1, 2.0, 1.7]),
    (4, [3.3, 1.9, 1.0, 5.6, 2.1, 1.8]),
    (5, [3.0, 1.8, 0.9, 5.4, 2.0, 1.7])
]

# Irrelevant baseline model parameters (distractor)
baseline_coefficients = [0.88, 1.02, 0.75, 1.15, 0.94, 1.01]
calibration_matrix = [[1.03, 0.99], [0.97, 1.04]]
offset_correction = sum(baseline_coefficients) / len(baseline_coefficients) * 0.01

# Noise threshold filters (partially used)
noise_floor = 0.5
amplitude_ceiling = 6.0

# Misleading transformation chain (dead path)
def legacy_transform(x):
    return [val * 0.97 + 0.1 for val in x if val > noise_floor]

def apply_mask(signal, mask=[1, 1, 0, 1, 1, 0]):
    return [s * m for s, m in zip(signal, mask)]

# Signal conditioning pipeline
def denoise_signal(signal):
    return [x for x in signal if noise_floor <= x <= amplitude_ceiling]

def align_phase(signal):
    phase_shift = int(sum(signal) % 3)
    return signal[phase_shift:] + signal[:phase_shift]

# Core processing functions
def extract_anomaly_signature(data):
    readings = [entry[1][2] for entry in data]  # Extract channel 2 (prone to anomalies)
    avg = sum(readings) / len(readings)
    deviations = [(x - avg) ** 2 for x in readings]
    return sum(deviations)

# Red herring function: looks important but unused
def compute_entropy(signal):
    counter = Counter([round(x, 1) for x in signal])
    total = sum(counter.values())
    return -sum((count / total) * math.log2(count / total) for count in counter.values())

# Real processing path begins here
filtered_data = []
for timestamp, raw_readings in data_stream:
    cleaned = denoise_signal(raw_readings)
    adjusted = [x * 1.05 for x in cleaned]  # Empirical gain correction
    if len(adjusted) > 4:
        aligned = align_phase(adjusted)
        filtered_data.append((timestamp, aligned))

# Decoy aggregation (unused result)
temp_aggregate = defaultdict(float)
for t, readings in filtered_data:
    temp_aggregate[t] = sum(readings) / len(readings)

# Key transformation using lambda and set operations (core concept)
reference_set = {round(v, 1) for v in baseline_coefficients}
processing_pipeline = lambda x: round(sum(x) / len(x), 3)

normalized_vectors = [
    [val / processing_pipeline(data[1]) for val in data[1]]
    for data in filtered_data
]

# Main analysis function
def process_readings(log):
    cumulative_score = 0
    for idx, (ts, vec) in enumerate(log):
        # Bitwise modulation of timestamp (minor influence)
        mod_factor = ts ^ (idx + 1)
        mod_factor = mod_factor & 7  # Restrict range
        
        # Core calculation
        base_mean = sum(vec) / len(vec)
        peak_response = max(vec)
        response_ratio = peak_response / base_mean
        
        # Use of set difference as subtle weight
        unique_components = {round(v, 1) for v in vec} - reference_set
        specificity_bonus = len(unique_components) * 0.2
        
        # Accumulate weighted diagnostic
        step_score = (response_ratio + specificity_bonus) * (mod_factor + 1)
        cumulative_score += step_score
    
    # Final nonlinear transformation
    final_value = int((cumulative_score * 100) // len(log))
    return final_value

# Secondary decoy function (never called)
def validate_consistency(log):
    all_vals = [v for _, vec in log for v in vec]
    freq = Counter(all_vals)
    return max(freq.values()) / len(all_vals)

# Critical execution point
final_diagnostic = process_readings(filtered_data)

# Print result for evaluation
print(f"Result: {final_diagnostic}")