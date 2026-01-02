import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3, 7, 1, 9, 5, 11, 2, 8]
offset_calibration = 0.5
smoothing_factor = 0.2

# Irrelevant transformation (distractor)
def deprecated_filter(data):
    return [x * 0.9 for x in data if x > 5]

def apply_window(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window_avg = sum(signal[start:end]) / (end - start)
        smoothed.append(window_avg)
    return smoothed

def recursive_transform(seq, depth=0):
    if depth >= 3:
        return seq
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(int(math.sqrt(val)) if val > 0 else 0)
    return recursive_transform(transformed, depth + 1)

def detect_anomalies(series, limit=6):
    anomalies = []
    for idx, point in enumerate(series):
        if point > limit and idx % 2 == 1:
            anomalies.append((idx, point))
    return anomalies  # Unused return (red herring)

def compute_entropy(values):
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def analyze_pattern(data, cutoff):
    scores = []
    for i, (index, value) in enumerate(zip(range(len(data)), data)):
        if value < cutoff:
            score = value * (i + 1)
        else:
            score = value + (i * 2)
        scores.append(score)
    return sum(scores) // len(scores) if scores else 0

# Dead code path (unused function)
def legacy_analysis(arr):
    result = 0
    for x in arr:
        result ^= x
    return result

# Real processing begins here
filtered_data = [x + offset_calibration for x in raw_readings]
scaled_data = [int(x * smoothing_factor) for x in filtered_data]  # Loses precision intentionally
processed_signal = apply_window(scaled_data, window_size=2)

# Misleading intermediate (looks important but unused in final result)
entropy_diagnostic = compute_entropy(processed_signal)
anomaly_list = detect_anomalies(processed_signal, limit=3)

# Core transformation used in answer
decoded_sequence = []
temp_shift = 0
for i, val in enumerate(processed_signal):
    temp_shift += val % 3
    decoded_sequence.append(int(val) + temp_shift)

decoded_sequence.reverse()  # Reverse order
transformed_data = recursive_transform(decoded_sequence[:4])  # Only first 4 elements used

# Unused variables (distractors)
baseline_reference = sum(decoded_sequence) / len(decoded_sequence)
peak_magnitude = max(decoded_sequence)
correlation_matrix = [[i * j for j in range(3)] for i in range(3)]

threshold = 4
temp_result = [x for x in transformed_data if x > 2]
final_diagnostic = analyze_pattern(transformed_data, threshold)
print(f"Result: {final_diagnostic}")