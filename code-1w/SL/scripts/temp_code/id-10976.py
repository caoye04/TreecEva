from collections import defaultdict
import math

# Simulated sensor data preprocessing with red herrings
def fetch_raw_readings():
    return [14, 28, 19, 35, 22, 47, 31, 8, 11, 53]

def apply_calibration(raw, factor=1.05):
    # Distractor: this function is called but its result is not directly used in final answer
    return [round(x * factor, 2) for x in raw]

def transform_signal(readings):
    # Real processing path begins here
    squared = [x**2 for x in readings]
    filtered = [x for x in squared if x > 500]
    shifted = [x >> 2 for x in filtered]  # Bit manipulation distractor with actual use
    return shifted

def generate_checksum(data):
    # Dead-end function: looks important but unused
    return sum(data) % 1000

def build_threshold_map(config_level):
    # Creates a meaningful mapping used later
    base = {'low': 50, 'med': 120, 'high': 300}
    adj = {k: v + config_level * 10 for k, v in base.items()}
    extra = defaultdict(lambda: 0)
    for k, v in adj.items():
        extra[k] = v + 5
    return extra  # This is actually used

def evaluate_stability(indices):
    # Irrelevant recursive distraction
    if len(indices) <= 1:
        return indices[0] if indices else 0
    return evaluate_stability(indices[:-1]) + (indices[-1] % 7)

def analyze_signal(data, thresholds):
    count = 0
    for val in data:
        # Logical chain with mixed comparisons
        if val > thresholds['med'] and (val < thresholds['high'] or val % 2 == 0):
            count += int(math.log(val, 2))  # Uses logarithm and type conversion
    return count + (len(data) ^ 15)  # XOR operation as final touch

def main():
    # Entry point with multiple distractions
    raw_sensor_data = fetch_raw_readings()
    calibrated = apply_calibration(raw_sensor_data, 1.05)  # Computed but not used
    processed_data = transform_signal(raw_sensor_data)  # Key data pipeline
    
    # Distractor variables
    temp_analysis = [x for x in calibrated if x < 30]
    peak_value = max(raw_sensor_data)
    normalized_sum = sum(calibrated) / len(calibrated)
    
    # Unused data structure
    history_log = [{'step': i, 'val': v} for i, v in enumerate(temp_analysis)]
    
    # Real configuration
    config_mode = 6
    threshold_map = build_threshold_map(config_mode)
    
    # Irrelevant stability check
    index_sequence = [1, 3, 6, 10, 15]
    stability_score = evaluate_stability(index_sequence)
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # More red herring computations
    lambda_helper = lambda x, y: (x + y) * 2
    checksum_final = lambda_helper(final_diagnostic, stability_score) % 1000
    
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()