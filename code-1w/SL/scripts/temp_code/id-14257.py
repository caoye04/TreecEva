from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw):    
    # Irrelevant transformation (distractor)
    inverted = [300 - x for x in raw if x > 50]
    smoothed = [sum(raw[i:i+3]) / 3 for i in range(len(raw) - 2)]  # Smoothing filter
    return smoothed

# Decoy function - never called
def decrypt_sequence(data):
    return [x ^ 255 for x in data]

# Another decoy: complex but unused computation
def spectral_analysis(seq):
    total_power = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            total_power += (seq[i] - seq[j]) ** 2
    return total_power

# Misleading intermediate calculation
baseline_offset = sum([i * 2 for i in range(10)]) // 4  # Dead-end value

# Real signal input (simulated readings)
sensor_readings = [12, 15, 22, 18, 30, 35, 28, 40, 38, 50, 55]

# Apply preprocessing
filtered = preprocess_signal(sensor_readings)

# Red herring: string manipulation unrelated to final result
log_tag = "SYS_DIAG_" + "".join([chr(97 + (x % 26)) for x in [100, 111, 103, 101]])
diag_header = log_tag.split('_')[1]

# Transform step with slicing and conditional expressions
extended = filtered + [max(filtered)] * 3
trimmed = extended[1:-1]  # Remove first and last
normalized = [round(x - min(trimmed), 2) for x in trimmed]

def analyze_pattern(data, limit):
    # Count frequency of rounded values
    freq = Counter([int(round(x)) for x in data])
    
    # Irrelevant dictionary accumulation
    stats = defaultdict(lambda: 0)
    for k, v in freq.items():
        if k > 20:
            stats['high'] += v
        elif k > 10:
            stats['medium'] += v
        else:
            stats['low'] += v
    
    # Core logic hidden among distractions
    peak = max(freq.keys())
    total_valid = sum(1 for x in data if x > limit)
    
    # Bitwise obfuscation of a simple condition (distractor)
    flag = (total_valid & 1) ^ 1 if peak > 15 else 0
    
    # Actual key computation: sum of normalized values above threshold, scaled
    core_sum = sum(x for x in data if x > limit)
    adjustment = len([x for x in data if x < limit / 2])
    
    # Final diagnostic is this deterministic scalar
    result = round(core_sum - adjustment, 2)
    
    # Dead assignment (distractor)
    result = result if result > 0 else 0
    
    return result

# Unused complex structure (distractor)
class DataBuffer:
    def __init__(self):
        self.buffer = []
        self.size = 1024

threshold = 12.5

# Additional misleading variable
auxiliary_metric = sum([i << 1 for i in range(5)]) / 3  # Never used beyond here

transformed_data = normalized if len(normalized) % 2 == 0 else normalized[::-1]

# Key statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")