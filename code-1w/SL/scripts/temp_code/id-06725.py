def analyze_pattern(seq, mode='basic'):
    if mode == 'basic':
        return sum(seq) % 7
    elif mode == 'advanced':
        return (sum(x ** 2 for x in seq) % 11)

# Irrelevant helper function (decoy)
def validate_checksum(data):
    temp = 0
    for i in range(len(data)):
        temp ^= data[i] * (i + 1)
    return temp % 13

# Unused signal processing stub (dead code path)
def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Misleading intermediate calculation with red herring variables
raw_readings = [12, 8, 19, 3, 7, 4]
offset_adjustment = 5
adjusted_readings = [x - offset_adjustment for x in raw_readings]

# Distractor: complex-looking but unused transformation chain
encoded_stream = ''.join([chr((val % 26) + 97) for val in raw_readings])
debug_flag = len(encoded_stream) > 10
reversed_hex = [hex(x)[2:][::-1] for x in raw_readings if x % 2 == 0]

# Actual relevant data
health_signature = [3, 5, 7, 2, 8]
baseline_shift = analyze_pattern(health_signature, mode='basic')

# Multiple conditional branches with one being critical
if baseline_shift > 4:
    threshold_levels = (14, 28, 42)
elif baseline_shift == 4:
    threshold_levels = (10, 20, 30)
else:
    threshold_levels = (11, 22, 33)  # This branch is taken

# Tuple unpacking and conditional expression mix
primary, secondary, tertiary = threshold_levels
growth_factor = 1.5 if primary < 12 else 2.0

# Linear search disguised as validation (partially relevant)
def find_anomaly(values, limit):
    for idx, val in enumerate(values):
        if val > limit:
            return idx
    return -1

# Key computation path interwoven with noise
scaling_constant = primary * growth_factor
interim_score = scaling_constant + sum(health_signature[:3])

# String method used in non-obvious but ultimately irrelevant way
status_tag = f"HEALTH_{primary}_LEVEL"
status_flag = status_tag.lower().replace('_', '').isalpha()  # Always True

# Core logic embedded within distractions
def process_metrics(signal, thresholds):
    a, b, c = thresholds
    base = sum(signal) * (a // 3)
    bonus = 0
    
    # Conditional logic determining bonus
    if find_anomaly(signal, 6) != -1 and len(signal) % 2 == 1:
        bonus = b % 5
    
    penalty = 0
    if signal[0] < 5:
        penalty = c // 11
    
    # Final formula combining arithmetic and logical flow
    return int(base + bonus - penalty)

# Critical execution point
final_diagnostic = process_metrics(health_signature, threshold_levels)

print(f"Result: {final_diagnostic}")