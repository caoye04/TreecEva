def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count += 1
    return count > 2

# Irrelevant helper function (decoy)
def validate_checksum(arr):
    checksum = 0
    for x in arr:
        checksum = (checksum + x * 3) % 7
    return checksum == 0

# Another red herring: unused transformation
def transform_grid(matrix):
    return [[cell ** 2 for cell in row] for row in matrix]

# Distractor: complex but unused data structure
config_map = {
    'threshold': 42,
    'flags': [True, False, True],
    'payload': {'mode': 'debug', 'level': 9}
}

# Real logic begins here
def evaluate_stability(reading):
    return reading > 55 and reading < 85

def compute_baseline(readings):
    total = 0
    valid_count = 0
    for val in readings:
        # Early filtering (part of real logic)
        if evaluate_stability(val):
            total += val
            valid_count += 1
    return total / valid_count if valid_count > 0 else 0

def extract_peaks(series):
    peaks = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            peaks.append(series[i])
    return peaks[:3]  # Only top 3 matter

def process_metrics(data, weights):
    # Step 1: Baseline from stable readings
    base = compute_baseline(data['sensor_readings'])
    
    # Step 2: Get peak anomalies
    peaks = extract_peaks(data['sensor_readings'])
    anomaly_penalty = sum(p // 10 for p in peaks) if len(peaks) >= 2 else 0
    
    # Step 3: Conditional adjustment using ternary-like expression
    adjustment = (15 if data['mode'] == 'aggressive' else 5) if 'mode' in data else 0
    
    # Step 4: Weighted contribution (only one weight is actually used)
    signal_weight = weights.get('primary', 1.2)
    noise_weight = weights.get('auxiliary', 0.8)  # Unused distractor
    temporal_weight = weights.get('timing', 0.5)   # Another decoy

    # Step 5: Actual calculation chain
    raw_score = base * signal_weight
    adjusted_score = raw_score - anomaly_penalty + adjustment
    
    # Step 6: Final threshold clamp
    final_score = adjusted_score if adjusted_score <= 100 else 100
    
    # Irrelevant print for confusion
    # print(f'Debug: base={base}, peaks={peaks}, adjustment={adjustment}')
    
    return int(final_score)

# Simulated input data (real signal embedded in noise)
data = {
    'sensor_readings': [45, 58, 62, 70, 77, 82, 76, 68, 60, 52],  # stable zone: 58 to 82
    'mode': 'aggressive',
    'version': '2.1',
    'debug_flag': False
}

weights = {
    'primary': 1.2,
    'auxiliary': 0.4,
    'timing': 0.9
}

# Key execution point
final_score = process_metrics(data, weights)
print(f"Target result: {final_score}")