import math

# Simulated sensor data processing with embedded logic chain
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 150]
    offset = 27
    adjusted = [y + offset for y in filtered]
    return adjusted

# Irrelevant helper (distractor)
def smooth_signal(signal):
    if len(signal) == 0:
        return []
    smoothed = [signal[0]]
    for i in range(1, len(signal)):
        smoothed.append(int(0.7 * signal[i] + 0.3 * smoothed[-1]))
    return smoothed

# Core transformation function
def encode_sequence(data_chunk, base_shift):
    encoded = []
    for i, val in enumerate(data_chunk):
        temp = (val ^ i) + base_shift  # XOR with index
        temp = (temp * 3) % 97
        encoded.append(temp)
    return encoded

# Decoy function - never called
def legacy_compatibility(data):
    accumulator = 0
    for item in data:
        accumulator += (item % 11) ** 2
    return accumulator % 1000

# Matrix-based transformation
key_matrix = [
    [2, 3, 1],
    [0, 1, 4],
    [5, 1, 2]
]

# Another red herring: complex but unused structure
class DiagnosticBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.ptr = 0
    
    def append(self, val):
        self.buffer[self.ptr] = val % 100
        self.ptr = (self.ptr + 1) % self.size
    
    def get_stats(self):
        non_zero = [x for x in self.buffer if x != 0]
        return sum(non_zero), len(non_zero)

# Unused instance (distractor)
diag_buffer = DiagnosticBuffer(10)
for k in range(15):
    diag_buffer.append(k * 13)

# Real data flow begins here
raw_sensor_data = [42, -65, 88, 105, -200, 73, 91, 33, 150, 67]

# Step 1: Filter and adjust
cleaned_data = preprocess_readings(raw_sensor_data)

# Step 2: Apply encoding with shifting
coded_data = encode_sequence(cleaned_data, base_shift=13)

# Step 3: Transform via modular dynamics
def transform_sequence(seq):
    result = []
    rolling_sum = 0
    for idx, num in enumerate(seq):
        if idx % 2 == 0:
            rolled = (num + rolling_sum) % 50
            result.append(rolled)
            rolling_sum += num
        else:
            alt = (num * 2) % 41
            result.append(alt)
    return result

transformed_data = transform_sequence(coded_data)

# Misleading intermediate computation (dead path)
temporary_digest = 0
for val in transformed_data:
    temporary_digest += (val * 7) % 13
temporary_digest = temporary_digest % 89

# Another decoy list comprehension with no effect
shadow_copy = [x for x in transformed_data if x % 3 == 0 and x > 10]
shadow_copy = [x * 2 for x in shadow_copy]  # Never used again

# Actual analysis function that computes the answer
def analyze_pattern(seq, matrix):
    # Extract 3-element kernel from seq
    kernel = seq[:3]
    
    # Compute weighted combination using first row of matrix
    weighted_sum = 0
    for i in range(len(kernel)):
        weighted_sum += kernel[i] * matrix[0][i]
    
    # Secondary check: count high-frequency transitions
    transitions = 0
    for j in range(1, len(seq)):
        if abs(seq[j] - seq[j-1]) > 20:
            transitions += 1
    
    # Apply trigonometric modulation based on transition count
    angle = transitions * math.pi / 8
    modulator = math.cos(angle) if transitions % 2 == 0 else math.sin(angle)
    
    # Final diagnostic is weighted sum adjusted by modulator
    final_value = weighted_sum * modulator
    
    # Additional logic: if more than 4 transitions, add bonus
    if transitions > 4:
        final_value += 17.5
    
    return round(final_value, 6)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_matrix)

print(f"Target result: {final_diagnostic}")