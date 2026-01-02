from itertools import compress, cycle
import math

# Simulate sensor data stream with periodic noise
def generate_flow_data(baseline, duration, noise_factor):
    time_cycles = list(range(duration))
    noise_wave = [math.sin(t / 3) * noise_factor for t in time_cycles]
    base_flow = [baseline + (t % 7) for t in time_cycles]
    return [b + n for b, n in zip(base_flow, noise_wave)]

# Misleading auxiliary function (not used in final calculation)
def predict_failure_risk(data_stream):
    risk_score = 0
    for val in data_stream[:10]:
        if val > 30:
            risk_score += 1.5
        elif val < 10:
            risk_score -= 0.8
    return abs(risk_score)

# Real processing pipeline
flow_data = generate_flow_data(baseline=18, duration=24, noise_factor=6.5)

# Distractor: complex but unused filter mask
dynamic_mask = [(x > 20) and (i % 3 != 0) for i, x in enumerate(flow_data)]
masked_entries = list(compress(flow_data, dynamic_mask))

# Secondary distractor: cycling weights with no impact
weight_cycle = cycle([0.8, 1.2, 0.9])
weighted_buffer = [val * next(weight_cycle) for val, _ in zip(flow_data, range(len(flow_data)))]

# Threshold logic using lambda (required feature)
threshhold_func = lambda x: x > 19.3

# Conditional expression and modular arithmetic in filtering
relevant_peaks = [
    val for idx, val in enumerate(flow_data)
    if threshhold_func(val) and (idx % 5 == idx % 3)  # rare condition: mod conflict → only idx where mod 5 equals mod 3
]

# Helper function using lambda and conditional expression
def calculate_equilibrium(data, threshold_strategy):
    above_threshold = list(filter(threshold_strategy, data))
    below_or_equal = [x for x in data if not threshold_strategy(x)]
    
    # Complex but relevant aggregation
    high_avg = sum(above_threshold) / len(above_threshold) if above_threshold else 0
    low_avg = sum(below_or_equal) / len(below_or_equal) if below_or_equal else 0
    
    # Interdependent computation with nesting
    adjustment_factor = 0.5 if len(above_threshold) > len(below_or_equal) else 1.5
    
    # Core logic: equilibrium defined as weighted difference
    temp_result = high_avg - low_avg
    final_shift = temp_result * adjustment_factor
    
    # Introduce dead computation (distractor)
    _ = [math.log(1 + abs(final_shift / (i+1))) for i in range(3)]  # unused list
    
    return int(abs(final_shift))  # deterministic integer output

# Key statement
equilibrium_score = calculate_equilibrium(flow_data, threshhold_func)

# Print result as required
print(f"Target result: {equilibrium_score}")