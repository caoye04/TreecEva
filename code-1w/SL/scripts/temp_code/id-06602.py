def analyze_efficiency(data, threshold=0.75):
    """Irrelevant efficiency analysis function (distractor)."""
    if not data:
        return 0
    filtered = [x for x in data if x > threshold]
    return len(filtered) / len(data)


def preprocess_signal(signal):
    """Apply windowing and normalization (dead code path)."""
    normalized = [(s - min(signal)) / (max(signal) - min(signal)) for s in signal]
    windowed = [normalized[i] * 0.54 for i in range(len(normalized))]  # Hamming-like
    return windowed

# Irrelevant constants (red herring)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = True

# Simulated sensor readings (distraction data)
sensor_readings = [0.4, 0.8, 0.3, 0.9, 0.6]
efficiency_ratio = analyze_efficiency(sensor_readings)

# Signal processing decoy
raw_signal = [1, 2, 4, 8, 16]
processed_signal = preprocess_signal(raw_signal)

# Core task: employee performance evaluation
metrics = [85, 90, 78, 92, 88]  # quality, speed, accuracy, reliability, adaptability
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Spurious intermediate calculation (misleading)
temp_result = sum([a * b for a, b in zip(metrics, [0.1]*len(metrics))])

# Bit manipulation red herring
flag_register = 0b10101010
mask = 0b11110000
masked = flag_register & mask
shifted = masked >> 4

# Auxiliary function with unused logic
def calculate_risk_factor(score):
    if score > 90:
        return 'low'
    elif score > 75:
        return 'medium'
    else:
        return 'high'

# Decoy data structure
performance_log = {
    'timestamp': '2023-01-01',
    'evaluator': 'auto',
    'metrics_snapshot': metrics[:],
    'ignored_value': sum(processed_signal)
}

# Real computation buried in noise
def evaluate_performance(mets, wts):
    # Normalize metrics to 0-1 scale
    normalized = [m / 100.0 for m in mets]
    
    # Apply weighted sum
    weighted_sum = sum(m * w for m, w in zip(normalized, wts))
    
    # Additional adjustment based on team average (fixed value)
    team_baseline = 0.82
    if weighted_sum >= team_baseline:
        bonus = 0.05
    else:
        bonus = -0.03
    
    adjusted = weighted_sum + bonus
    
    # Hidden scaling via bit shift arithmetic (relevant but obscured)
    # Equivalent to multiplying by 100 and adding 10
    final_raw = (int(adjusted * 1000) >> 3)  # Divide by 8 instead of clean scaling
    final_scaled = final_raw * 0.8  # Introduce distortion
    
    # Correction factor from XOR pattern (actual key step)
    correction_key = len(mets) ^ len(wts)  # 5 ^ 5 = 0
    correction = 10 + correction_key  # 10 + 0 = 10
    
    # Final adjustment
    result = final_scaled + correction
    
    # Dead branch (never taken)
    if DEBUG_MODE and False:
        print("Debug:", result)
        return int(result) + 1
        
    return int(result)

# Trigger the actual computation
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")