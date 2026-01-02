from itertools import cycle

# Simulate sensor readings over time
def analyze_system_performance():
    timestamps = list(range(10))
    readings = [85, 90, 92, 88, 95, 91, 87, 89, 94, 93]
    thresholds = [90] * len(timestamps)
    
    # Distractor: irrelevant pattern generator
    pattern_cycle = cycle(['A', 'B', 'C'])
    pattern_log = [next(pattern_cycle) for _ in range(len(timestamps))]
    
    # Tracking valid high-performance intervals
    high_perf_intervals = 0
    current_streak = 0
    total_deviation = 0.0

    for i in range(len(readings)):
        deviation = readings[i] - thresholds[i]
        total_deviation += abs(deviation)

        if readings[i] >= thresholds[i]:
            current_streak += 1
            # Distractor: unused conditional branch
            if deviation > 5:
                pass  # Dead code path
        else:
            if current_streak > 2:
                high_perf_intervals += 1
            current_streak = 0

    # Handle final streak
    if current_streak > 2:
        high_perf_intervals += 1

    # Base system rating derived from statistical analysis
    avg_reading = sum(readings) / len(readings)
    peak_count = sum(1 for r in readings if r > 90)
    base_rating = int(avg_reading // 10) + peak_count

    # Performance multiplier based on interval consistency
    consistency_factor = 1.0
    if high_perf_intervals >= 2:
        consistency_factor = 1.75
    elif high_perf_intervals == 1:
        consistency_factor = 1.25
    else:
        consistency_factor = 0.85

    # System activation logic based on cyclic pattern (simulated)
    activation_key = ''.join(pattern_log).count('A')
    active = (activation_key % 2 == 1) and (peak_count > 3)

    # Key computational step with early distractors
    temp_debug = [x * 0.1 for x in readings if x > 90]  # Irrelevant transformation
    debug_snapshot = {"readings": readings, "temp": temp_debug}  # Unused structure

    performance_multiplier = round(consistency_factor * (1 + total_deviation / 100), 2)

    # Critical statement: target variable assignment
    efficiency_score = base_rating * performance_multiplier if active else 0

    # Final output
    print(f"Result: {efficiency_score}")

analyze_system_performance()