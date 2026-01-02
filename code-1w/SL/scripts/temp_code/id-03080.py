import math

# Simulated sensor array data (real and decoy)
sensor_a = [1.2, 3.4, 2.5, 6.7, 4.1]
sensor_b = [0.9, 2.8, 3.6, 5.5, 6.2]
sensor_c = [1.1, 1.1, 1.1, 1.1]  # Red herring: constant values

# Irrelevant metadata
device_id = "SENS-9X"
firmware_version = "2.1.8"
last_calibration = "2023-06-15"

def normalize readings(data):
    mean = sum(data) / len(data)
    return [(x - mean) / mean for x in data]

def detect_peaks(signal, sensitivity=1.5):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > sensitivity * signal[i-1] and signal[i] > sensitivity * signal[i+1]:
            peaks.append(i)
    return peaks if peaks else [0]  # Avoid empty

def compute_entropy(data):
    # Decoy function – looks important but unused in critical path
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

def filter_outliers(data, factor=1.5):
    # Interquartile range filtering (distractor logic)
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def transform_coordinates(x, y):
    # Unused geometric transformation (red herring)
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r * math.cos(2*theta), r * math.sin(2*theta)

def rolling_window_average(data, window_size=3):
    if len(data) < window_size:
        return data
    averages = []
    for i in range(len(data) - window_size + 1):
        averages.append(sum(data[i:i+window_size]) / window_size)
    return averages

def generate_signature(sequence):
    # Creates a hash-like value using bit manipulation (misleading intermediate)
    sig = 0
    for val in sequence:
        sig ^= int(val * 100) << 2
        sig &= 0xFFFF  # Clamp to 16 bits
        sig = (sig >> 1) | (sig << 15)  # Rotate right
    return sig

def validate_checksum(data):
    # Looks critical but only used in dead branch
    return sum(int(d * 10) for d in data) % 256

# Data fusion pipeline
raw_data = [sensor_a[i] + sensor_b[i] for i in range(min(len(sensor_a), len(sensor_b)))]

# Apply normalization
normalized = normalize_readings(raw_data)

# Rolling average smoothing
smoothed = rolling_window_average(normalized, 2)

# Decoy conditional with early exit that never triggers
system_status = "ACTIVE"
if system_status == "DEGRADED":
    fallback_data = [x * 0.5 for x in smoothed]
    entropy_val = compute_entropy(fallback_data)
    if entropy_val > 1.0:
        final_diagnostic = -999
        print("Result:", final_diagnostic)
        exit()

# Real processing begins here
processed_data = [abs(x) for x in smoothed if x > -1.0]  # Filter small negatives

# Threshold configuration map (used later)
threshold_map = {
    'low': 0.15,
    'medium': 0.35,
    'high': 0.65
}

# Simulate fault pattern detection using list comprehension and set logic
def analyze_signal(data, thresholds):
    high_t = thresholds['high']
    mid_t = thresholds['medium']

    # Identify critical segments
    critical_indices = {i for i, x in enumerate(data) if x > high_t}
    warning_indices = {i for i, x in enumerate(data) if mid_t < x <= high_t}

    # Cross-reference with peak detection
    raw_indices = detect_peaks(data, sensitivity=1.1)
    confirmed_critical = critical_indices.intersection(set(raw_indices))

    # Compute impact score using arithmetic and bit operations
    base_score = sum(int(x * 100) for x in data)
    penalty = len(warning_indices) * 15
    bonus = len(confirmed_critical) * 50 if confirmed_critical else 0

    # Final diagnostic calculation
    raw_diagnostic = base_score - penalty + bonus

    # Bit manipulation layer (obscures reasoning)
    shifted = (raw_diagnostic << 2)
    masked = shifted & 0xFFFFFF  # Trim to 24 bits
    flipped = masked ^ 0xAAAA  # XOR mask
    adjusted = flipped - (flipped >> 4)  # Arithmetic adjustment

    # Final clamp and scaling
    if adjusted > 10000:
        adjusted = adjusted % 9999

    return float(adjusted)

# Key execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)
print("Target result:", final_diagnostic)