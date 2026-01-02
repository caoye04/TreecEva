def analyze_component(x, y):
    if x < 0:
        return (y ** 2) % 5
    else:
        return (x + y) & 3

# Simulate sensor calibration offsets
calibration_map = {"sensor_a": 3, "sensor_b": 7, "sensor_c": 1, "sensor_d": 9}
offset_keys = list(calibration_map.keys())
temp_readings = [calibration_map[k] * 2 for k in offset_keys if 'sensor_' in k]

# Irrelevant transformation chain
transformed = 0
for val in temp_readings:
    transformed += val ^ 5
    if transformed > 20:
        transformed -= 10

# Main data processing pipeline
benchmark_data = {
    'input_sequence': [4, -2, 6, 1],
    'weights': [0.5, 1.0, 1.5, 2.0],
    'flags': [True, False, True, False]
}

# Auxiliary state tracking (mostly unused)
state_log = set()
running_total = 0
adjustment_factor = 0.8

# Distractor: complex-looking but unused computation
aggregate = sum([w * w for w in benchmark_data['weights']]) / len(benchmark_data['weights'])
smoothed = aggregate ** 0.5

# Core logic with moderate nesting and multiple concepts
intermediate_scores = []
for i, val in enumerate(benchmark_data['input_sequence']):
    weight = benchmark_data['weights'][i]
    flag = benchmark_data['flags'][i]
    
    # Conditional expression and logical operation
    base_score = val * weight if flag or (val > 0 and weight >= 1.0) else val + weight
    
    # Bitwise and modular arithmetic mix
    adjusted = analyze_component(int(base_score), i)
    
    # Set operations for tracking (partial use)
    state_log.add(adjusted)
    
    # Only positive adjusted scores contribute
    if adjusted > 0:
        intermediate_scores.append(adjusted * adjustment_factor)

# Secondary filtering using dictionary-like logic
filtered_scores = [s for s in intermediate_scores if s in {1.6, 2.4, 3.2, 0.8, 4.0}]

# Final aggregation with case conversion red herring
mode_flag = 'FAST'.lower()

# Unused string manipulation distraction
log_trace = ''.join([f"[{s:.1f}]" for s in intermediate_scores])
sanitized_trace = log_trace.replace('.', 'p')

# Critical function call
def calculate_performance(data):
    raw = sum(filtered_scores)
    penalty = len(state_log) % 4
    bonus = len(temp_readings) - 4  # Always zero, but not obviously
    return int(raw - penalty + bonus)

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")