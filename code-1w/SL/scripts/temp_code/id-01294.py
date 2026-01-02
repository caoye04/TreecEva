def analyze_component(x, threshold=5.0):
    return x * 1.5 if x > threshold else x * 0.8

# Simulate sensor readings and system diagnostics
def main():
    raw_readings = [3.4, 6.7, 2.1, 8.9, 4.5]
    adjusted_values = [analyze_component(val) for val in raw_readings]

    # Irrelevant diagnostic stats (distractors)
    avg_reading = sum(raw_readings) / len(raw_readings)
    max_adjusted = max(adjusted_values)
    stability_index = (max_adjusted - avg_reading) / avg_reading

    # System mode flags (some unused)
    is_calibration_mode = False
    is_diagnostics_active = True
    debug_override = False

    # Process benchmark results
    benchmark_results = {
        'latency': 7.2,
        'throughput': 4.8,
        'consistency': 6.1,
        'reliability': 5.5
    }

    # Secondary data structure with redundant info
    auxiliary_metrics = {
        'jitter': 3.3,
        'packet_loss': 0.9,
        'bandwidth_usage': 7.7
    }

    # Mapping components to weights (not all used)
    weight_map = {
        'latency': 0.3,
        'throughput': 0.25,
        'consistency': 0.2,
        'reliability': 0.15,
        'fallback': 0.1
    }

    def calculate_performance(data):
        base = 0.0
        penalty = 0.0

        # Conditional logic with mixed operations
        if data['latency'] < 7.0:
            base += data['latency'] * weight_map['latency']
        else:
            base += data['latency'] * weight_map['latency'] * 0.9

        if data['throughput'] >= 4.5:
            base += data['throughput'] * weight_map['throughput']
            bonus_factor = 1.1 if data['consistency'] > 5.0 else 1.0
            base *= bonus_factor  # Compound effect

        # Nested condition with short-circuit behavior
        if data['reliability'] > 5.0 and (data['consistency'] > 5.5 or data['throughput'] > 5.0):
            adjustment = data['reliability'] * 0.1
        else:
            adjustment = -1.5

        final_base = base + adjustment

        # Distractor computation: unused health metric
        health_score = 100 - (stability_index * 5) if 'stability_index' in locals() else 85
        temp_correction = max_adjusted / 10 if is_calibration_mode else 0

        return final_base + temp_correction

    # Key execution point
    final_score = calculate_performance(benchmark_results)

    # Additional irrelevant state tracking
    status_log = []
    if final_score > 6.0:
        status_log.append('OPTIMAL')
    elif final_score > 4.0:
        status_log.append('STABLE')
    else:
        status_log.append('CRITICAL')

    # Print required result
    print(f"Target result: {final_score}")

if __name__ == "__main__":
    main()