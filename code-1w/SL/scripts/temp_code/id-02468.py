from collections import defaultdict, Counter
import math

# Simulated sensor array data with metadata
data_stream = [
    {'id': 'S1', 'val': 85, 'type': 'temp', 'status': 'active'},
    {'id': 'S2', 'val': 45, 'type': 'pressure', 'status': 'active'},
    {'id': 'S3', 'val': 90, 'type': 'temp', 'status': 'active'},
    {'id': 'S4', 'val': 30, 'type': 'pressure', 'status': 'inactive'},
    {'id': 'S5', 'val': 75, 'type': 'temp', 'status': 'active'},
    {'id': 'S6', 'val': 50, 'type': 'flow', 'status': 'active'},
    {'id': 'S7', 'val': 80, 'type': 'temp', 'status': 'active'},
    {'id': 'S8', 'val': 40, 'type': 'pressure', 'status': 'active'},
]

# Irrelevant helper: counts status types (not used in final result)
def count_status_types(stream):
    counter = defaultdict(int)
    for entry in stream:
        counter[entry['status']] += 1
    return counter

# Misleading transformation: applies arbitrary scaling to pressure sensors
def scale_pressure_values(stream):
    scaled = []
    for entry in stream:
        if entry['type'] == 'pressure':
            scaled.append({**entry, 'val': entry['val'] * 1.5})
        else:
            scaled.append(entry)
    return scaled

# Decoy function: performs bitwise analysis on sensor IDs (not used)
def analyze_sensor_id_bits(stream):
    bit_analysis = {}
    for entry in stream:
        sensor_id = entry['id']
        numeric_part = int(sensor_id[1:])
        bit_count = bin(numeric_part).count('1')
        bit_analysis[sensor_id] = bit_count
    return bit_analysis

# Core logic: filter active temperature sensors above threshold
def filter_high_temp_active_sensors(stream, threshold=75):
    filtered = []
    for entry in stream:
        if entry['type'] == 'temp' and entry['status'] == 'active' and entry['val'] > threshold:
            filtered.append(entry['val'])
    return filtered

# Secondary processing: apply logarithmic compression and average
compression_func = lambda x: math.log(x) * 1.2

def process_readings(readings):
    compressed = [compression_func(val) for val in readings]
    return sum(compressed) / len(compressed)

# Irrelevant aggregation: group by type (dead code path)
def aggregate_by_type(stream):
    groups = defaultdict(list)
    for entry in stream:
        groups[entry['type']].append(entry['val'])
    return {k: sum(v)/len(v) for k, v in groups.items()}

# Unused statistical check: detects outliers using IQR (distractor)
def detect_outliers(values):
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
    return [v for v in values if v < lower or v > upper]

# Spurious data transformation chain
transform_chain = [
    lambda x: x + 5,
    lambda x: x * 0.9,
    lambda x: x - 2
]

tempered_data = [transform_chain[2](transform_chain[1](transform_chain[0](v))) for v in range(10, 50, 10)]  # Unused

# Key execution steps
status_counts = count_status_types(data_stream)  # Irrelevant
scaled_data = scale_pressure_values(data_stream)  # Red herring
id_bit_analysis = analyze_sensor_id_bits(data_stream)  # Dead end

filtered_data = filter_high_temp_active_sensors(data_stream, threshold=75)

# Aggregate stats (unused)
avg_by_type = aggregate_by_type(data_stream)

# Outlier detection on wrong data (misleading)
pressure_vals = [d['val'] for d in data_stream if d['type'] == 'pressure']
detected_pressure_outliers = detect_outliers(pressure_vals)

# Critical statement
final_diagnostic = process_readings(filtered_data)

print(f"Result: {final_diagnostic}")