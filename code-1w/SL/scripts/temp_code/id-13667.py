import math

# Simulated sensor data with noise and redundant measurements
temperature_readings = [23.5, 24.1, 25.0, 22.8, 26.3, 27.1, 25.7, 24.9]
pressure_readings = [1013, 1015, 1010, 1020, 1008, 1018, 1012, 1016]
humidity_readings = [45, 47, 50, 44, 52, 55, 49, 48]

# Irrelevant auxiliary data (distractor)
auxiliary_codes = [0xA1, 0xB2, 0xC3, 0xD4, 0xE5, 0xF6, 0x1A, 0x2B]
lookup_map = {i: val for i, val in enumerate([x ^ 0xFF for x in auxiliary_codes])}

# Misleading transformation chain (dead path)
def legacy_process(data):
    return [round(d * 1.02) for d in data if d > 0]

temperatures_legacy = legacy_process([int(t) for t in temperature_readings])  # Unused

# Core processing functions
def clean_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        window = signal[max(0, i-1):min(len(signal), i+2)]
        smoothed.append(sum(window) / len(window))
    return smoothed

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [(v / total) for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

# Data fusion logic with distractors
def fuse_sensors(temp, press, humid):
    normalized_temp = [t / 30.0 for t in temp]
    normalized_press = [p / 1100.0 for p in press]
    normalized_humid = [h / 100.0 for h in humid]
    
    fused = []
    for i in range(len(normalized_temp)):
        # Complex but partially irrelevant weighting
        weight_t = 0.4 + 0.1 * math.sin(i)
        weight_p = 0.3 + 0.1 * math.cos(i)
        weight_h = 0.3 + 0.05 * math.tan(i % 2) if i % 2 != 0 else 0.25
        fused.append(
            weight_t * normalized_temp[i] + 
            weight_p * normalized_press[i] + 
            weight_h * normalized_humid[i]
        )
    return fused

# Decoy function (never called in main logic)
def deprecated_analysis(arr):
    magic_factor = 0.87
    result = 0
    for x in arr:
        if x < 0.5:
            result += magic_factor * x ** 2
        else:
            result += magic_factor * math.sqrt(x)
    return result

# Real processing begins here
filtered_temps = clean_signal(temperature_readings)
fused_data = fuse_sensors(filtered_temps, pressure_readings, humidity_readings)

# Bit manipulation red herring
bit_flags = 0
for i, val in enumerate(fused_data):
    if val > 0.8:
        bit_flags |= (1 << i)
    elif val < 0.4:
        bit_flags ^= (0x0F << (i % 4))

# Transform step with lambda (required feature)
transform_strategy = lambda x: round(x * 1000) % 7  # Maps to small integers
transformed_data = [transform_strategy(x) for x in fused_data]

# Recursive pattern analyzer (core concept)
def analyze_pattern(seq, idx=0, acc=None):
    if acc is None:
        acc = {'count': 0, 'sum': 0, 'path': []}
    
    # Base case
    if idx >= len(seq):
        if acc['count'] == 0:
            return 0.0
        mean_cycle = acc['sum'] / acc['count']
        cycle_entropy = compute_entropy([abs(x - mean_cycle) + 1 for x in acc['path']])
        return round(mean_cycle * cycle_entropy, 4)
    
    current = seq[idx]
    # Conditional branching with filtering
    if current in {1, 3, 5}:
        acc['count'] += 1
        acc['sum'] += current
        acc['path'].append(current)
    elif current == 0:
        acc['sum'] -= 1  # Small adjustment
    else:
        # Even numbers or 6 - ignored but tracked in decoy way
        pass
    
    # Recurse
    return analyze_pattern(seq, idx + 1, acc)

# Secondary recursive helper (distractor - unused)
def trace_sequence(seq, func=lambda x: x):
    if not seq:
        return []
    return [func(seq[0])] + trace_sequence(seq[1:], func)

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)

# Print result as required
print(f"Result: {final_diagnostic}")