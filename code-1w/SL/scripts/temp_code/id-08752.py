import math

# Simulated sensor array data with noise and calibration offsets
def generate_raw_readings():
    base_values = [i * 2.5 for i in range(15)]
    noise = [math.sin(i) * 0.7 for i in range(15)]
    calibrated = [base_values[i] + noise[i] + 0.3 for i in range(len(base_values))]
    return calibrated

# Irrelevant auxiliary function – decoy for signal smoothing
def smooth_signal(data, factor=0.1):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(factor * data[i] + (1 - factor) * smoothed[-1])
    return smoothed  # Never used in actual computation path

# Red herring: Emulates hardware lag but unused
delay_buffer = [0] * 5
def apply_hardware_delay(data):
    return delay_buffer[:-1] + data[:5]  # Dead code path

# Core processing: filter and transform relevant components
def filter_anomalies(readings):
    filtered = []
    threshold = sum(readings) / len(readings) * 1.15
    for val in readings:
        if val < threshold and abs(val) > 1e-6:
            filtered.append(val)
    return filtered

# Transform via logarithmic scaling and phase shift (key step)
def logarithmic_transform(data):
    transformed = []
    for x in data:
        if x > 0:
            transformed.append(math.log(x) * 1.7)
        else:
            transformed.append(0)
    return transformed

# Secondary transformation: harmonic weighting (distractor)
def compute_harmonic_weights(n):
    weights = []
    for i in range(1, n+1):
        weights.append(1/i)
    return weights  # Computed but not used

# Real transformation chain — applies bitwise modulation based on index parity
def modulate_by_index(data):
    result = []
    for i, x in enumerate(data):
        if i % 2 == 0:
            result.append(int(x) ^ 3)  # XOR even indices
        else:
            result.append(int(x) | 5)   # OR odd indices
    return [float(x) for x in result]

# Aggregation with conditional accumulation (key logic)
def accumulate_diagnostics(data):
    total = 0.0
    for i, val in enumerate(data):
        if i % 3 == 0:
            total += val * 1.1
        elif i % 3 == 1:
            total -= val * 0.9
        else:
            total += abs(val) * 0.2
    return total

# Final analysis using tuple unpacking and conditional override (target execution point)
def analyze_readings(data):
    temp_data = [x * 1.05 for x in data]
    
    # Dummy destructuring - looks important but irrelevant
    first_half, second_half = temp_data[:len(temp_data)//2], temp_data[len(temp_data)//2:]
    mid_idx = len(temp_data) // 2
    left_avg = sum(first_half) / len(first_half)
    right_avg = sum(second_half) / len(second_half)
    
    # Unused comparison – misleading diagnostic
    imbalance = abs(left_avg - right_avg) > 2.0
    
    # Actual computation happens here: list comprehension with zip
    paired = [(a, b) for a, b in zip(temp_data, reversed(temp_data))]
    products = [p[0] * p[1] for p in paired]
    reduced = sum([math.sqrt(p) if p > 0 else 0 for p in products])
    
    # Final calculation using enumerated weighted sum
    adjustment = 0
    for idx, val in enumerate(products):
        if idx % 4 == 0:
            adjustment += math.floor(val / 10) * 0.5
    final_score = reduced + adjustment
    
    # Critical assignment: this is the true answer
    final_diagnostic = int(final_score * 2) / 2.0  # Round to nearest 0.5
    
    # Decoy printout – distracts from real result
    # print(f'Diagnostic trace: {final_score=}, {adjustment=}, {imbalance=}')
    
    return final_diagnostic

# Entry point
if __name__ == '__main__':
    raw_data = generate_raw_readings()
    cleaned = filter_anomalies(raw_data)
    transformed = logarithmic_transform(cleaned)
    modulated = modulate_by_index(transformed)
    processed_data = [x * 1.1 for x in modulated]  # Minor scaling before final analysis
    
    # Irrelevant combinatorics – creates distraction
    n = len(processed_data)
    combinations_ignored = [i * j for i in range(n) for j in range(i+1, n)]  # Heavy but unused
    
    # UNUSED weight computation – red herring
    harmonic_weights = compute_harmonic_weights(len(processed_data))
    
    # Key statement: where the target variable is computed
    final_diagnostic = analyze_readings(processed_data)
    
    # Print only the required result
    print(f"Result: {final_diagnostic}")