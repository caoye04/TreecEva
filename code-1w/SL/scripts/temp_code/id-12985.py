from collections import defaultdict
from itertools import cycle

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_samples):
    processed = []
    noise_floor = 0.041
    calibration_offset = 0.003
    for val in raw_samples:
        corrected = abs(val - calibration_offset)
        if corrected > noise_floor:
            processed.append(int(corrected * 1000))
    return processed

# Irrelevant helper: computes statistical moment (not used in final path)
def compute_moment(data, order=2):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** order for x in data) / len(data)

# Decoy function: appears important but unused
def legacy_normalization(vec):
    max_val = max(vec)
    return [v / max_val for v in vec]

# Core transformation: maps values using modulo dispersion
def generate_pattern(sequence, key_shift):
    result = []
    shift_cycle = cycle([key_shift, -key_shift])
    for i, item in enumerate(sequence):
        shifted = item + next(shift_cycle)
        modded = shifted % 17
        if modded not in [0, 1]:
            result.append(modded)
    return result

# Secondary filter: removes Fibonacci-like artifacts
def filter_anomalies(trace):
    safe_list = [trace[0]] if trace else []
    for i in range(1, len(trace)-1):
        prev, curr, next_val = trace[i-1], trace[i], trace[i+1]
        if not (curr == (prev + next_val) or curr == abs(prev - next_val)):
            safe_list.append(curr)
    if len(trace) > 1:
        safe_list.append(trace[-1])
    return safe_list

# Main analysis engine
def analyze_signal(buffer, config_map):
    base_score = 0
    for k, v in config_map.items():
        if len(k) % 2 == 0:
            base_score += v * 2
        else:
            base_score -= v

    # Apply buffer weighting
    weights = [1, -1, 2]
    weighted_sum = sum(buffer[i % len(buffer)] * weights[i % len(weights)] for i in range(len(buffer)))

    temp_flag = (weighted_sum + base_score) > 50

    # Critical branching logic
    if temp_flag:
        intermediate = (base_score * 3) + (weighted_sum // 4)
        if intermediate < 0:
            return intermediate * -1
        else:
            return intermediate // 2
    else:
        return base_score * weighted_sum

# --- Initialization and Execution ---

def main():
    # Raw sensor input (simulated)
    raw_data = [0.102, 0.038, 0.214, 0.042, 0.156, 0.099, 0.301]

    # Irrelevant statistic
    sample_variance = compute_moment(raw_data, 2)

    # Process signal
    cleaned = preprocess_readings(raw_data)

    # Dead code path: unused normalization
    normalized_cleaned = legacy_normalization(cleaned)  # Unused

    # Generate pattern key
    pattern_key = 7
    dispersed = generate_pattern(cleaned, pattern_key)

    # Filtering stage
    filtered_trace = filter_anomalies(dispersed)

    # Build configuration map using defaultdict
    threshold_map = defaultdict(int)
    categories = ['alpha', 'beta', 'gamma_response', 'delta_peak']
    values = [8, 12, 5, 20]
    for cat, val in zip(categories, values):
        threshold_map[cat] = val

    # Buffer preparation
    pattern_buffer = []
    for x in filtered_trace:
        if x % 3 == 0:
            pattern_buffer.append(x * 2)
        elif x % 5 == 0:
            pattern_buffer.append(x + 1)
        else:
            pattern_buffer.append(x)

    # Introduce red herring variable
    diagnostic_shadow = sum(pattern_buffer) * threshold_map['beta']  # Distractor

    # Key execution point
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

    # Output target result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()