from collections import defaultdict
import math

# Simulated sensor data with noise and irrelevant entries
data_stream = [
    (1, 'temp', 23.5), (2, 'pressure', 101.3), (3, 'temp', 24.1),
    (4, 'humidity', 45.0), (5, 'temp', 22.8), (6, 'pressure', 102.1),
    (7, 'co2', 410), (8, 'temp', 25.3), (9, 'humidity', 47.2),
    (10, 'temp', 26.0), (11, 'pressure', 100.7), (12, 'temp', 24.9)
]

# Irrelevant mappings and decoy transformations
decoy_map = defaultdict(lambda: 0)
for i in range(5):
    for j in range(5):
        decoy_map[(i,j)] = (i ** j) % 7

# Noise injection function (never actually used)
def inject_noise(values, factor=0.1):
    return [v + random.uniform(-factor, factor) for v in values]

# Dead code path: Unused class with misleading complexity
class DataFilter:
    def __init__(self, method="moving_avg"):
        self.method = method
        self.buffer = []

    def apply(self, x):
        self.buffer.append(x)
        if len(self.buffer) > 3:
            self.buffer.pop(0)
        return sum(self.buffer) / len(self.buffer)

# Extract temperature readings above threshold (core logic hidden in distractions)
def extract_temperatures(data, min_id=0):
    temps = []
    for entry in data:
        record_id, sensor_type, value = entry
        if sensor_type == 'temp' and record_id >= min_id:
            temps.append(value)
    return temps

# Secondary processing with red herring operations
def transform_sequence(seq):
    transformed = []
    scaling_factor = 1.05
    offset = -0.5
    for val in seq:
        # Complex-looking but ultimately unused transformation
        temp_val = (val * scaling_factor) + offset
        temp_val = round(temp_val, 2)
        adjusted = temp_val + math.sin(math.pi * val / 180)  # Minor trig distraction
        transformed.append(adjusted)
    # But we actually just return original sequence with no change
    return seq  # Critical: returns unmodified seq

# Misleading aggregation that seems important but isn't used
misleading_stats = {}
temp_only = [v for _, t, v in data_stream if t == 'temp']
misleading_stats['range'] = max(temp_only) - min(temp_only)
misleading_stats['variance'] = sum((x - sum(temp_only)/len(temp_only))**2 for x in temp_only) / len(temp_only)

# Actual filtering step buried in setup
filtered_data = extract_temperatures(data_stream, min_id=3)

# Decoy statistical summary (looks important but unused)
summary = {}
summary['count'] = len(filtered_data)
summary['avg'] = sum(filtered_data) / len(filtered_data)
summary['peak'] = max(filtered_data)
summary['baseline'] = 20.0
summary['deviation'] = abs(summary['avg'] - summary['baseline'])

# Threshold logic with conditional expression twist
threshold = 24.0 if len(filtered_data) > 3 else 22.0

# Core processing function: combines arithmetic, boolean, and control flow
def process_signals(readings, limit):
    count_above = 0
    total = 0.0
    weights = [0.8, 1.0, 1.2, 1.1]  # Weighting scheme
    weight_index = 0
    
    for reading in readings:
        # Conditional expression used as weight selector
        weight = weights[weight_index] if reading < 25.0 else 1.3
        total += reading * weight
        
        # Boolean logic with short-circuit evaluation
        is_significant = reading >= limit
        is_stable = abs(reading - 24.5) < 1.5
        if is_significant and is_stable or reading > 25.5:
            count_above += 1
        
        weight_index = (weight_index + 1) % len(weights)
    
    # Composite calculation combining weighted sum and count
    adjustment = math.log(count_above + 1) if count_above > 0 else 0
    result = total - adjustment * 2.5
    
    # Dead code: unreachable branch due to logic
    if False and result < 0:
        result *= -1
    
    return int(round(result))

# Final execution point — key statement
final_output = process_signals(filtered_data, threshold)

# Print result as required
print(f"Target result: {final_output}")