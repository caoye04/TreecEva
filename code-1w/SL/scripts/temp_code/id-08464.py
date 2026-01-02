from collections import defaultdict, Counter

# Simulate sensor data processing with noise filtering and state tracking
def analyze_readings(raw_data):
    filtered_data = []
    noise_count = 0
    temp_buffer = []

    for reading in raw_data:
        if reading < -100 or reading > 100:
            noise_count += 1
            continue
        if reading % 7 == 0:
            temp_buffer.append(reading)
        filtered_data.append(reading * 0.95)

    # Irrelevant aggregation (distractor)
    stats_summary = {
        'valid': len(filtered_data),
        'noisy': noise_count,
        'buffered_multiples_of_7': len(temp_buffer)
    }

    return filtered_data

# Track convergence behavior over iterations
def generate_convergence_trace(max_iter=50):
    trace = []
    value = 1000
    decay_factor = 0.92

    for i in range(max_iter):
        value = value * decay_factor + (i % 3) * 0.5
        trace.append(round(value, 3))
    
    # Dead code path - never used (distractor)
    if len(trace) > 100:
        trace = trace[:100]

    return trace

# Evaluate system performance based on convergence pattern and thresholds
def evaluate_performance(log, limits):
    stable_window = []
    fluctuation_count = 0
    breach_count = 0
    recent_trend = []

    for entry in log:
        # Count threshold breaches
        if entry > limits['upper']:
            breach_count += 1

        # Track stability within tolerance
        if abs(entry - limits['target']) < 5.0:
            stable_window.append(entry)
        else:
            if len(stable_window) > 0:
                fluctuation_count += 1
            stable_window.clear()

        # Capture recent trend (last 5 entries)
        recent_trend.append(entry)
        if len(recent_trend) > 5:
            recent_trend.pop(0)

    # Compute final score using only specific logic
    base_score = len(log) // 5
    penalty = breach_count * 2 + fluctuation_count * 3
    final_score = base_score - penalty

    # Unused diagnostic computation (distractor)
    trend_counter = Counter(recent_trend)
    avg_recent = sum(recent_trend) / len(recent_trend) if recent_trend else 0

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data generation
    sensor_input = list(range(-120, 130, 4)) + [7 * i for i in range(15)]
    processed_readings = analyze_readings(sensor_input)

    # Generate convergence history
    convergence_log = generate_convergence_trace(max_iter=42)

    # Define performance thresholds
    thresholds = {
        'upper': 85.0,
        'lower': 60.0,
        'target': 72.5
    }

    # Key statement
    final_score = evaluate_performance(convergence_log, thresholds)
    
    # Additional irrelevant tracking (distractor)
    state_tracker = defaultdict(int)
    for val in convergence_log:
        state_tracker[round(val // 10)] += 1

    print(f"Result: {final_score}")