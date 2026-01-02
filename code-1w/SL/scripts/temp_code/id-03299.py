from collections import defaultdict

# Simulate sensor data aggregation and signal correction in a communication system
def aggregate_readings(sensor_data):
    aggregated = defaultdict(int)
    temp_sum = 0
    
    for sensor_id, readings in sensor_data.items():
        valid_readings = [r for r in readings if 0 <= r <= 100]
        if valid_readings:
            avg = sum(valid_readings) / len(valid_readings)
            aggregated[sensor_id] = round(avg)
            temp_sum += avg  # distractor: used only for side computation
    
    # Distractor computation: entropy-like measure (not used in final result)
    total_sensors = len(aggregated)
    entropy_approx = 0
    if total_sensors > 1:
        for val in aggregated.values():
            prob = val / (sum(aggregated.values()) + 1e-5)
            entropy_approx -= prob * __import__('math').log(prob + 1e-5)
    
    return aggregated

def apply_filter(raw_map):
    filtered = {}
    offset = 17  # arbitrary base
    for key, value in raw_map.items():
        transformed = (value ^ 213) % 97  # bitwise XOR and modular arithmetic
        filtered[key] = transformed + offset
    
    # Dead code path (never executed under current logic)
    if False:
        backup = list(filtered.values())
        backup.sort(reverse=True)
    
    return filtered

def process_transmission(seq, factor):
    accumulator = 0
    history = []
    
    for i, val in enumerate(seq):
        adjusted = val * factor
        if i % 2 == 0:
            adjusted = (adjusted + 10) // 2
        else:
            adjusted = adjusted * 2
        
        # Additional irrelevant transformation
        normalized = adjusted / max(1, sum(seq)) * 100
        history.append(normalized)
        
        accumulator += int(adjusted)  # only this matters
    
    # Extra unused computation to increase cognitive load
    trend_score = sum(1 for i in range(1, len(history)) if history[i] > history[i-1])
    stability_index = len(history) / (trend_score + 1)
    
    return accumulator % 10000

# Main execution
sensor_input = {
    'A': [85, 90, 88, 105],
    'B': [70, -5, 72, 74],
    'C': [95, 93, 97, 92],
    'D': [60, 65, 63, 61]
}

aggregated_signal = aggregate_readings(sensor_input)
corrected_map = apply_filter(aggregated_signal)
signal_sequence = list(corrected_map.values())
correction_factor = len(signal_sequence)  # equals 4

final_signal = process_transmission(signal_sequence, correction_factor)
print(f"Result: {final_signal}")