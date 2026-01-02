import math

# Simulated sensor data from multiple sources
def fetch_sensor_readings():
    raw_signals = [2.1, 3.5, -1.2, 4.8, 0.0, -3.3, 6.7, 2.2]
    noise_floor = 0.5
    filtered = [x for x in raw_signals if abs(x) > noise_floor]
    return filtered

# Legacy function - not used but looks relevant
def deprecated_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Transform data using frequency-domain approximation
def apply_fourier_weighting(signal):
    weighted = []
    for i, val in enumerate(signal):
        phase = math.sin(i * math.pi / 4)
        magnitude = abs(val) ** 0.5
        weighted.append(magnitude * phase)
    return weighted

# Map thresholds based on environmental conditions
def generate_threshold_map(conditions):
    base_map = {"critical": 3.0, "warning": 1.5, "info": 0.5}
    adjustment = sum([c % 2 for c in conditions]) * 0.1
    return {k: v + adjustment for k, v in base_map.items()}

# Misleading auxiliary function that computes unrelated metric
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x != 0:
            total += -x * math.log(abs(x))
    return total if total == total else 0.0  # Handle NaN

# Core analysis logic with distractors
def analyze_signal(data, thresholds):
    # Irrelevant transformation (distractor)
    inverted = [1.0 / (1 + math.exp(-x)) for x in data if x < 5]
    
    # Real processing begins
    squared_values = [x * x for x in data]
    avg_sq = sum(squared_values) / len(squared_values)
    rms = math.sqrt(avg_sq)
    
    # Bit manipulation red herring
    bit_analysis = 0
    for x in data:
        if x > 0:
            truncated = int(x)
            bit_analysis ^= (truncated << 1) | 1
    
    # Conditional aggregation across multiple criteria
    high_severity = list(filter(lambda x: x > thresholds["critical"], data))
    medium_severity = list(filter(lambda x: thresholds["warning"] < x <= thresholds["critical"], data))
    
    # Unused but plausible computation path
    if len(high_severity) > len(medium_severity):
        surge_pattern = list(enumerate(high_severity))
    else:
        surge_pattern = []
    
    # Key decision logic
    if rms > thresholds["warning"]:
        score = len(high_severity) * 100 + len(medium_severity) * 10
    else:
        score = 50
    
    # Decoy string-based analysis
    status_flags = ['A', 'B', 'C']
    flag_summary = ''.join(status_flags) + '_DIAG'
    
    # Final diagnostic depends only on score and bit_analysis (but bit_analysis unused)
    final_diagnostic = score + 13  # Offset for calibration
    return final_diagnostic

# Orchestration with red herrings
if __name__ == "__main__":
    # Fetch and preprocess data
    raw_data = fetch_sensor_readings()
    processed_data = apply_fourier_weighting(raw_data)
    
    # Generate environment-specific thresholds
    env_conditions = [17, 23, 29, 31]
    threshold_map = generate_threshold_map(env_conditions)
    
    # Dead code path - never executed but looks important
    debug_mode = False
    if debug_mode:
        entropy = compute_entropy(processed_data)
        print(f'Debug: Entropy={entropy}')
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f'Result: {final_diagnostic}')