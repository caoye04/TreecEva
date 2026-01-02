def preprocess_signals(raw_data):
    # Irrelevant preprocessing (dead path)
    cleaned = [x for x in raw_data if x > 0]
    smoothed = [sum(cleaned[i:i+3]) / 3 for i in range(len(cleaned) - 2)]
    return smoothed


def generate_baseline(count):
    # Distractor function: generates unused baseline sequence
    return [i ** 2 + 2 * i + 1 for i in range(count)]


def evaluate_stability(readings):
    # Another decoy function with misleading intermediate logic
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 5.0

# Main diagnostic workflow
def analyze_pattern(logs, limits):
    cumulative_score = 0
    history = []
    
    for entry in logs:
        # Extract time-series values
        values = [v for v in entry['data'] if v % 2 == 1]  # Keep only odd values
        
        # Bit manipulation red herring
        shifted = [(v << 1) ^ 3 for v in values]
        
        # Real logic begins: count occurrences above threshold
        above_limit = sum(1 for v in values if v > limits['upper'])
        below_guard = sum(1 for v in values if v < limits['lower'])
        
        # Update score based on valid conditions
        if above_limit > below_guard:
            cumulative_score += above_limit * 2
        else:
            cumulative_score -= below_guard
        
        history.append(len(values))
    
    # Slicing operation to extract recent history
    recent_history = history[-4:]
    
    # Use of enumerate and zip: real but subtle usage
    trend_adjustment = 0
    for i, (a, b) in enumerate(zip(recent_history, recent_history[1:])):
        if b > a:
            trend_adjustment += i + 1

    # Set operations as meaningful distraction
    unique_counts = set(history)
    expected_counts = set(range(1, max(history)+1))
    missing = expected_counts - unique_counts  # Unused
    
    # Final computation using only part of the data
    base_result = sum(recent_history) + trend_adjustment
    
    # Key transformation
    final_weight = len(logs) ** 2 if len(missing) > 0 else len(logs)
    
    return base_result * final_weight

# Simulated sensor diagnostics
sensor_logs = [
    {'timestamp': 1001, 'data': [3, 7, 8, 12, 15], 'mode': 'active'},
    {'timestamp': 1002, 'data': [2, 5, 6, 9, 11, 14], 'mode': 'active'},
    {'timestamp': 1003, 'data': [4, 5, 10, 13, 16], 'mode': 'idle'},
    {'timestamp': 1004, 'data': [1, 7, 9, 10, 11, 12, 13], 'mode': 'active'},
    {'timestamp': 1005, 'data': [6, 8, 9, 14, 15], 'mode': 'idle'}
]

# Threshold configuration (real input)
thresholds = {'upper': 10, 'lower': 5}

# Unused variables and irrelevant computations (distraction)
data_matrix = [[i*j for j in range(5)] for i in range(5)]
baseline_sequence = generate_baseline(10)

# Signal preprocessing (never used)
processed = preprocess_signals([val for log in sensor_logs for val in log['data']])

# Stability check (unused result)
stability_flag = evaluate_stability(processed)

# Core execution point
final_diagnostic = analyze_pattern(sensor_logs, thresholds)

print(f"Target result: {final_diagnostic}")