from itertools import cycle, islice

# Simulate a production line with varying output rates and maintenance cycles
def analyze_production_efficiency(base_rate, anomalies, duration_hours):
    base_cycle = [1.0, 1.05, 0.95, 1.1, 0.9]  # Hourly variation pattern
    hourly_multiplier = cycle(base_cycle)
    
    total_output = 0.0
    downtime_accumulated = 0.0
    peak_hour_contribution = 0.0
    fluctuation_tracker = []
    simulated_hours = []

    # Misleading counters (distractors)
    false_alarm_count = 0
    recalibration_events = 0
    buffer_reserve = 1250.0

    for hour in range(1, duration_hours + 1):
        current_multiplier = next(hourly_multiplier)
        raw_output = base_rate * current_multiplier
        
        # Simulate anomaly impact
        if hour in anomalies:
            raw_output *= 0.6  # 40% loss during anomaly
            false_alarm_count += 1  # Not actually used

        # Track peak contribution (semi-relevant)
        if current_multiplier == max(base_cycle):
            peak_hour_contribution += raw_output

        # Normal operation
        total_output += raw_output
        fluctuation_tracker.append(current_multiplier)
        simulated_hours.append(raw_output)

        # Fake recalibration logic (dead code path)
        if hour % 100 == 0:
            recalibration_events += 1  # Never used

    # Auxiliary calculation (distractor)
    avg_fluctuation = sum(fluctuation_tracker) / len(fluctuation_tracker)
    total_buffer_needed = buffer_reserve * (duration_hours / 24)

    # Core timing parameters
    ideal_cycle_time = duration_hours * 0.85
    adjusted_downtime = downtime_accumulated * 1.2
    cycle_time = ideal_cycle_time - adjusted_downtime

    # Key computation: efficiency score
    efficiency_score = total_output / (cycle_time * 0.95)
    
    # Red herring final adjustment (not assigned back)
    efficiency_score * 1.02  # No effect

    return efficiency_score

# Execute simulation
result = analyze_production_efficiency(base_rate=87, anomalies=[12, 23, 45], duration_hours=72)
efficiency_score = result
print(f"Result: {efficiency_score}")