import math

# System telemetry simulation (irrelevant data generation)
telemetry_logs = [
    'ERR:VOLTAGE_SPIKE', 'OK:SENSOR_3', 'WARN:FAN_RPM',
    'OK:DISK_IO', 'ERR:VOLTAGE_SPIKE', 'OK:NETWORK'
]
error_count = sum(1 for log in telemetry_logs if 'ERR' in log)
redundant_checksum = sum(len(log) for log in telemetry_logs) % 7

# Primary signal processing chain
raw_signal = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0, 0.8, 0.6, 0.4, 0.2]
filtered_signal = [x for x in raw_signal if x > 0.25]  # Remove noise floor

# Decoy transformation - looks important but unused later
decoy_spectrum = []
for x in filtered_signal:
    val = 0
    for i in range(3):
        val += math.sin(x * i) * (0.5 ** i)
    decoy_spectrum.append(round(val, 3))

# Real entropy computation path
entropy_sequence = []
for i in range(len(filtered_signal)):
    weight = filtered_signal[i]
    if i % 2 == 0:
        contribution = -weight * math.log(weight)
    else:
        contribution = weight * math.exp(-weight)
    entropy_sequence.append(round(contribution, 4))

# Auxiliary diagnostic (distractor)
baseline_health = 0
for i, v in enumerate(entropy_sequence):
    if v > 0.5:
        baseline_health += (v * 10) // (i + 1)

# Bit manipulation red herring (unused)
temp_bits = 0
for val in entropy_sequence[::2]:
    shifted = int(val * 100) << 2
    temp_bits ^= shifted

# Core analysis function with nested logic
def analyze_pattern(seq):
    n = len(seq)
    if n == 0:
        return 0.0
    
    # Set-based uniqueness check (partially relevant)
    unique_vals = set(round(x, 3) for x in seq)
    diversity_score = len(unique_vals)
    
    # Tuple unpacking distraction
    extremes = (min(seq), max(seq))
    low, high = extremes
    
    # Conditional weighting with misleading branches
    total = 0.0
    adjustment = 0
    for i, val in enumerate(seq):
        if i < n // 3:
            factor = 0.8
        elif i < 2 * n // 3:
            factor = 1.1
        else:
            factor = 0.9
            # Dead code path - never executed due to logic
            if val < 0:
                adjustment += 1  # unreachable
        
        # Actual contribution
        total += val * factor
    
    # Final composition with irrelevant components
    size_factor = math.sqrt(n)
    diversity_factor = diversity_score / (n or 1)
    
    # Key calculation - only this part matters
    result = (total * size_factor) + (diversity_factor * 10)
    
    # Distractor: string processing that seems related
    status_tag = f"DIAG_{int(result)}"
    char_sum = sum(ord(c) for c in status_tag if c.isdigit())
    
    return round(result, 4)

# Secondary decoy pipeline - processes same data differently
def ghost_analysis(data):
    transformed = [math.cos(x) ** 2 for x in data]
    return sum(transformed) / len(transformed)

# Unused but plausible-looking initialization
cached_intermediates = {}
for idx in range(3):
    cached_intermediates[f'frame_{idx}'] = ghost_analysis(raw_signal[idx*3:idx*3+3])

# Critical execution point
final_diagnostic = analyze_pattern(entropy_sequence)

# Print target result
print(f"Target result: {final_diagnostic}")