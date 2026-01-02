import itertools

# Simulated sensor data processing pipeline with red herrings
raw_readings = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Irrelevant transformation: frequency analysis (dead end)
frequencies = {}
for val in raw_readings:
    frequencies[val] = frequencies.get(val, 0) + 1

# Distractor: unused statistical functions
def calculate_skew(data):
    n = len(data)
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    return sum((x - mean_val) ** 3 for x in data) / (n * variance ** 1.5)

def calculate_kurtosis(data):
    n = len(data)
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    return sum((x - mean_val) ** 4 for x in data) / (n * variance ** 2) - 3

# Unused recursive smoothing (decoy function)
def smooth_recursive(signal, depth=0):
    if depth >= 3 or len(signal) < 2:
        return signal
    smoothed = [(signal[i] + signal[i+1]) / 2 for i in range(len(signal)-1)]
    return smooth_recursive(smoothed, depth + 1)

# Real processing path begins here
offset_correction = sum(raw_readings[:3]) - sum(raw_readings[-3:])
corrected_data = [x + offset_correction for x in raw_readings]

# Misleading intermediate: checksum that looks important but isn't used later
data_checksum = sum(x * (i + 1) for i, x in enumerate(corrected_data)) % 10007

# Signal slicing and windowing (actual relevant step)
signal_windows = [corrected_data[i:i+4] for i in range(0, len(corrected_data)-3, 2)]

# Apply transformation: XOR-based folding
transformed_data = []
for window in signal_windows:
    folded = 0
    for val in window:
        folded ^= (val * 2)  # Bit manipulation twist
    transformed_data.append(folded)

# Decoy list comprehension with no side effects
_ = [x for x in itertools.combinations(transformed_data, 3) if sum(x) % 2 == 0]

# Conditional expression chain (short-circuit red herring)
threshold_met = len(transformed_data) > 3 and any(x > 20 for x in transformed_data) or False
auxiliary_flag = threshold_met and not (sum(transformed_data) < 50)

# Real logic: pattern analysis using combinatorics
pattern_registry = []
for r in range(2, min(4, len(transformed_data)+1)):
    for combo in itertools.combinations(transformed_data, r):
        if sum(combo) % 7 == 0:  # Selective filtering
            pattern_registry.append(combo)

# Secondary transformation: slice reversal and shift
reversed_tail = transformed_data[::-1][:len(transformed_data)//2]
shifted_cycle = [reversed_tail[-i % len(reversed_tail)] for i in range(len(reversed_tail))]

# Final diagnostic computation (this is the key statement)
def analyze_pattern(seq):
    base_score = sum(seq) * len(seq)
    penalty = 0
    
    # Nested conditional logic with distractors
    for i in range(len(seq)):
        if i % 2 == 0 and seq[i] % 2 == 1:
            penalty += 3
        elif i % 3 == 0:
            penalty -= 1  # Overcompensation trap
        
        # Dead branch: never executed due to logic
        if i > len(seq) * 2:  
            penalty += 100  # Unreachable
    
    # Critical adjustment using slicing
    recent_slice = seq[-3:] if len(seq) >= 3 else seq
    adjustment = sum(recent_slice) // (len(recent_slice) or 1)
    
    return base_score - penalty + adjustment

final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")