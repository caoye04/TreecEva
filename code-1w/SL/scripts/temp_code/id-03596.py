from collections import defaultdict, Counter
import math

# Simulated sensor array data (irrelevant in part)
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
base_offsets = {'S1': 12.5, 'S2': -8.3, 'S3': 0.0, 'S4': 17.2, 'S5': -3.1}
raw_readings = [105, 203, 155, 98, 201, 142, 111, 198, 134, 102]

# Irrelevant signal transformation branch
def apply_filter(signal_list, kernel_size=3):
    smoothed = []
    for i in range(len(signal_list)):
        start = max(0, i - kernel_size // 2)
        end = min(len(signal_list), i + kernel_size // 2 + 1)
        window = signal_list[start:end]
        smoothed.append(sum(window) / len(window))
    return [round(x) for x in smoothed]  # Never used

def transform_signal(signal):
    return [math.sin(x / 10.0) * 2.5 for x in signal]  # Unused path

# Core processing chain
def extract_patterns(data):
    counts = defaultdict(int)
    for val in data:
        if val > 100:
            counts['high'] += 1
        elif val > 50:
            counts['medium'] += 1
        else:
            counts['low'] += 1
    return dict(counts)

def compute_entropy(count_dict):
    total = sum(count_dict.values())
    entropy = 0.0
    for count in count_dict.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def flag_anomalies(seq):
    anomalies = []
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > 50:
            anomalies.append((i-1, i))
    return anomalies  # Computed but not used later

def rolling_average(data, window_size=2):
    averages = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        averages.append(avg)
    return averages

def detect_peaks(values, threshold=150):
    return [i for i, v in enumerate(values) if v >= threshold]

def shift_sequence(seq, amount):
    amount = amount % len(seq)
    return seq[amount:] + seq[:amount]  # Unused distraction

def compress_data(seq):
    if not seq:
        return []
    compressed = [seq[0]]
    for x in seq[1:]:
        if x != compressed[-1]:
            compressed.append(x)
    return compressed  # Dead-end function

def validate_integrity(arr):
    checksum = sum(arr) % 100
    return checksum < 50  # Always true here, distractor logic

# Primary pipeline functions
def preprocess(raw):
    doubled = [x * 2 for x in raw]
    adjusted = [x - 100 for x in doubled]
    return [x for x in adjusted if x > 0]

def aggregate_metrics(cleaned):
    total = sum(cleaned)
    peak_count = len([x for x in cleaned if x >= 100])
    avg_val = total / len(cleaned) if cleaned else 0
    max_val = max(cleaned) if cleaned else 0
    return {
        'sum': total,
        'peaks': peak_count,
        'mean': avg_val,
        'max': max_val
    }

def calculate_diagnostic(metrics):
    base_score = metrics['sum'] * 0.1
    adjustment = (metrics['peaks'] * 5) - (metrics['mean'] / 10)
    if metrics['max'] > 150:
        adjustment += 10
    return int(base_score + adjustment)

def analyze_readings(data):
    processed = preprocess(data)
    features = aggregate_metrics(processed)
    grade = calculate_diagnostic(features)
    return grade

# Red herring variables
filtered_data = apply_filter(raw_readings)
transformed = transform_signal(raw_readings)
anomaly_list = flag_anomalies(raw_readings)
moving_avgs = rolling_average(raw_readings)
peak_indices = detect_peaks(raw_readings)
reordered = shift_sequence(raw_readings, 3)
compressed_result = compress_data(raw_readings)

# Relevant pattern extraction (used in side calculation)
pattern_freq = extract_patterns(raw_readings)
entropy_value = compute_entropy(pattern_freq)

# Actual execution path
processed_signals = [x for x in raw_readings if x % 2 == 1]  # Keep odd values
final_diagnostic = analyze_readings(processed_signals)

# Side computation with no effect (distractor)
baseline_check = validate_integrity([10, 20, 30, 40])
reference_shift = [x - 5 for x in moving_avgs if x > 100]

print(f"Result: {final_diagnostic}")