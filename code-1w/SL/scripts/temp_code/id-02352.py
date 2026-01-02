import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, count):
    return [baseline + math.sin(i * 0.5) * math.cos(i * 0.3) for i in range(count)]

def filter_noise(signal_list, factor=0.9):
    # Irrelevant smoothing function (dead code path)
    return [x * factor for x in signal_list]

def compute_entropy(data):
    # Misleading complexity: computes entropy but not used in final result
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

def extract_peaks(signal_seq):
    peaks = []
    for i in range(1, len(signal_seq) - 1):
        if signal_seq[i] > signal_seq[i-1] and signal_seq[i] > signal_seq[i+1]:
            peaks.append(signal_seq[i])
    return sorted(peaks, reverse=True)[:5]  # Top 5 peaks only

def transform_sequence(seq, multiplier):
    # Distractor transformation with unused result
    shifted = [(x * 1.1 + 2.5) ** 0.5 for x in seq]
    return [int(x * multiplier) for x in shifted]

def detect_anomalies(readings, limit):
    anomalies = []
    for val in readings:
        if abs(val) > limit:
            anomalies.append(val)
    return anomalies if len(anomalies) > 0 else [0]

# Unused recursive helper (red herring)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def calculate_checksum(items):
    # Decoy function that looks important but isn't used
    chk = 0
    for item in items:
        chk = (chk * 31 + int(abs(item))) % 10007
    return chk

# Core processing chain
raw_data = generate_signals(baseline=100.0, count=50)

# Dead assignment: transformed_data not used later
transformed_data = transform_sequence(raw_data, multiplier=1.75)

# Real processing begins here
noisy_readings = [x + math.cos(x * 0.2) * 0.8 for x in raw_data]

# Multiple distractor variables
entropy_value = compute_entropy(noisy_readings)  # Not used
checksum_value = calculate_checksum(noisy_readings)  # Not used
peak_magnitudes = extract_peaks(noisy_readings)  # Partially relevant

# Simulated calibration offset (irrelevant)
calibration_log = []
for step in range(3):
    adjustment = math.exp(-step) * 0.1
    calibration_log.append(adjustment)

# Actual critical data refinement
processed_data = []
for val in noisy_readings:
    adjusted = val - 100.0
    normalized = abs(adjusted) ** 1.5
    processed_data.append(normalized)

# Threshold logic with lambda abstraction (key concept)
thresh_limit = 50.0
threshold_func = lambda x: x > thresh_limit

# Secondary filter to mislead reasoning
anomaly_set = detect_anomalies(processed_data, limit=45.0)  # Computed but not decisive

# Critical analysis function
# Combines list comprehension, conditionals, and aggregation
def analyze_readings(data, thresholder):
    # List comprehension with filtering and transformation
    significant = [x for x in data if thresholder(x)]
    
    # Nested conditional logic with decoy branches
    if len(significant) == 0:
        return -1
    elif len(significant) > 10:
        # This block modifies behavior based on count
        clipped = [min(x, 200.0) for x in significant]
        base_score = sum(clipped) / len(clipped)
        bonus = 10 if any(x > 150 for x in clipped) else 0
        penalty = 5 if all(x < 180 for x in clipped) else 0
        return int(base_score + bonus - penalty)
    else:
        fallback = sum(significant) * 0.75
        return int(fallback)

# Final execution point
final_diagnostic = analyze_readings(processed_data, threshold_func)

# Output the required result
print(f"Result: {final_diagnostic}")