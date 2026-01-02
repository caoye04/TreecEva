import itertools

# Simulated sensor data from multiple sources
def generate_telemetry():
    base_values = [i * 1.5 for i in range(10)]
    offsets = [0.1, -0.2, 0.3, -0.1, 0.0]
    return [[val + offset for val in base_values] for offset in offsets]

# Irrelevant helper - looks useful but unused in critical path
def smooth_signal(data):
    smoothed = []
    for row in data:
        smooth_row = [sum(row[i:i+3]) / 3 if i+2 < len(row) else row[i] for i in range(len(row))]
        smoothed.append(smooth_row)
    return smoothed

# Data conditioning with red herring transformations
def preprocess_telemetry(raw_data):
    # Distractor: transform using multiple methods, only one matters
    transformed = []
    temp_amplified = []
    for idx, series in enumerate(raw_data):
        amplified = [x * (idx + 1) for x in series]  # Looks important, but not used
        inverted = [-x for x in series]             # Dead end
        shifted = [x + 10 for x in series]          # Actually used
        temp_amplified.append(amplified)
        transformed.append(shifted)
    
    # More misdirection: complex zip + enumerate that computes irrelevant stats
    stats_log = {}
    for i, (orig, proc) in enumerate(zip(raw_data, transformed)):
        diffs = [abs(a - b) for a, b in zip(orig, proc)]
        stats_log[f'batch_{i}_drift'] = sum(diffs) / len(diffs)
    
    # Decoy structure
    decoy_matrix = [[i*j for j in range(5)] for i in range(5)]
    
    return transformed  # Only this matters

# Threshold system with misleading configuration
threshold_map = {
    'normal': (0, 15),
    'elevated': (15, 25),
    'critical': (25, float('inf')),
    'deprecated_mode': (-10, 0)  # Unused legacy key
}

# Core analysis logic buried in distractions
def evaluate_risk_level(value, config):
    # Multiple checks, but only one logic chain is correct
    if value < config['normal'][1]:
        return 0
    elif value >= config['elevated'][0] and value < config['elevated'][1]:
        return 1
    elif value >= config['critical'][0]:
        return 2
    else:
        return -1  # unreachable, but looks like an edge case

# Recursive pattern detector - appears complex but has fixed outcome
def detect_pattern(seq, index=0, depth=0):
    if depth >= 3:
        return 42  # Magic number red herring
    if index >= len(seq) - 1:
        return 0
    diff = seq[index+1] - seq[index]
    if abs(diff) > 5:
        return 1 + detect_pattern(seq, index+2, depth+1)
    return detect_pattern(seq, index+1, depth)

# Main signal analyzer - the actual critical function
def analyze_signal(data, thresholds):
    cumulative_score = 0
    risk_tally = [0, 0, 0]
    
    # Real computation interlaced with noise
    for i, series in enumerate(data):
        # Key transformation: only even-indexed series contribute
        if i % 2 == 0:
            # Actual logic: count values in critical range
            for val in series:
                if val >= thresholds['critical'][0]:
                    cumulative_score += int(val // 5)
                    risk_tally[2] += 1
        else:
            # Process odd indices through decoy recursion
            _ = detect_pattern(series)
    
    # Irrelevant aggregation
    all_vals = list(itertools.chain.from_iterable(data))
    avg_val = sum(all_vals) / len(all_vals)
    peak = max(all_vals)
    
    # Side calculation that logs but doesn't affect result
    diagnostic_trace = []
    for val in [avg_val, peak]:
        level = evaluate_risk_level(val, thresholds)
        diagnostic_trace.append(level)
    
    # Critical result built silently
    final_component = cumulative_score * 2
    
    # Last distraction: conditional expression with false urgency
    status_flag = 'CRITICAL' if any(x > 30 for x in all_vals) else 'NORMAL'
    
    # The real answer is built here, quietly
    final_diagnostic = final_component - risk_tally[2] * 3 + 10
    
    return final_diagnostic

# Execution flow with obscured entry point
if __name__ == "__main__":
    raw_telemetry = generate_telemetry()
    processed_data = preprocess_telemetry(raw_telemetry)
    
    # These look important but are just warming up the namespace
    _ = smooth_signal(raw_telemetry)
    _ = {f'init_{i}': pow(2, i) for i in range(5)}
    
    # KEY STATEMENT
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    print(f"Result: {final_diagnostic}")