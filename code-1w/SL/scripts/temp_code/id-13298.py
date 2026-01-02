import math

# Simulated sensor data preprocessing with multiple red herrings
def fetch_raw_readings():
    readings = [i * 0.7 + abs(math.sin(i)) for i in range(15)]
    offset = 2.3
    adjusted = [r + offset for r in readings]
    return adjusted

# Irrelevant transformation - decoy function
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 1.0:
            total -= x * math.log(x)
    return round(total, 4)

# Real transformation: apply moving average filter
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        segment = signal[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    return smoothed

# Bit manipulation decoy - looks relevant but unused
def flag_encoder(value):
    encoded = 0
    for i in range(8):
        encoded |= (value & (1 << i)) << 2
    return encoded ^ 0xAA

# Data normalization (actually used later)
def normalize_sequence(seq):
    min_val, max_val = min(seq), max(seq)
    if max_val == min_val:
        return [0.0] * len(seq)
    return [(x - min_val) / (max_val - min_val) for x in seq]

# Misleading statistical analysis (dead code path)
def calculate_outlier_score(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val)**2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return 0
    return sum(1 for x in data if abs(x - mean_val) > 2 * std_dev)

# Core logic disguised among distractors
def detect_anomaly_cluster(pattern):
    count = 0
    for i in range(1, len(pattern)):
        if pattern[i] > pattern[i-1] and pattern[i] > 0.5:
            count += 1
    return count > 5

# Actual key processing function
def analyze_pattern(data, limit):
    temp_result = 0
    for val in data:
        if val < limit:
            temp_result += int(val * 10)
        else:
            temp_result -= int(val)
    # This condition is always true due to data distribution
    if len(data) % 2 == 1:
        temp_result = abs(temp_result) + 17
    return temp_result

# Unused recursive distraction
def fibonacci_threshold(n, cap=100):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
        if b > cap:
            break
    return b

# Main execution chain
raw_data = fetch_raw_readings()  # Initial data source

# Dead-end processing branch
entropy_value = compute_entropy(raw_data)
decoy_flags = [flag_encoder(i) for i in range(8)]
outlier_metric = calculate_outlier_score(raw_data)

# Relevant transformations
filtered_data = smooth_signal(raw_data)
normalized_data = normalize_sequence(filtered_data)
transformed_data = [math.cos(x) ** 2 for x in normalized_data]  # Squared cosine transform

# Threshold computed from irrelevant sequence
fib_limit = fibonacci_threshold(10)
threshold = 0.43  # Hardcoded based on domain knowledge

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output requirement
print(f"Result: {final_diagnostic}")