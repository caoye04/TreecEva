from collections import defaultdict, Counter

# Simulated bio-signal processing system with decoy diagnostics

def analyze_rhythm(pattern):
    if len(pattern) < 3:
        return False
    rhythm_score = 0
    for i in range(1, len(pattern)):
        if pattern[i] > pattern[i-1]:
            rhythm_score += 2
        elif pattern[i] == pattern[i-1]:
            rhythm_score -= 1
    return rhythm_score > 3

# Irrelevant helper - dead code path
def deprecated_calibrate(x):
    return (x * 0.97) + 3.14

# Unused transformation function (distractor)
def transform_sequence(seq):
    return [x ** 0.5 for x in seq if x > 0]

# Core diagnostic engine
system_load = [87, 92, 65, 74, 88, 90, 71]
baseline_readings = {"alpha": 45, "beta": 67, "gamma": 53}

# Misleading intermediate computation (looks important but unused)
avg_reading = sum(baseline_readings.values()) / len(baseline_readings)
adjusted_load = list(map(lambda x: x * 1.05, system_load))

# Primary health signature (tuple unpacking and slicing)
raw_signature = [3.2, 1.8, 4.5, 2.1, 5.0, 3.7, 2.4, 4.1, 3.9, 2.8]
trimmed = raw_signature[1:8:2]  # slicing operation
offset_val = 0.3
shifted = [round(x - offset_val, 2) for x in trimmed]

detrended = [abs(shifted[i] - shifted[i+1]) for i in range(len(shifted)-1)]

event_flag = any(x >= 1.5 for x in detrended)
signal_stable = all(x < 2.0 for x in shifted)

# Decoy dictionary aggregation (irrelevant)
stats_summary = defaultdict(int)
for val in system_load:
    if val > 85:
        stats_summary['high'] += 1
    elif val > 70:
        stats_summary['medium'] += 1
    else:
        stats_summary['low'] += 1

# Health signature constructed via conditional expression and slicing
health_signature = [
    raw_signature[i] * (1.1 if i % 2 == 0 else 0.9)
    for i in range(0, len(raw_signature), 2)
]

# Dictionary used for mapping (real usage)
severity_map = {'critical': 5, 'high': 4, 'moderate': 3, 'low': 2, 'normal': 1}

# Bit manipulation decoy (misleading - looks like signal encoding)
encoded_diagnostic = 0
for val in system_load[:4]:
    encoded_diagnostic ^= int(val)
    encoded_diagnostic <<= 1
    if encoded_diagnostic > 255:
        encoded_diagnostic = encoded_diagnostic % 256

# Actual key processing function
# Combines boolean logic, arithmetic, collections, and conditionals
def process_metrics(signature, load):
    c = Counter()
    for x in signature:
        if x > 3.0:
            c['elevated'] += 1
        else:
            c['stable'] += 1
    
    # Conditional expression determining processing path
    base_score = sum(signature) if c['elevated'] >= 2 else sum(signature) * 0.85
    
    # Real computational chain (nested logic)
    adjustment_factor = 0.0
    if base_score > 10.0:
        if len(load) % 2 == 0:
            adjustment_factor = 1.2
        else:
            if sum(load) / len(load) > 80:
                adjustment_factor = 1.35
            else:
                adjustment_factor = 1.1
    else:
        adjustment_factor = 0.9
    
    # Multiple arithmetic operations and data structure use
    temp_array = [x for x in load if x > 75]
    outlier_count = len([x for x in temp_array if x > 85])
    
    # Final calculation with interaction between multiple concepts
    penalty = 0
    if event_flag and not signal_stable:  # uses outer-scope variables (closure-like)
        penalty += 5
    if analyze_rhythm(system_load):  # calls function with real impact
        penalty -= 2
    
    # Key result computation
    intermediate = base_score * adjustment_factor
    final_value = int(intermediate) - penalty + severity_map['moderate']
    
    # Dead code branch (never reached - red herring)
    if final_value < 0:
        final_value = abs(final_value) ^ 2
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(health_signature, system_load)

# Output required format
print(f"Target result: {final_diagnostic}")