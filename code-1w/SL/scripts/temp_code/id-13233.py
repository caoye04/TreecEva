import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_signals = [127, 255, 83, 196, 42, 211, 77, 144, 95, 230]
    offset = 42
    adjusted = [val - offset for val in raw_signals]
    return adjusted

# Irrelevant helper - dead code path (red herring)
def legacy_calibrate(x):
    return (x * 1.05) + 3.7 if x > 100 else (x * 0.98) - 1.2

# Signal normalization using sliding window (relevant)
def normalize_signal(data):
    window_size = 3
    normalized = []
    for i in range(len(data)):
        start = max(0, i - window_size // 2)
        end = min(len(data), i + window_size // 2 + 1)
        window = data[start:end]
        avg = sum(window) / len(window)
        normalized.append(round(avg))
    return normalized

# Bit manipulation for noise detection (partially relevant)
def detect_noise_patterns(seq):
    noise_flags = []
    for val in seq:
        # Count set bits in lower nibble
        nibble_ones = bin(val & 0xF).count('1')
        is_noisy = nibble_ones % 2 == 1
        noise_flags.append(is_noisy)
    return noise_flags

# Decoy function: looks important but unused in final flow
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Real-time filter simulation (distractor with side computation)
def apply_temporal_filter(signal):
    filtered = [signal[0]]
    coefficients = [0.3, 0.4, 0.3]
    for i in range(1, len(signal)-1):
        conv = signal[i-1]*coefficients[0] + signal[i]*coefficients[1] + signal[i+1]*coefficients[2]
        filtered.append(int(conv))
    filtered.append(signal[-1])
    # Derived metric not used later
    peak_to_peak = max(filtered) - min(filtered)
    return filtered

# Core analysis logic (used)
def build_threshold_map(normalized_vals):
    base_thresholds = {}
    for idx, val in enumerate(normalized_vals):
        category = 'high' if val > 100 else 'low'
        penalty = 5 if idx % 3 == 0 else 0
        safe_margin = 10 + penalty
        base_thresholds[idx] = {
            'base': val,
            'safe': val - safe_margin,
            'category': category
        }
    # Unused slicing distraction
    slice_sample = list(base_thresholds.items())[::2]
    temp_dict = {k: v['base'] for k, v in base_thresholds.items()}
    return base_thresholds

# Main diagnostic engine
def analyze_signal(data, thresholds):
    score = 0
    debug_logs = []
    
    # Step 1: amplitude check
    for i, val in enumerate(data):
        th = thresholds[i]['safe']
        if val > th:
            score += 2
        else:
            score -= 1
    
    # Step 2: trend analysis (slope between points)
    trend_score = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if abs(diff) > 15:
            trend_score += 1
    score += trend_score
    
    # Step 3: checksum validation (bit-level)
    checksum = 0
    for val in data[:5]:
        checksum ^= (val & 0xFF)  # Full byte XOR
    if checksum % 7 == 0:
        score += 5
    
    # Step 4: dictionary-based state tracking
    state_tracker = {}
    for val in data:
        key = val // 25
        state_tracker[key] = state_tracker.get(key, 0) + 1
    mode_bin = max(state_tracker, key=state_tracker.get)
    if mode_bin >= 3:
        score += 3
    
    # Final adjustment based on distractor-influenced logic
    magic_offset = len(data) // 2  # red herring, looks algorithmic
    scaling_factor = 1.0  # could be variable, but fixed here
    final_score = score * scaling_factor + 7
    
    # Critical result assignment
    final_diagnostic = int(round(final_score))
    
    # Dead code - misleading print that never executes in normal flow
    if False:
        backup_result = math.floor(sum(data) / len(data))
        print(f"Fallback: {backup_result}")
    
    return final_diagnostic

# Entry point with irrelevant setup
if __name__ == "__main__":
    readings = collect_sensor_readings()
    processed_data = normalize_signal(readings)
    
    # Apply unused transformations (distraction)
    noise_pattern = detect_noise_patterns(readings)
    filtered_data = apply_temporal_filter(processed_data)  # computed but unused
    entropy_value = compute_entropy(processed_data)  # calculated but irrelevant
    
    # Slice manipulation - looks important
    mid_segment = processed_data[2:7]
    reversed_part = mid_segment[::-1]
    padded = [0] * 2 + reversed_part + [0] * 2
    
    # Build necessary map for analysis
    threshold_map = build_threshold_map(processed_data)
    
    # Execute critical statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")