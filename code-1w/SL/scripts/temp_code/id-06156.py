import math

# Simulated sensor data processing with noise filtering and signal interpretation
def main():
    raw_readings = [12.5, 14.8, 9.6, 15.2, 13.0, 11.7, 16.3, 10.4, 14.1, 13.9]
    thresholds = {'low': 10.0, 'high': 15.0}
    calibration_factor = 0.98
    adjustment_history = []

    # Apply calibration and filter out-of-range values using list comprehension
    calibrated_readings = [(x * calibration_factor) for x in raw_readings]
    
    # Misleading transformation: used to distract (not part of final logic)
    transformed_readings = [math.log(x + 1) for x in calibrated_readings if x > 12.0]
    average_transformed = sum(transformed_readings) / len(transformed_readings) if transformed_readings else 0

    # Actual filtering based on dynamic condition
    filtered_data = [x for x in calibrated_readings if thresholds['low'] < x < thresholds['high']]

    # Auxiliary function to compute moving average (distractor, not used directly)
    def moving_average(data, window=2):
        return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]
    
    ma_values = moving_average(filtered_data)  # Computed but unused

    # Signal processor as lambda with conditional logic
    classify_signal = lambda x: 1 if x > 13.0 else -1

    # Process each valid signal and accumulate weighted contribution
    signal_weights = []
    cumulative_drift = 0.0
    for val in filtered_data:
        weight = classify_signal(val) * math.sin(val % math.pi)
        signal_weights.append(round(weight, 4))
        cumulative_drift += abs(val - sum(thresholds.values()) / 2)  # Tracking but not critical

    # Red herring: recursive countdown (no effect on result)
    def countdown(n):
        return 1 if n <= 0 else n - countdown(n-1)
    distraction_value = countdown(5)

    # Core computation: aggregate signal influence
    def process_signals(data):
        if not data:
            return 0
        base = sum(math.cos(x) for x in data)
        modifier = len([x for x in data if x > 13.0]) - len([x for x in data if x <= 13.0])
        return round(base * (modifier if modifier != 0 else 1), 3)

    final_output = process_signals(filtered_data)
    print(f"Result: {final_output}")
    return final_output

result = main()