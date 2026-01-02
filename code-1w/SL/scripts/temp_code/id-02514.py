import math

# Simulated sensor data processing with red herrings and multiple layers

def preprocess_input(raw_samples):
    filtered = []
    noise_floor = 0.041
    gain_boost = 1.87
    for sample in raw_samples:
        if abs(sample) > noise_floor:
            filtered.append(sample * gain_boost)
    return filtered

# Irrelevant transformation - decoy function
def frequency_shift(signal, shift_by):
    return [math.sin(x + shift_by) for x in signal]

# Unused utility - dead code path
def compress_data(sequence):
    encoded = 0
    for i, val in enumerate(sequence):
        encoded ^= int(val * 100) << (i % 6)
    return encoded

# Distractor: complex but unused signal model
class SignalModel:
    def __init__(self):
        self.alpha = 0.3
        self.beta = 2.7
        self.state_history = []

    def update(self, x):
        y = self.alpha * x + self.beta * math.cos(x)
        self.state_history.append(y)
        return y

# Core logic buried under distractions
pattern_buffer = [0.1, -0.3, 0.7, -0.5, 0.9]
calibration_factor = 3
decoy_matrix = [[i*j for j in range(4)] for i in range(4)]  # Unused structure
phantom_counter = 0

for index, value in enumerate(pattern_buffer):
    if index % 2 == 0:
        pattern_buffer[index] = math.pow(abs(value), 1.5) * ((-1) ** index)
    else:
        temp_val = value << 1  # Bitwise red herring
        phantom_counter += temp_val  # Misleading accumulator

# Fake data transformation chain
aux_data = [x for x in zip(pattern_buffer, [calibration_factor]*len(pattern_buffer))]
scaled_aux = [a*b for a,b in aux_data]

# Real computation hidden among noise
def generate_baseline(n, factor):
    base = 0
    for i in range(1, n+1):
        base += math.log(i + factor) if i % 2 == 1 else math.exp(factor / i) / 100
    return base

# Secondary irrelevant calculation
entropy_score = 0
for i in range(len(pattern_buffer)-1):
    entropy_score += abs(pattern_buffer[i] - pattern_buffer[i+1])

# Critical function with mixed operations and distractors
def analyze_signal(signal, factor):
    # Local variables to increase cognitive load
    debug_trace = []
    intermediate = 0
    shift_register = 0
    
    for idx, val in enumerate(signal):
        # Mix of relevant and irrelevant ops
        shifted = val << 1 if idx % 3 == 0 else val
        masked = shifted & 0xFF if isinstance(shifted, int) else int(abs(shifted))
        
        # Only this line contributes to final result
        intermediate += math.sin(val * factor) * (idx + 1)
        
        # Dead logic branches
        if len(debug_trace) > 10:
            shift_register ^= masked
        debug_trace.append(masked)
    
    # Final computation involving modular arithmetic and trig
    residue = int(intermediate * 100) % 77
    checksum = 0
    for i in range(residue):
        checksum += math.cos(math.pi * i / 38.5)
    
    # The actual answer emerges here
    final_value = intermediate + (checksum / 1000)
    return round(final_value, 6)

# Decoy recursive call - never used
def recursive_denoise(arr, depth):
    if depth == 0 or len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return recursive_denoise(arr[:mid], depth-1) + recursive_denoise(arr[mid:], depth-1)

# Trigger the real computation
final_diagnostic = analyze_signal(pattern_buffer, calibration_factor)

# Output requirement
print(f"Target result: {final_diagnostic}")