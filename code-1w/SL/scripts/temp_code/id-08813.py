import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
    offset = 0.05
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant transformation: frequency mirroring (dead logic path)
def mirror_frequency(signal):
    mirrored = [max(signal) - x for x in signal]
    normalized = [x / max(mirrored) if max(mirrored) != 0 else 0 for x in mirrored]
    return normalized

# Signal envelope detection (partially relevant)
def detect_envelope(signal):
    envelope = []
    for i in range(1, len(signal)):
        diff = abs(signal[i] - signal[i-1])
        envelope.append(diff * 2.0)
    return envelope

# Data smoothing via moving average (distractor)
def smooth_data(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        smoothed.append(avg)
    return smoothed

# Red herring function: spectral centroid (unused in final path)
def compute_centroid(amplitudes):
    weighted_sum = sum(i * a for i, a in enumerate(amplitudes))
    total_power = sum(amplitudes)
    return weighted_sum / total_power if total_power > 0 else 0

# Core transformation: square root compression
def compress_signal(data):
    compressed = [math.sqrt(x) for x in data]
    return compressed

# Conditional threshold filtering with string-tagged modes
def filter_outliers(data, mode='strict'):
    threshold = 3.0 if mode == 'strict' else 2.5
    tag_map = {'strict': 'S', 'loose': 'L'}
    mode_tag = tag_map.get(mode, 'X')
    filtered = [x for x in data if x <= threshold]
    log_entry = f"Filtered using {mode_tag} mode: {len(data)} -> {len(filtered)}"
    # Log not used further
    return filtered

# Recursive peak pairing algorithm (key component)
def pair_peaks(values, depth=0):
    if len(values) < 2 or depth > 5:
        return [sum(values) * 0.5] if values else [0]
    paired = []
    for i in range(0, len(values) - 1, 2):
        product = values[i] * values[i+1]
        paired.append(math.log(product + 1))
    return pair_peaks(paired, depth + 1)

# Main analysis pipeline
processed_data = []
data_source = collect_readings()

# Apply compression
compressed_signal = compress_signal(data_source)

# Distractor: smoothing chain (not used in final result)
smoothed_primary = smooth_data(compressed_signal, window=2)
smoothed_secondary = smooth_data(smoothed_primary, window=2)

# Filter based on dynamic condition
filter_mode = 'strict' if len(compressed_signal) > 5 else 'loose'
filtered_signal = filter_outliers(compressed_signal, mode=('strict' if sum(compressed_signal) > 10 else 'loose'))

# Envelope extraction (red herring)
envelope_trace = detect_envelope(filtered_signal)
centroid_value = compute_centroid(envelope_trace) if envelope_trace else 0

# Mirror transform (completely irrelevant)
mirrored_comp = mirror_frequency(compressed_signal)

# Key processing step: only filtered_signal goes into recursive pairing
paired_diagnostics = pair_peaks(filtered_signal)

# Final diagnostic computation
if paired_diagnostics:
    mean_diagnostic = sum(paired_diagnostics) / len(paired_diagnostics)
    adjustment_factor = len(filtered_signal) % 4 + 1
    final_diagnostic = mean_diagnostic * adjustment_factor
else:
    final_diagnostic = 0

# String-based status report (uses string methods)
status = "DIAGNOSTIC_{}".format("PASS" if final_diagnostic > 0 else "FAIL")
status_lower = status.lower()
clean_status = status_lower.replace("_", ".") if "pass" in status_lower else "error"

# Output result
print(f"Result: {final_diagnostic}")