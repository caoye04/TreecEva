import itertools

def preprocess_readings(readings):
    # Irrelevant preprocessing: transforms data in a way not used in final calculation
    filtered = [x for x in readings if x > 0.1]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return [round(x * 1.07, 4) for x in smoothed]  # Distractor transformation

def compute_efficiency_index(seq):
    # Dead function: looks important but unused
    return sum(x ** 0.5 for x in seq if x > 0.5)

def detect_anomalies(stream):
    # Complex but irrelevant anomaly detection with red herring logic
    anomalies = []
    for i, val in enumerate(stream):
        if val < 0.3:
            if i == 0 or stream[i-1] < 0.4:
                anomalies.append((i, val * 2.1))
    return [(idx, round(score, 3)) for idx, score in anomalies]  # Unused result

def calculate_entropy(data):
    # Decoy scientific computation
    from math import log
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [x / total for x in data]
    return round(-sum(p * log(p, 2) for p in probabilities if p > 0), 4)

def validate_signal_integrity(signal):
    # Looks critical but only returns boolean used in dead branch
    if len(signal) < 5:
        return False
    checksum = sum(itertools.islice(signal, 0, None, 2))
    return checksum > 1.5

def aggregate_metrics(dataset, threshold):
    # CORE FUNCTION - relevant logic begins here
    primary_values = [entry['output'] for entry in dataset]
    
    # Real transformation chain
    scaled = [x * 1.618 for x in primary_values]  # Golden ratio scaling
    adjusted = [x - 0.2 for x in scaled]
    
    # Conditional filtering based on threshold
    qualified = [val for val in adjusted if val > threshold * 1.8]
    
    # Real intermediate: statistical moment
    mean_val = sum(qualified) / len(qualified) if qualified else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in qualified) / len(qualified) if qualified else 0
    
    # Critical path: bit manipulation on length
    n = len(qualified)
    bit_shifted = (n << 3) - (n >> 1)  # Multiply by 8, subtract divide by 2
    
    # Final answer derived from mixed arithmetic and list logic
    magic_offset = 42.7
    final_score = bit_shifted * variance_proxy + magic_offset
    
    # Misleading side computation (unused)
    peak = max(primary_values) if primary_values else 0
    decay_chain = [peak / (2**i) for i in range(5)]
    
    return round(final_score, 4)

# Simulated turbine sensor data (real input source)
turbine_data = [
    {'id': 'T01', 'output': 0.48, 'temp': 78.2, 'vibration': 0.18},
    {'id': 'T02', 'output': 0.52, 'temp': 81.7, 'vibration': 0.21},
    {'id': 'T03', 'output': 0.61, 'temp': 85.0, 'vibration': 0.15},
    {'id': 'T04', 'output': 0.49, 'temp': 79.3, 'vibration': 0.23},
    {'id': 'T05', 'output': 0.73, 'temp': 83.1, 'vibration': 0.19},
    {'id': 'T06', 'output': 0.81, 'temp': 87.4, 'vibration': 0.25},
    {'id': 'T07', 'output': 0.66, 'temp': 82.9, 'vibration': 0.17},
    {'id': 'T08', 'output': 0.54, 'temp': 76.5, 'vibration': 0.20}
]

# Irrelevant global transformations
baseline = [d['output'] * 0.97 for d in turbine_data]
processed_baseline = preprocess_readings(baseline)
anomaly_report = detect_anomalies([d['vibration'] for d in turbine_data])

# Fake validation gate (never actually blocks anything)
signal_ok = validate_signal_integrity([d['temp'] for d in turbine_data])
if signal_ok:
    entropy = calculate_efficiency_index([d['output'] for d in turbine_data])
else:
    entropy = 0  # Dead branch, but distracts reasoning

# Key execution point
final_diagnostic = aggregate_metrics(turbine_data, threshold=0.75)
print(f"Result: {final_diagnostic}")