import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [14, -8, 22, 31, -17, 9, 11, 25, -13, 0]
noise_floor = 7
sampling_rate = 44100

def apply_filter(data, threshold):
    """Apply high-pass filter above noise floor."""
    filtered = []
    for x in data:
        if abs(x) > threshold:
            filtered.append(x * 1.05)
    return filtered

def compute_envelope(signal):
    """Compute absolute envelope of signal."""
    return [abs(x) for x in signal]

def calculate_rms(series):
    """Calculate root mean square of a series."""
    if not series:
        return 0.0
    sum_squares = 0
    for val in series:
        sum_squares += val ** 2
    return math.sqrt(sum_squares / len(series))

def detect_peaks(values, sensitivity=0.8):
    """Detect peaks using dynamic threshold."""
    if not values:
        return []
    avg_val = sum(values) / len(values)
    threshold = avg_val * sensitivity
    peak_indices = []
    for i in range(1, len(values) - 1):
        if values[i] > threshold and values[i] > values[i-1] and values[i] > values[i+1]:
            peak_indices.append(i)
    return peak_indices

def integrate_series(data):
    """Cumulative integration of signal."""
    integrated = [0]
    for i in range(1, len(data)):
        integrated.append(integrated[-1] + (data[i] + data[i-1]) / 2)
    return integrated

# Irrelevant helper - dead function path
# def deprecated_normalization(vec):
#     max_val = max(vec)
#     return [x / max_val for x in vec] if max_val != 0 else vec

# Unused transformation matrix
transformation_matrix = [
    [1.0, 0.1],
    [-0.1, 0.9]
]

# Fake calibration constants (distractors)
calibration_offset_1 = 0.0034
calibration_offset_2 = -0.0012
temp_compensation = lambda t: 1 + 0.002 * (t - 25)

# Simulated temperature effect (not actually used)
temperature_profile = [22, 23, 25, 27, 26]
compensated_gains = [temp_compensation(t) for t in temperature_profile]

# Key processing chain begins
filtered_samples = apply_filter(raw_readings, noise_floor)
envelope = compute_envelope(filtered_samples)
rms_power = calculate_rms(envelope)

# Secondary unused metrics (misleading intermediate results)
spectral_estimate = rms_power * math.log(sampling_rate + 1) / 1000
coherence_score = 0.87 if rms_power > 15 else 0.32

# Integration step with red herring usage
integrated_signal = integrate_series(envelope)
prominent_peaks = detect_peaks(integrated_signal, sensitivity=0.6)

# Decoy assignment - looks important but unused
aggregate_metric = (rms_power * 0.7) + (len(prominent_peaks) * 2.3)

# Critical data transformation
processed_samples = [round(x, 2) for x in filtered_samples if x > 0]

# Another lambda distraction
weighting_func = lambda x: x * (1.1 if x > 15 else 0.9)
weighted_values = [weighting_func(x) for x in processed_samples]

# Unused list comprehension - dead code
_ = [x for x in raw_readings if x % 2 == 0 and x > 10]

# Core diagnostic logic
peak_magnitude_sum = 0
for i in prominent_peaks:
    if i < len(envelope):
        peak_magnitude_sum += envelope[i]

baseline_adjustment = len(processed_samples) * 0.25
heuristic_factor = 3 if peak_magnitude_sum > 50 else 1

# Final diagnostic computed from multiple indirect sources
final_diagnostic = int(
    (rms_power * heuristic_factor) 
    + baseline_adjustment 
    - (len(raw_readings) - len(filtered_samples))
    + (sum(processed_samples) // (len(processed_samples) or 1))
)

# Distractor print (not affecting result)
# print(f'Debug: {coherence_score=}, {spectral_estimate=}')

# Target result output
Result: final_diagnostic