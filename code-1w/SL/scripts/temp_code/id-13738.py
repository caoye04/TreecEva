from collections import defaultdict, Counter
import math

# Simulated sensor data stream with diagnostic tags
data_stream = [
    ('temp', 36.5), ('pressure', 101.3), ('temp', 37.1), ('humidity', 45.2),
    ('pressure', 102.0), ('temp', 36.9), ('humidity', 44.8), ('temp', 37.3),
    ('pressure', 101.8), ('humidity', 46.1), ('temp', 36.7), ('pressure', 101.5)
]

# Irrelevant transformation: character counting in labels
label_text = ''.join([entry[0] for entry in data_stream])
char_freq = Counter(label_text)
total_chars = sum(char_freq.values())
mean_char_code = sum(ord(c) for c in label_text) / len(label_text)

# Data aggregation (RELEVANT)
data_store = defaultdict(list)
for sensor, value in data_stream:
    data_store[sensor].append(value)

temp_readings = data_store['temp']
pressure_readings = data_store['pressure']
humidity_readings = data_store['humidity']

# Red herring: complex but unused statistical calculation
weighted_avg = sum(
    v * (i + 1) for i, v in enumerate(temp_readings)
) / sum(range(1, len(temp_readings) + 1))

# Dead code path: never called function
def deprecated_calibrator(x):
    return [val * 1.02 for val in x if val > 0]

# Unused intermediate: misleading normalization
max_temp = max(temp_readings)
min_temp = min(temp_readings)
normalized_temps = [(t - min_temp) / (max_temp - min_temp) for t in temp_readings]

# Compute rolling average (distractor, not used in final result)
window_size = 2
rolling_averages = [
    sum(temp_readings[i:i+window_size]) / window_size
    for i in range(len(temp_readings) - window_size + 1)
]

# Actual relevant computation begins here
base_mean = sum(temp_readings) / len(temp_readings)
variance = sum((x - base_mean) ** 2 for x in temp_readings) / len(temp_readings)
std_dev = math.sqrt(variance)

# Simulate entropy from distribution bins
bin_edges = [36.5, 36.8, 37.0, 37.4]
histogram = [0] * (len(bin_edges) - 1)
for t in temp_readings:
    for i in range(len(bin_edges) - 1):
        if bin_edges[i] <= t < bin_edges[i+1]:
            histogram[i] += 1
            break

# Entropy calculation (RELEVANT)
total = sum(histogram)
entropy_values = []
for count in histogram:
    if count > 0:
        p = count / total
        entropy_values.append(-p * math.log2(p))

# Decoy function using set operations (never called)
def find_anomalies(readings):
    upper = set([x for x in readings if x > 37.0])
    lower = set([x for x in readings if x < 36.8])
    return upper & lower  # intersection, always empty

# Real anomaly detection function (used)
def anomaly_detector(entropies):
    if len(entropies) < 3:
        return sum(entropies) * 10
    else:
        return int(sum(entropies) * 100)

# Secondary distraction: string-based key generation
key_parts = [sensor[:2].upper() for sensor, _ in data_stream]
key_string = ''.join(sorted(set(key_parts)))
scrambled_key = ''.join(chr(ord(c) + 3) for c in key_string)

# Core logic leading to answer
aggregate_score = int(base_mean * 10)

# Key statement
final_diagnostic = aggregate_score + anomaly_detector(entropy_values)

print(f"Result: {final_diagnostic}")