import itertools

# Simulate sensor data with noise and metadata
def generate_sensor_snapshot():
    raw_readings = [18, 22, 15, 30, 12]
    calibration_offset = 3
    adjusted = [x + calibration_offset for x in raw_readings]
    timestamp_tag = "2023-09-15T10:45:00Z"
    return adjusted, timestamp_tag

# Irrelevant helper - looks important but unused in critical path
def compute_entropy(data):
    import math
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Decoy transformation chain
def apply_filter_chain(signal):
    filtered = [x for x in signal if x > 20]
    padded = [0] * 2 + filtered + [0] * 2
    reversed_pad = padded[::-1]
    # This function is called but only part of it matters
    return [x * 1.5 for x in reversed_pad]

# Core logic disguised among distractions
def transform_entry(val, shift):
    if val < 20:
        return (val + shift) ** 2
    else:
        return val - (shift * 2)

# Real processing pipeline
initial_data, time_ref = generate_sensor_snapshot()

# Distractor: complex-looking but unused structure
historical_stats = {
    'peak': max(initial_data),
    'baseline': sum(initial_data[:3]) / 3,
    'variance': sum((x - sum(initial_data)/5)**2 for x in initial_data) / 5
}

# Apply actual relevant transformation
shift_factor = len(initial_data)  # 5
transformed_data = []
for item in initial_data:
    result = transform_entry(item, shift_factor)
    transformed_data.append(result)

# Another red herring: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Short-circuit evaluation distraction
trigger_active = False
emergency_override = (trigger_active or False) and fibonacci(5) > 10

# Conditional expression mix
mode_flag = 'turbo' if sum(transformed_data) > 100 else 'eco'
scaling_factor = 1.2 if mode_flag == 'turbo' else 0.8

# Real computation begins here — obscure due to prior noise
def process_sequence(seq):
    # Use itertools to create paired shifts
    shifted_pairs = list(itertools.pairwise(seq))
    totals = []
    for a, b in shifted_pairs:
        totals.append(abs(a - b))
    
    # Actual answer depends on this sum
    base_sum = sum(totals)
    
    # String method used as light obfuscation
    control_key = "adjustment_needed"
    needs_adjust = control_key.startswith("adjust") and 'needed' in control_key
    
    # Final adjustment
    final_value = base_sum
    if needs_adjust:
        multiplier = len(shifted_pairs)
        final_value = base_sum * multiplier  # 4
    
    return final_value

# Critical execution point
final_output = process_sequence(transformed_data)

# Output result as required
print(f"Target result: {final_output}")