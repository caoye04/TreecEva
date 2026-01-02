import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(raw):    
    offset = 0.73
    scale = 1.85
    adjusted = [(x * scale + offset) for x in raw]
    filtered = [x for x in adjusted if x > 1.0]  # Irrelevant filtering
    return adjusted

# Distractor function – never called
def legacy_calibrate(data):
    return [math.sin(x) * 0.5 for x in data]

# Real transformation: applies modular arithmetic and bit manipulation
def transform_signal(sequence):
    mod_base = 7
    shifted = []
    for i, val in enumerate(sequence):
        temp = (val ** 2) % mod_base
        if i % 2 == 0:
            temp = temp ^ 3  # XOR operation on even indices
        shifted.append(temp)
    return shifted

# Secondary distractor: complex but unused structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
    
    def fill(self, val):
        self.buffer = [val] * self.size

# Another red herring: calculates checksum but not used in final path
def compute_checksum(arr):
    chk = 0
    for x in arr:
        chk = (chk + x) % 256
    return chk

# Core analysis logic — depends on prior transformations
def analyze_pattern(data, limit):
    count = 0
    total = 0.0
    for x in data:
        if x & 1:  # Check if odd (bitwise)
            count += 1
        total += math.sqrt(x + 1)  # Use of advanced arithmetic
    
    # Complex condition with short-circuiting
    adjustment = count * 1.5 if count > limit else (count ** 2) / 2.0 if count > 0 else 0
    
    # Final computation
    result = int(total - adjustment)
    return result

# Main execution flow
if __name__ == "__main__":
    # Initial dataset
    readings = [2, 3, 1, 4, 5]
    
    # Step 1: Preprocess with scaling (includes irrelevant filter)
    processed = preprocess_sensor_readings(readings)
    
    # Step 2: Transform using modular and bitwise logic
    transformed_data = transform_signal(processed)
    
    # Irrelevant object instantiation (dead code path)
    buffer = DataBuffer(10)
    buffer.fill(7)
    
    # Unused checksum calculation (distractor)
    checksum = compute_checksum(transformed_data)
    
    # Threshold logic based on length
    threshold = len(transformed_data) // 3
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")