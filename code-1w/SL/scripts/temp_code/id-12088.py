import math

# Simulate sensor data preprocessing with red herrings
def analyze_pattern(sequence):
    if len(sequence) == 0:
        return 0
    temp_sum = sum(x ** 0.5 for x in sequence if x > 0)
    normalization_factor = max(sequence) if sequence else 1
    return temp_sum / normalization_factor if normalization_factor != 0 else 0

def evaluate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings) if readings else 0
    return variance < 5

# Irrelevant auxiliary function (dead code path)
def deprecated_filter(data):
    filtered = []
    for item in data:
        if item & 1:  # Keep only odd numbers
            filtered.append(item >> 1)
    return filtered

# Core transformation chain
def transform_sequence(raw):
    shifted = [(x << 1) ^ 3 for x in raw]  # Bit manipulation misdirection
    amplified = [y * 1.5 for y in shifted]
    return [z for z in amplified if z % 2 == 0]  # Filter even values

def compute_baseline(signal):
    if not signal:
        return 0
    avg = sum(signal) / len(signal)
    adjusted = [val - avg for val in signal]
    return sum(abs(a) for a in adjusted)

def detect_anomalies(stream, limit):
    count = 0
    for i, val in enumerate(stream):
        if i % 3 == 0 and val > limit:
            count += 1
    return count > 2

# Distractor: Unused complex structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
    
    def fill(self, value):
        for i in range(self.size):
            self.buffer[i] = value ^ i

# Main processing pipeline
def process_signal(data, cutoff):
    if len(data) < 5:
        return -1
    
    # Step 1: Normalize using conditional expression
    base_ref = 100 if sum(data) > 0 else -100
    
    # Step 2: Apply non-linear transformation
    modified = [math.log(abs(d) + 1) * base_ref for d in data]
    
    # Step 3: Conditional filtering based on dynamic rule
    filtered = [m for m in modified if (m > cutoff) != (m < -cutoff)]
    
    # Step 4: Accumulate with offset
    accumulator = 0
    for idx, val in enumerate(filtered):
        adjustment = (idx & 1) * 2 - 1  # Alternating sign via bitwise
        accumulator += val * adjustment
    
    # Step 5: Final thresholding
    return accumulator if accumulator >= 0 else int(accumulator)

# Irrelevant global variables (distractors)
MAX_BUFFER_SIZE = 1024
temp_cache = {i: i**3 for i in range(10)}
status_flags = [False, True, False]

# Real input data
sensor_input = [4, -8, 15, 16, -23, 42]

# Dead code invocation (misleading)
deprecated_result = deprecated_filter(sensor_input)

# Signal transformation stage
transformed_data = transform_sequence(sensor_input)

# Phantom analysis (no impact on result)
valid_pattern = evaluate_stability(sensor_input)
anomaly_detected = detect_anomalies(transformed_data, 30)
baseline_score = compute_baseline(transformed_data)

# Threshold determination with conditional expression
threshold = 7.5 if len(transformed_data) > 4 else 12.0

# Critical execution point
final_output = process_signal(transformed_data, threshold)

# Output result
print(f"Target result: {final_output}")