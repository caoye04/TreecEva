import math

# Simulated sensor data with noise and redundant metadata
data_stream = list(range(100, 200, 3)) + [0] * 5 + list(range(300, 310))

# Irrelevant calibration constants (distractors)
calib_a = 0.87
calib_b = 1.03
calib_c = 42.0
offset_table = {i: (i ** 0.5) for i in range(1, 10)}

# Decoy function - looks important but unused
def apply_calibration(x):
    return x * calib_b + calib_a

# Noise filter using lambda and list comprehension (partially relevant)
filtered_noise = list(map(lambda x: x if x < 250 else 0, data_stream))
valid_entries = [x for x in filtered_noise if x != 0]

# Dummy transformation chain (red herring)
shifted_data = [x - 90 for x in valid_entries if x > 150]
decoded_signal = []
for val in shifted_data:
    if val % 2 == 0:
        decoded_signal.append(int(math.sqrt(val) * 10))

# Core processing pipeline (relevant)
def transform_value(x):
    if x < 120:
        return (x ** 2) // 10
    elif x < 180:
        return (x * 3) - 50
    else:
        return int(math.log(x, 2)) * 15

def aggregate_values(vals):
    total = 0
    for i, v in enumerate(vals):
        if i % 3 == 0:
            total += v // 2
        elif i % 3 == 1:
            total += v
        else:
            total -= v % 7
    return abs(total)

# Another decoy: complex but unused data structure
class SignalBuffer:
    def __init__(self, size):
        self.buffer = [0] * size
        self.ptr = 0
    
    def append(self, x):
        self.buffer[self.ptr] = x
        self.ptr = (self.ptr + 1) % len(self.buffer)

buffer = SignalBuffer(10)
for x in data_stream[:10]:
    buffer.append(x ^ 7)  # Bitwise red herring

# Actual used processing functions
def preprocess_chunk(chunk):
    # Mix of arithmetic and filtering
    processed = []
    for item in chunk:
        temp = item
        if temp > 100:
            temp = (temp + 5) | 3  # Bit manipulation distraction
            temp = temp & ~1  # Clear least significant bit
        processed.append(temp - 4)
    return processed

def compute_checksum(arr):
    # Checksum with modular arithmetic and conditional logic
    chk = 0
    for idx, val in enumerate(arr):
        if val == 0:
            continue
        if idx % 4 == 0:
            chk += val * 2
        elif idx % 4 == 2:
            chk -= val // 3
        else:
            chk ^= val % 19
    return chk % 10000

# Main pipeline combining multiple concepts
def process_pipeline(input_data):
    # Step 1: Preprocess
    step1 = preprocess_chunk(input_data)
    
    # Step 2: Transform values
    step2 = [transform_value(x) for x in step1 if x % 4 != 0]  # List comprehension
    
    # Step 3: Aggregate
    step3 = aggregate_values(step2)
    
    # Step 4: Compute checksum (this modifies flow meaningfully)
    chk_val = compute_checksum(step2)
    
    # Step 5: Final adjustment with logical condition
    if chk_val > step3:
        final = (chk_val - step3) * 3
    else:
        final = (step3 + chk_val) // 2
    
    # Dead code path - never executed due to data constraints
    if False and len(step2) > 1000:
        backup = sum(step2) / len(step2)
        final = int(backup)
    
    return final

# Execute main logic
temp_result = process_pipeline(data_stream)

# Misleading intermediate assignment (not the answer)
interim_flag = any(x > 1000 for x in [temp_result, calib_c])

# Critical statement
final_output = temp_result

# Output result
print(f"Result: {final_output}")