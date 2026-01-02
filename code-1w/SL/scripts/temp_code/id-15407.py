import itertools

# Simulated sensor readings with noise and redundant data
data_stream = [18, 22, 25, 27, 30, 33, 35, 36, 38, 40, 42, 45, 47, 50, 55]
noise_floor = [0.1, -0.2, 0.3, -0.1, 0.05]
duplicate_flags = set()
anomaly_buffer = []
calibration_offset = 0.25

# Irrelevant pre-processing: checksum validation (never used later)
checksum = sum(d * i for i, d in enumerate(data_stream)) % 1000

# Apply noisy offset (only some components are relevant)
adjusted_readings = [x + calibration_offset for x in data_stream]

# Misleading transformation: frequency simulation (unused later)
frequencies = [abs((adjusted_readings[i] - adjusted_readings[i-1]) / 2) for i in range(1, len(adjusted_readings))]
frequencies.insert(0, 0)

# Decoy function: looks important but never called
def compute_resonance(seq):
    return sum(s ** 0.5 for s in seq if s > 25) / len(seq)

# Real signal extraction: isolate rising trends above threshold
rising_segments = []
for i in range(1, len(adjusted_readings)):
    if adjusted_readings[i] > adjusted_readings[i-1]:
        rising_segments.append(adjusted_readings[i] - adjusted_readings[i-1])

# Inject artificial stabilization pulse (distraction)
stabilized_rise = []
for val in rising_segments:
    if val > 2.0:
        stabilized_rise.append(val - 0.5)
    else:
        stabilized_rise.append(val)

# Compute rolling average of last 5 rises (red herring)
rolling_avg = sum(stabilized_rise[-5:]) / len(stabilized_rise[-5:]) if len(stabilized_rise) >= 5 else 0

# Critical path: transform data using windowed variance
window_size = 4
deviation_windows = [
    [stabilized_rise[j] for j in range(i, i + window_size)]
    for i in range(len(stabilized_rise) - window_size + 1)
]

variance_peaks = []
for window in deviation_windows:
    mean_w = sum(window) / len(window)
    var = sum((x - mean_w) ** 2 for x in window) / len(window)
    variance_peaks.append(round(var, 3))

# Use itertools to generate phase shifts (looks complex, minimal impact)
phases = list(itertools.accumulate([0.1] * len(variance_peaks), lambda a, b: (a + b) % 1.0))
modulated_peaks = [vp + p for vp, p in zip(variance_peaks, phases)]

# Threshold determined from median of modulated peaks (distractor)
threshold_guess = sorted(modulated_peaks)[len(modulated_peaks)//2]

# Real transformation: apply logarithmic compression to original rising segments
compressed_signal = [round(x * 0.87 for x in stabilized_rise], 2)

# Add string-based metadata tagging (irrelevant but plausible)
tags = ['sensor_A', 'valid', 'primary']
status_flag = '_'.join(tag.upper() for tag in tags if 'A' in tag)

# Transform into grouped quartiles for analysis
quartile_groups = [
    compressed_signal[i:i+3] for i in range(0, len(compressed_signal), 3)
]

# Compute inter-quartile balance (misleading metric)
balances = []
for grp in quartile_groups:
    if len(grp) == 3:
        balance = (grp[2] - grp[0]) / grp[1] if grp[1] != 0 else 0
        balances.append(round(balance, 3))

# Actual core logic: find dominant frequency in compressed signal via gap counting
gap_modes = {}
for i in range(1, len(compressed_signal)):
    gap = round(compressed_signal[i] - compressed_signal[i-1], 2)
    gap_modes[gap] = gap_modes.get(gap, 0) + 1

dominant_gap = max(gap_modes, key=gap_modes.get) if gap_modes else 0.0

# Final transformation: map to diagnostic space
transformed_data = [
    int(round((x + dominant_gap) * 2.1)) for x in compressed_signal
]

# Threshold derived from initial data structure (non-obvious source)
threshold = len([x for x in data_stream if x > 35]) * 3

# Core analysis function: counts pattern matches above threshold
def analyze_pattern(seq, limit):
    count = 0
    for val in seq:
        if val > limit:
            count += 1
            if count > 5:
                break
    return count * limit // 2

# Execute critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result for evaluation
print(f"Result: {final_diagnostic}")