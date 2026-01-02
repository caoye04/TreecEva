from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and redundant readings
data_stream = [18, 22, 25, 25, 22, 19, 20, 24, 26, 28, 30, 33, 32, 30, 27, 25, 24, 23, 22, 20, 19, 18]

# Irrelevant auxiliary data (distractor)
aux_temperatures = [21, 23, 19, 25, 27, 20, 18, 22]  # Unused in final calculation

# Preprocessing: filter anomalies using a sliding window (relevant)
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size // 2)
        end = min(len(signal), i + window_size // 2 + 1)
        window = signal[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Transform raw data into frequency domain via simplified DFT (relevant)
def compute_spectral_density(signal):
    N = len(signal)
    spectrum = []
    for k in range(N // 4):  # Only compute first quarter for efficiency
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(-signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(real**2 + imag**2)
        spectrum.append(magnitude)
    return spectrum

# Misleading function: looks important but unused (red herring)
def calculate_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy  # Never called

# Another decoy: processes irrelevant metrics
def assess_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs) > 2.0

# Signal transformation pipeline
smoothed_data = smooth_signal(data_stream)
filtered_data = [x for x in smoothed_data if 20 <= x <= 30]  # Trim outliers

# Apply spectral analysis to detect periodic patterns
spectral_components = compute_spectral_density(filtered_data)

# Simulate hardware calibration offset (irrelevant adjustment)
calibration_map = defaultdict(lambda: 0.95)
for freq in range(5):
    calibration_map[freq] = 0.9 + (freq * 0.03)  # Not actually applied

# Apply artificial gain boost (distractor computation)
boosted_spectrum = [val * 1.15 for val in spectral_components]
gain_factor = 1.15  # Unused beyond this point

# Normalize spectral data for pattern recognition
normalized_spectrum = [s / sum(spectral_components) for s in spectral_components]

# Transform into discrete pattern codes based on thresholds (key transformation)
transformed_data = []
for val in normalized_spectrum:
    if val > 0.12:
        transformed_data.append(3)
    elif val > 0.08:
        transformed_data.append(2)
    elif val > 0.03:
        transformed_data.append(1)
    else:
        transformed_data.append(0)

# Decoy statistical summary (dead code path)
stats_summary = {}
stats_summary['mean'] = sum(transformed_data) / len(transformed_data)
stats_summary['mode'] = Counter(transformed_data).most_common(1)[0][0]

# Core diagnostic analyzer (critical logic)
def analyze_pattern(pattern_seq, sensitivity_threshold):
    pattern_counter = defaultdict(int)
    for p in pattern_seq:
        pattern_counter[p] += 1

    # Weighted risk score based on pattern frequency
    weights = {0: -1.0, 1: 0.5, 2: 2.0, 3: 5.5}
    base_score = sum(weights[p] * pattern_counter[p] for p in pattern_counter)
    
    # Adjust by threshold modulation (threshold affects scaling)
    adjustment_factor = 1.0 + (sensitivity_threshold * 0.05)
    adjusted_score = base_score * adjustment_factor
    
    # Secondary correction based on sequence length (anti-pattern check)
    if len(pattern_seq) < 4:
        adjusted_score -= 2.5
    
    # Final nonlinear transformation
    final_value = int((adjusted_score ** 2) + 17) % 999
    return final_value

# Phantom control flag (misleading boolean)
enable_deep_analysis = False  # Looks important but not used

# Threshold derived from data characteristics (relevant)
threshold = int(sum(smoothed_data) / len(smoothed_data)) % 7  # Yields 5

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result as required
print(f"Result: {final_diagnostic}")