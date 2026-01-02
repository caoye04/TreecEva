import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_signal, noise_level, duration):
    return [base_signal * math.sin(t / 10) + noise_level * (t % 3 - 1) for t in range(duration)]

# Irrelevant utility: converts numeric levels to categorical tags
def level_to_category(value):
    if value > 1.5:
        return 'HIGH'
    elif value > 0.5:
        return 'MEDIUM'
    elif value > -0.5:
        return 'NORMAL'
    else:
        return 'LOW'

# Decoy function: appears useful but unused in critical path
def apply_calibration(data, factor=1.0):
    return [x * factor for x in data]

# Signal feature extraction (used)
def extract_peaks(signal, sensitivity=0.8):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > sensitivity:
            peaks.append(i)
    return peaks

# Data transformation via lambda and slicing (critical)
def slice_window(data, start, end):
    truncate = lambda seq, a, b: seq[a:b]
    return truncate(data, start, end)

# Boolean logic chain with set operations (critical)
def detect_anomalies(peaks, known_abnormal_positions, size_hint):
    suspicious = set()
    for p in peaks:
        if p in known_abnormal_positions:
            suspicious.add(p)
        elif p % 7 == 0 and size_hint > 5:
            suspicious.add(p)
    confirmed = suspicious.difference({p for p in suspicious if p % 2 == 1})  # remove odd-indexed anomalies
    return list(confirmed)

# Core analysis function (critical path)
def analyze_signal(buffer, threshold):
    length = len(buffer)
    
    # Step 1: Extract rising edges above threshold
    candidates = [i for i in range(1, length) if buffer[i] > threshold > buffer[i-1]]
    
    # Step 2: Use lambda-based transformation
    transform = lambda x: round(x * 2.5, 1)
    scaled = sum(transform(buffer[i]) for i in candidates)
    
    # Step 3: Slice middle portion for refinement
    mid_section = slice_window(buffer, length//4, 3*length//4)
    
    # Step 4: Find peaks in mid section
    peak_indices = extract_peaks(mid_section, sensitivity=threshold)
    
    # Step 5: Simulate reference anomaly map
    reference_map = {5, 10, 15, 20, 25}
    
    # Step 6: Detect anomalies using boolean and set logic
    valid_detections = detect_anomalies(peak_indices, reference_map, len(mid_section))
    
    # Step 7: Compute weighted contribution from detections
    weights = [buffer[idx + length//4] * 100 for idx in valid_detections]
    
    # Step 8: Final diagnostic score
    base_score = sum(weights) + scaled
    adjustment = math.log(abs(base_score) + 1) if base_score != 0 else 0
    final_score = int(base_score - adjustment)
    
    return final_score

# === Distractor Code Zone ===

# Unused variables with plausible names
baseline_correction = 0.987
reference_registry = {'A': 1, 'B': 2, 'C': 3}
calibration_matrix = [[1,0],[0,1]]

# Dead code path: looks like initialization but unused
initial_sync_pulse = [0.1, 0.2, 0.4, 0.8]
for i in range(len(initial_sync_pulse)):
    initial_sync_pulse[i] *= 1.1

# Fake post-processing block
redundant_flag = False
if redundant_flag:
    temp_result = None
    backup_chain = []
    for x in range(10):
        backup_chain.append(x ** 2)

# === Critical Execution Path ===
raw_signal = collect_samples(base_signal=2.1, noise_level=0.3, duration=60)
pattern_buffer = raw_signal[::3]  # every 3rd sample
filter_threshold = 0.75

# Key statement
final_diagnostic = analyze_signal(pattern_buffer, filter_threshold)

print(f"Result: {final_diagnostic}")