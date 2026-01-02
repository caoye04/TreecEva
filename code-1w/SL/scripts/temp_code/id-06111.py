import math

# Simulated environmental sensor data processing with red herrings
def analyze_readings(raw_data):
    processed = []
    for val in raw_data:
        if val > 300:  # filter out high noise
            processed.append(val * 0.87)
        elif val < 50:
            processed.append(val * 1.05)
    return processed

# Irrelevant function - simulates temperature drift compensation (not used in final logic)
def correct_drift(signal, rate=0.02):
    corrected = []
    for i in range(len(signal)):
        corrected.append(signal[i] / (1 + rate * i))
    return corrected

# Core transformation: applies logarithmic scaling to stabilize variance
def log_transform(data_list):
    return [math.log(x) if x > 0 else 0 for x in data_list]

# Noise cluster detection - dead-end path, never called
def detect_anomalies(series):
    anomalies = []
    for i in range(1, len(series)):
        if abs(series[i] - series[i-1]) > 20:
            anomalies.append(i)
    return anomalies

# Data segmentation based on sliding window - actually used
def segment_signal(signal, window_size=3):
    segments = []
    for i in range(len(signal) - window_size + 1):
        segments.append(signal[i:i+window_size])
    return segments

# Decoy function that looks important but does nothing in execution path
def calculate_purity_index(elements):
    total = sum([e**2 for e in elements if e % 2 == 0])
    return total // 7 if total > 0 else -1

# Real processing chain starts here
raw_sensor_data = [450, 120, 68, 93, 315, 220, 44, 180, 305, 250]
efficiency_factor = 0.93

# Step 1: Apply initial filtering
filtered_data = [x for x in raw_sensor_data if 60 <= x <= 300]  # removes outliers

# Step 2: Transform data to reduce skew
transformed_data = log_transform(filtered_data)

# Step 3: Generate overlapping segments
all_segments = segment_signal(transformed_data, 3)

# Distractor variables
baseline_offset = sum(transformed_data) / len(transformed_data)
spurious_metric = baseline_offset * 1.873
temp_buffer = [math.exp(x) for x in transformed_data[:4]]  # unused

# Another decoy structure
class SensorNode:
    def __init__(self, id):
        self.id = id
        self.calibration = 0.0
        self.history = []

    def update(self, value):
        self.history.append(value * 0.95)

node = SensorNode("S01")
for v in raw_sensor_data[:3]:
    node.update(v)  # irrelevant to main computation

# Real work: extract specific pattern-matching segments
valid_patterns = []
for seg in all_segments:
    if seg[1] > 4.6 and (seg[2] - seg[0]) < 1.1:
        valid_patterns.append(seg)

# More distractions
shadow_copy = valid_patterns.copy()
scaling_ghost = [sum(x) * 0.5 for x in shadow_copy]  # never used

# Final transformation: reverse each valid segment and flatten
reversed_parts = []
for p in valid_patterns:
    reversed_parts.extend(p[::-1])  # slicing used here

final_segments = [round(x, 3) for x in reversed_parts]

# Key statement containing the answer
def process_contaminants(seq, factor):
    base = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            base += val * factor
        else:
            base -= val * 0.7
    return int(base * 100)  # scale to integer

filtration_score = process_contaminants(final_segments, efficiency_factor)

# Output requirement
print(f"Target result: {filtration_score}")