import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_signals = [0.78, 1.32, 0.51, 2.44, 1.99, 0.01, 0.33, 1.11]
    baseline = 1.0
    adjusted = [math.sin(x - baseline) for x in raw_signals]
    return adjusted

# Irrelevant auxiliary function - dead code path
def deprecated_filter(data):
    result = []
    for x in data:
        if x > 0.5:
            result.append(x * 0.9)
    return result

# Signal transformation with slicing and noise injection (some irrelevant)
def transform_signal(signal):
    shifted = [x * 1.1 for x in signal]
    extended = shifted + shifted[:3]  # Append first 3 for continuity
    noise_floor = [0.01, -0.02, 0.015, -0.01, 0.005]
    corrupted = [extended[i] + noise_floor[i % len(noise_floor)] for i in range(len(extended))]
    cleaned = corrupted[1:-1]  # Slice to remove edge artifacts
    resampled = cleaned[::2]  # Downsample every other point
    return resampled

# Complex pattern analyzer combining multiple logic types
def analyze_pattern(data, threshold):
    n = len(data)
    if n == 0:
        return 0
    
    # Compute moving average of last 3 elements
    avg_recent = sum(data[-3:]) / 3 if n >= 3 else sum(data) / n
    
    # Bit manipulation red herring
    magic_seed = 0b1010
    mask = (magic_seed << 2) ^ 0b1101
    decoy_value = (mask & 0xFF) % 7  # Unused but looks important
    
    # Multiple assignments and tuple unpacking distraction
    (alpha, beta) = (0.618, 1.618)
    gamma, delta = beta - alpha, alpha + 0.382
    
    # Real logic: count how many exceed threshold after phase shift
    shifted_data = [math.cos(x) * gamma for x in data]
    triggered = 0
    for val in shifted_data:
        if abs(val) > threshold:
            triggered += 1
    
    # Secondary condition with short-circuit logic
    bonus = 10 if triggered > 2 and (avg_recent > -0.1 or True and False) else 0
    
    # Final computation involving composite operations
    base_score = sum(shifted_data) * 100
    final_score = int(base_score + bonus)
    
    # Distractor: unused complex structure
    diagnostics_log = {
        'raw_count': len(data),
        'peak': max(data, default=0),
        'entropy': math.log(abs(base_score) + 1),
        'decoy_flag': (mask & 0b1001) == 0b1001
    }
    
    return final_score

# Misleading preprocessing chain
readings = collect_readings()
processed_buffer = [x * 2.0 for x in readings if x > 0]  # Partial filtering
extended_buffer = processed_buffer[:4] + [0.1, 0.2, 0.3]
sorted_view = sorted(extended_buffer)

# Actual relevant data pipeline
primary_stream = collect_readings()           # Re-collect fresh data
target_phase = primary_stream[1:7]             # Extract subset
time_window = target_phase + [target_phase[0]] # Circular wrap
transformed_data = transform_signal(time_window)

# Decoy statistical analysis (never used)
def compute_entropy(arr):
    total = 0.0
    for x in arr:
        if x != 0:
            total += x * math.log(abs(x))
    return round(total, 4)

entropy_diagnostic = compute_entropy(transformed_data)  # Dead end

# Key control parameter
key_threshold = 0.75

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

print(f"Result: {final_diagnostic}")