def preprocess_signal(raw_samples):
    """Apply irrelevant transformation to signal data."""
    magnitude = sum(abs(x) for x in raw_samples)
    normalized = [x / (magnitude + 1e-9) for x in raw_samples]
    filtered = [x for x in normalized if abs(x) > 0.01]
    return filtered

# Irrelevant frequency analysis
def compute_harmonics(components):
    harmonics = []
    for i, val in enumerate(components):
        if i % 2 == 1:
            harmonics.append(val * (i + 1))
    return [h * 0.5 for h in harmonics]

# Fake noise reduction (dead code path)
def reduce_noise(signal):
    smoothed = []
    for i in range(1, len(signal) - 1):
        avg = (signal[i-1] + signal[i] + signal[i+1]) / 3
        smoothed.append(avg)
    return smoothed

# Character counting distraction
def count_chars_in_labels(labels):
    total = 0
    for label in labels:
        total += len(label.strip())
    return total

# Bit manipulation red herring
def encode_flags(mode, debug=False):
    base = mode << 3
    if debug:
        base |= 7
    else:
        base |= 1
    return base ^ 255  # Obfuscation

# Core logic disguised among distractors
def extract_peaks(series, sensitivity=0.1):
    peaks = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            if series[i] - series[i-1] > sensitivity and series[i] - series[i+1] > sensitivity:
                peaks.append((i, series[i]))
    return peaks

# Data restructuring with zip distraction
def align_segments(primary, secondary):
    if len(primary) != len(secondary):
        min_len = min(len(primary), len(secondary))
        primary = primary[:min_len]
        secondary = secondary[:min_len]
    paired = list(zip(primary, secondary))
    indexed = [(i, p, s) for i, (p, s) in enumerate(paired)]
    return indexed  # Unused return

# Actual processing chain
raw_data = [12.4, 15.6, 13.2, 18.1, 17.9, 20.3, 19.8, 22.5, 21.7, 16.8]
labels_list = ['sensor_A', 'sensor_B', 'sensor_C']
mode_setting = 5

# Distractor: unused variables
baseline_offset = 0.0034
scaling_factor = 1.0045
max_iterations = 150
convergence_epsilon = 1e-6
dummy_matrix = [[i*j for j in range(4)] for i in range(4)]

# Distractor: dead function call
char_count = count_chars_in_labels(labels_list)
encoded_mode = encode_flags(mode_setting, debug=False)

# Real preprocessing
filtered_signal = preprocess_signal(raw_data)

# Red herring: harmonic analysis on irrelevant data
if len(filtered_signal) > 5:
    _ = compute_harmonics(filtered_signal[:6])

# Key peak extraction
significant_peaks = extract_peaks(filtered_signal, sensitivity=0.05)

# Simulate auxiliary data
auxiliary_readings = [x * 0.87 for x in raw_data[::2]]

# Use of enumerate and zip as required
paired_diagnostics = []
for idx, (pos, val) in enumerate(significant_peaks):
    correction = 1 + (idx * 0.02)
    adjusted_val = val * correction
    paired_diagnostics.append((pos, adjusted_val))

# Create threshold map (partially used)
threshold_map = {f'level_{i}': 0.5 + i*0.1 for i in range(len(significant_peaks))}
temp_thresholds = [t for t in threshold_map.values()]

# Main analysis function
def analyze_readings(peaks_with_position, thresholds):
    cumulative_score = 0.0
    peak_values = [val for pos, val in peaks_with_position]
    
    # Bitwise red herring
    magic_seed = 17
    for i, v in enumerate(peak_values):
        shifted = (magic_seed << 2) ^ i
        contribution = v * ((shifted & 7) / 4.0)
        cumulative_score += contribution if i % 2 == 0 else contribution * 0.9
    
    # Final adjustment using threshold lengths
    length_factor = len(thresholds) * 1.5 if thresholds else 1.0
    final_score = cumulative_score * length_factor
    
    # Decoy calculation
    _ = [x ** 2 for x in peak_values if x > 1.5]
    
    return final_score

# Execution point of interest
final_diagnostic = analyze_readings(paired_diagnostics, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")