import math

# Simulated sensor data with noise and redundant metrics
data_stream = [127, 85, 150, 64, 200, 32, 175, 45, 190, 75, 160, 55]

def analyze_signal_strength(raw_values):
    # Irrelevant transformation: frequency analysis (unused later)
    frequencies = [abs(math.sin(x / 10.0)) for x in raw_values]
    avg_freq = sum(frequencies) / len(frequencies)
    
    # Distractor: unused signal categorization
    signal_classes = []
    for val in raw_values:
        if val > 150:
            signal_classes.append('strong')
        elif val > 100:
            signal_classes.append('moderate')
        else:
            signal_classes.append('weak')
    
    # Actual relevant processing path
    filtered = [x for x in raw_values if x > 100]  # Only high-amplitude signals matter
    normalized = [(x - 100) for x in filtered]  # Shift baseline
    return normalized

# Dead function: looks important but not used
def legacy_calibrate(data):
    return [d ^ 0xFF for d in data][::-1]

# Unused recursive smoothing (red herring)
def smooth_recursive(arr, depth=3):
    if depth == 0 or len(arr) < 2:
        return arr
    smoothed = [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1)]
    return smooth_recursive(smoothed, depth - 1)

# Bit manipulation decoy: simulates checksum but unused
def compute_checksum(values):
    chk = 0
    for v in values:
        chk = (chk ^ v) << 1
        if chk > 255:
            chk = chk ^ 0xFF
    return chk & 0xFF

# Real processing begins here
processed_data = analyze_signal_strength(data_stream)

# Simulate multiple feature extractions (only one is actually used)
def extract_features(signal):
    feature_set = {}
    
    # Distractor features
    feature_set['peak'] = max(signal) if signal else 0
    feature_set['entropy'] = sum([math.log(x+1) for x in signal])
    feature_set['parity_pattern'] = sum([1 for x in signal if x & 1])
    
    # Relevant feature: sum of squares modulo base
    feature_set['energy'] = sum([x * x for x in signal]) % 997
    
    # More red herrings
    feature_set['shift_product'] = 1
    for s in signal[:3]:
        feature_set['shift_product'] *= (s >> 2)
    
    return feature_set

features = extract_features(processed_data)

# Decoy dictionary mapping that looks like it's used
status_map = {
    0: 'idle',
    1: 'active',
    2: 'standby',
    997: 'critical'
}

# Critical calculation chain
base_energy = features['energy']
temp_offset = 0
for i, val in enumerate(processed_data):
    temp_offset += (val * (i + 1)) % 17

temp_offset = temp_offset % 89

# Another layer of distraction: unused state tracker
class StateTracker:
    def __init__(self):
        self.history = []
        self.threshold = 75
    
    def update(self, x):
        self.history.append(x > self.threshold)

tracker = StateTracker()
for v in processed_data:
    tracker.update(v)

# Core logic buried under noise
intermediate = (base_energy * 3) + (temp_offset * 2)

# Conditional expression with misleading branches
scaling_factor = 1.5 if len(processed_data) > 5 else 2.0
if sum(processed_data) < 300:
    scaling_factor = 1.0  # This branch is unreachable
else:
    scaling_factor = 1.75  # Actual path taken

# Final computation
final_score = int(intermediate * scaling_factor)

# Additional distractor: slicing operation on irrelevant list
snapshot = data_stream[::2]  # every second reading
snapshot_sum = sum(snapshot[:4])

# Unused bitwise cascade (looks complex but irrelevant)
bit_cascade = 0
for d in data_stream:
    bit_cascade |= d
    bit_cascade &= (bit_cascade ^ (d >> 3))

# Output only the target result
print(f"Target result: {final_score}")