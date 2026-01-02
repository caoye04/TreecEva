import math

# Simulated sensor array data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 80, 96, 112, 224, 240, 208, 176, 160]
    baseline_offset = 63
    adjusted = [r - baseline_offset for r in raw_readings]
    return adjusted

# Irrelevant helper - dead code path (not used in final execution)
def deprecated_filter(data):
    return [x for x in data if x > 50]

# Data transformation pipeline
def transform_signal(sequence, mode='fast'):
    if mode == 'legacy':
        return [int(s * 1.5) for s in sequence]
    else:
        # Apply bit manipulation: rotate left by 1 and XOR with prime
        rotated = [(s << 1) & 255 | (s >> 7) for s in sequence]
        processed = [r ^ 89 for r in rotated]  # XOR with prime
        return processed[:len(processed)//2 + len(processed)%2]  # slicing: keep first half (ceiling division)

# Secondary transformation for red herring branch
def obscure_transform(seq):
    reversed_seq = seq[::-1]
    mapped = [int(math.sqrt(x * 2)) if x > 0 else 0 for x in reversed_seq]
    return [m + 10 for m in mapped]

# Control flow decoy: looks important but unused
potential_modes = ['fast', 'secure', 'legacy']
current_mode = 'fast'

# Threshold logic for system diagnostics
def build_threshold_map(level='normal'):
    base = {'low': 32, 'mid': 64, 'high': 128}
    if level == 'strict':
        return {k: int(v * 0.75) for k, v in base.items()}
    elif level == 'relaxed':
        return {k: v + 20 for k, v in base.items()}
    else:
        return base  # normal thresholds

# Main analysis function with multiple concepts
def analyze_pattern(data_list, limits):
    count_low = 0
    count_mid = 0
    count_high = 0
    
    # Bit analysis side computation (distractor)
    total_bits = sum(bin(item).count('1') for item in data_list)
    avg_bit_density = total_bits / len(data_list)

    # Real logic: classify based on thresholds
    for val in data_list:
        if val < limits['low']:
            count_low += 1
        elif val < limits['mid']:
            count_mid += 1
        elif val < limits['high']:
            count_high += 1
    
    # Compute weighted diagnostic score
    weights = {'low': 1, 'mid': 2.5, 'high': 4.75}
    score = (count_low * weights['low'] + 
             count_mid * weights['mid'] + 
             count_high * weights['high'])
    
    # Final adjustment using trigonometric weighting (overkill but plausible)
    angle = math.pi * count_low / (len(data_list) + 1)
    correction = math.cos(angle)
    adjusted_score = score * correction
    
    # Dead branch: never executed due to prior conditions
    if len(data_list) > 1000:
        fallback = sum(data_list) / 100
        adjusted_score = fallback
    
    return int(adjusted_score)

# Unused recursive red herring function
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2)

# --- Execution Flow ---
sensor_data = collect_sensor_readings()

# Misleading alternate path (never taken)
temp_debug = False
if temp_debug:
    processed_data = obscure_transform(sensor_data)
else:
    processed_data = transform_signal(sensor_data, mode='fast')

# Build threshold configuration
threshold_config = build_threshold_map('normal')

# Key diagnostic analysis
final_diagnostic = analyze_pattern(processed_data, threshold_config)

# Output result
print(f"Result: {final_diagnostic}")