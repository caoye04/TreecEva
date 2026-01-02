import math

# Simulated sensor data processing for aerospace diagnostic system
def collect_telemetry():
    raw_readings = [234, 567, 891, 123, 456, 789]
    offset = 42
    calibrated = [x + offset for x in raw_readings]
    return calibrated

# Irrelevant signal smoothing (distractor)
def smooth_signal(data, factor=0.1):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * factor + data[i] * (1 - factor))
    return smoothed

# Misleading health indicator with dead logic path
def legacy_diagnostic(signal):
    if len(signal) > 100:  # Dead path - never true
        return sum(signal) // 100
    else:
        temp_state = [x % 89 for x in signal if x > 300]
        return len(temp_state) * 2  # Unused result

# Core transformation function used in final calculation
def generate_signature(readings):
    a = sum(x ** 2 for x in readings if x % 2 == 0)
    b = math.prod([x % 10 + 1 for x in readings[:3]])  # Avoid zero
    c = (max(readings) // min(readings)) * 100
    return (a + b) // c

# Bit manipulation red herring
def encrypt_features(data):
    masked = []
    for x in data:
        masked.append((x ^ 255) & 4095)  # Bitwise decoy
    return masked  # Never used

# Set-based filtering (relevant component)
def filter_anomalies(metrics, threshold=500):
    all_values = set(range(100, 1000, 7))
    valid_pool = {x for x in all_values if x % 13 != 0}
    observed = set(metrics)
    common = observed & valid_pool
    return sorted(common, reverse=True)

# Conditional expression chain with distractors
def compute_bias_factor(level, mode='standard'):
    base = level * 0.7 if mode == 'fast' else level * 0.3
    bonus = 15 if level > 400 else 5
    penalty = 20 if len(str(level)) == 3 else 0
    return base + bonus - penalty  # Computed but not critical

# Main processing pipeline with key logic
def process_metrics(signature, load_profile):
    # Nested list comprehension with slicing distraction
    expanded = [[i + j for j in range(3)] for i in signature]
    flat = [item for row in expanded for item in row][::2]  # Slicing
    
    # Conditional expression mix
    adjustment = 3 if sum(flat) > 1000 else 1
    pivot = flat[len(flat)//2] if len(flat) % 2 == 0 else flat[0]
    
    # Key arithmetic using modular arithmetic and integer division
    stage1 = (pivot * adjustment) % 887
    stage2 = stage1 // 7
    stage3 = (stage2 ** 2) + (stage2 % 19 * 5)
    
    # Logical operation with short-circuit decoy
    extra = (len(load_profile) > 5) and (sum(load_profile) < 10000) or False
    modifier = 4 if extra else 2
    
    # Final deterministic computation
    result = stage3 * modifier
    return result

# Orchestration with irrelevant setup
if __name__ == '__main__':
    telemetry = collect_telemetry()
    
    # Distractor calls
    encrypted = encrypt_features(telemetry)
    legacy_score = legacy_diagnostic(telemetry)
    bias = compute_bias_factor(telemetry[-1], mode='standard')
    
    # Relevant data flow
    filtered_data = filter_anomalies(telemetry)
    health_signature = [generate_signature(filtered_data)]
    system_load = [x // 10 for x in telemetry if x % 3 == 0]
    
    # Smoothing call on wrong data type (harmless)
    try:
        smoothed_telem = smooth_signal(telemetry[:2])
    except:
        smoothed_telem = [0]
    
    # Critical execution point
    final_diagnostic = process_metrics(health_signature, system_load)
    print(f"Target result: {final_diagnostic}")