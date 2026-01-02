import math

# Simulated sensor network diagnostic system
def collect_sensor_data():
    raw_values = [145, 203, 98, 176, 255, 34, 112]
    timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800, 1623456805, 1623456810]
    statuses = ['OK', 'ERROR', 'OK', 'WARNING', 'OK', 'ERROR', 'OK']
    return list(zip(raw_values, timestamps, statuses))


def filter_anomalies(data):
    filtered = []
    error_count = 0
    for val, ts, stat in data:
        if stat == 'ERROR':  # Irrelevant to final result
            error_count += 1
        if val > 100 and stat != 'WARNING':
            filtered.append(val)
    scaling_factor = 1.05
    adjusted = [int(x * scaling_factor) for x in filtered]  # Distractor: not used later
    return filtered


def transform_magnitude(x):
    if x < 150:
        return (x ** 2) >> 3  # Bit shift as transformation
    else:
        return int(math.log(x) * 10)


def generate_signature(seq):
    base_sig = 0
    for i, v in enumerate(seq):
        base_sig ^= (v + i) & 255  # Creates checksum, but irrelevant
    return base_sig

# Dead function - never called
def deprecated_analysis(arr):
    total = 0
    for item in arr:
        total += item % 7
    return total // 2

# Unused auxiliary computation
temp_offsets = [3, -1, 4, 2]
offset_map = {i: abs(o) ** 2 for i, o in enumerate(temp_offsets)}  # Complex distractor

processed_logs = []
sensor_data = collect_sensor_data()
valid_readings = filter_anomalies(sensor_data)

# Core transformation chain
transformed = []
for reading in valid_readings:
    transformed.append(transform_magnitude(reading))

# Multiple layers of processing with distractions
decoy_sum = sum([r for r in valid_readings if r < 200])  # Misleading sum
weight_matrix = [[1, 2], [3, 4]]
matrix_trace = weight_matrix[0][0] + weight_matrix[1][1]  # Irrelevant

# Real processing path begins here
aggregate = 0
for t in transformed:
    if t % 2 == 0:
        aggregate += t // 2
    else:
        aggregate -= t // 3

# Conditional expression mix
threshold = 128
primary_flag = 'HIGH' if aggregate > threshold else 'LOW'

# Data structure cross-reference distraction
status_counter = {'OK': 0, 'WARNING': 0, 'ERROR': 0}
for _, _, s in sensor_data:
    status_counter[s] += 1

# Set operation as per requirement
unique_transformed = set(transformed)
overlap_check = unique_transformed.intersection({16, 32, 64})  # Slight distraction

# List comprehension with filtering (required feature)
evaluated_nodes = [math.ceil(t / 4.3) for t in transformed if t > 15]

# Final analysis function
def analyze_readings(readings):
    if not readings:
        return -1
    
    # Multi-step internal logic
    magnitude_total = 0
    for r in readings:
        temp_val = r * 1.1
        if temp_val > 150:
            temp_val = math.sqrt(temp_val) * 8
        magnitude_total += int(temp_val) % 100
    
    # Secondary adjustment
    adjustment = len(readings) * 3
    intermediate = (magnitude_total + adjustment) // 2
    
    # Apply conditional correction
    correction = 7 if any(r % 17 == 0 for r in readings) else 11
    corrected = intermediate - correction
    
    # Final nonlinear mapping
    final_score = int((corrected ** 1.5) / 10)  # Produces deterministic scalar
    
    # Decoy return path (not taken)
    if False:
        return sum(transformed) % 1000  # Dead code
        
    return final_score

# Critical execution point
final_diagnostic = analyze_readings(processed_logs)
print(f"Result: {final_diagnostic}")