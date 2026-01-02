import math

# Simulated sensor data processing with embedded logic chain
def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper - distractor
def smooth_data(signal):
    if len(signal) < 2:
        return signal
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Core transformation with meaningful computation
def generate_sequence(base, length):
    seq = [base]
    for i in range(1, length):
        next_val = (seq[-1] * 1.7 + 2.3) % 100
        seq.append(round(next_val, 3))
    return seq

# Decoy function - never called
def legacy_compatibility(data):
    temp_store = {}
    for idx, val in enumerate(data):
        temp_store[f'item_{idx}'] = val ^ int(val * 3) & 255
    return sum(temp_store.values()) >> 4

# Bit manipulation layer - relevant only in part
def encode_flags(mode, level, active):
    flag = 0
    flag |= (mode & 0b111) << 5
    flag |= (level & 0b1111) << 1
    flag |= (1 if active else 0)
    return flag

# Unused complex structure - red herring
class DiagnosticBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0.0] * size
        self.index = 0
    
    def append(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.size
    
    def get_stats(self):
        return {
            'min': min(self.buffer),
            'max': max(self.buffer),
            'avg': sum(self.buffer) / len(self.buffer)
        }

# Central analysis logic - partially dependent on prior steps
def transform_sequence(seq, modifier):
    shifted = [(v * modifier) % 64 for v in seq]
    # Introduce list comprehension with filtering
    processed = [x for x in shifted if x > 10 and (x & 7) == (len(seq) % 8)]
    return processed

# Higher-order logic with conditional branching
def evaluate_stability(metrics, tolerance=0.05):
    if not metrics:
        return False
    avg = sum(metrics) / len(metrics)
    variance = sum((m - avg) ** 2 for m in metrics) / len(metrics)
    return variance < tolerance

# Main pattern analyzer - contains critical answer path
def analyze_pattern(data, threshold):
    # Step 1: Aggregate base value
    aggregate = sum(abs(d) for d in data) / len(data)
    
    # Step 2: Apply threshold logic
    if aggregate < threshold:
        adjustment = 0.6
    else:
        adjustment = 1.4
    
    # Step 3: Complex conditional with bitwise twist
    meta_flag = 0
    for d in data:
        meta_flag ^= int(abs(d) * 10) & 0xF
    
    # Step 4: Final composition
    if meta_flag % 3 == 0:
        result = (aggregate * adjustment * 123) + (meta_flag * 7)
    elif meta_flag % 3 == 1:
        result = (aggregate * adjustment * 97) - (meta_flag * 5)
    else:
        result = (aggregate * adjustment * 111) + (meta_flag % 17)
    
    return int(round(result))

# === EXECUTION FLOW WITH DISTRACTIONS ===

# Irrelevant initialization - dead path
buffer_mgr = DiagnosticBuffer(16)
for k in range(10):
    buffer_mgr.append(k * 0.73)

# Real input generation
raw_sensor_data = generate_sequence(base=7.2, length=15)

# Real preprocessing
filtered_data = preprocess_signal(raw_sensor_data)

# Real transformation - used later
transformed_data = transform_sequence(filtered_data, modifier=3.1)

# Fake diagnostic check - misleading intermediate
stability = evaluate_stability([x / max(transformed_data) for x in transformed_data if x > 5])

# Dummy flag creation - irrelevant but plausible
system_flag = encode_flags(mode=5, level=12, active=True)

# Key threshold derived from multiple sources
key_threshold = (len(filtered_data) + system_flag % 10) / 15.0

# CRITICAL STATEMENT
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Output required result
print(f"Result: {final_diagnostic}")