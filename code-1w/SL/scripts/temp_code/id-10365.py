import math

# Simulated sensor array data (irrelevant structure)
sensor_matrix = [[i * j + 2 for j in range(5)] for i in range(6)]

# Unused calibration constants (distractors)
CALIBRATION_OFFSET_A = 0.872
CALIBRATION_OFFSET_B = -1.003
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256

# Real processing parameters
def preprocess_entry(val, mode):
    if mode == 'A':
        return val ** 0.5 if val > 0 else 0
    elif mode == 'B':
        return abs(val) * 0.1
    else:
        return val

def generate_checksum(sequence):
    # Complex but irrelevant checksum calculation (dead path)
    chk = 0
    for s in sequence:
        chk = (chk * 31 + hash(str(s))) % 10007
    return chk

def decode_sequence(raw):
    # Unused decoding logic (red herring)
    return [x ^ 0xAA for x in raw if isinstance(x, int)]

# Primary signal data (core input)
raw_readings = [16, -9, 25, 4, 0, 36, -16, 49]

# Signal transformation with conditional expression
processed_data = [preprocess_entry(x, 'A') if x >= 0 else preprocess_entry(x, 'B') for x in raw_readings]

# Irrelevant frequency analysis (distractor computation)
frequency_spectrum = [math.sin(i * 0.5) * math.cos(i * 0.25) for i in range(10)]
spectral_energy = sum([f ** 2 for f in frequency_spectrum])

# Decoy state machine (misleading complexity)
class StateProcessor:
    def __init__(self):
        self.state = 'IDLE'
        self.buffer = []
    
    def update(self, val):
        if self.state == 'IDLE' and val > 5:
            self.state = 'ACTIVE'
        elif self.state == 'ACTIVE' and val < 0:
            self.state = 'ERROR'

# Unused instance (distractor object)
processor_instance = StateProcessor()

# Threshold configuration map (critical for final result)
threshold_map = {
    'low': 2.0,
    'medium': 3.0,
    'high': 5.0
}

# Auxiliary counting function (used indirectly)
def count_exceeding(values, limit):
    return sum(1 for v in values if v > limit)

# Core analysis logic with nesting and conditional expressions
def analyze_signal(data, thresholds):
    count_low = count_exceeding(data, thresholds['low'])
    count_med = count_exceeding(data, thresholds['medium'])
    count_high = count_exceeding(data, thresholds['high'])
    
    # Complex decision tree with early returns
    if count_high > 3:
        category = 'SEVERE'
        scaling_factor = 3.0
    elif count_med > 4:
        category = 'MODERATE'
        scaling_factor = 1.8
    elif count_low > 5:
        category = 'MILD'
        scaling_factor = 0.9
    else:
        category = 'NORMAL'
        return 0  # Early exit (not taken here)
    
    # Secondary check with bit manipulation red herring
    flag_sum = 0
    for d in data:
        if d > 0:
            # Irrelevant bit operation chain
            temp_flag = (int(d) << 1) ^ 0xF
            temp_flag = (temp_flag >> 2) & 0x3
            flag_sum += temp_flag
    
    # Final diagnostic computed from real logic
    base_score = count_high * 7 + count_med * 3 + count_low * 1
    adjustment = math.log(base_score + 1) if base_score > 0 else 0
    
    # Key statement: what is the value of final_diagnostic?
    final_value = int((base_score + adjustment) * scaling_factor)
    
    # Multiple unused return candidates (misdirection)
    # return flag_sum  # decoy
    # return len(data) # decoy
    return final_value

# Execution flow with irrelevant pre-checks
valid_entries = [x for x in raw_readings if isinstance(x, int)]
duplicate_check = len(valid_entries) != len(set(abs(x) for x in valid_entries))

# Actual critical computation path
processed_data = [math.sqrt(x) if x >= 0 else abs(x) * 0.1 for x in raw_readings]  # redefined for clarity

# Final call that produces the answer
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")