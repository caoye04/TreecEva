import math

def analyze_conditions(temperature, pressure):
    # Irrelevant computation (distractor)
    hypothetical_yield = (temperature * 0.8) + (pressure * 0.3)
    stress_factor = temperature > 50 and pressure > 80
    correction = 1.2 if stress_factor else 0.9
    adjusted_temp = temperature * correction
    return adjusted_temp

# Simulate sensor data
raw_readings = [105, 92, 118, 87, 95]
data_points = []
for val in raw_readings:
    normalized = (val - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) if max(raw_readings) != min(raw_readings) else 0
    data_points.append(round(normalized * 100))

# Misleading intermediate calculations
total_cycles = 0
for i in range(len(data_points)):
    if data_points[i] > 50:
        total_cycles += 1
extra_load = total_cycles * 2.5  # Not used later

# Core logic with conditional expressions and state tracking
baseline = sum(data_points) / len(data_points)
variance = sum((x - baseline) ** 2 for x in data_points) / len(data_points)
std_deviation = math.sqrt(variance)

stability_index = 100 - std_deviation

# Simulate multi-factor adjustment
external_factor = 0.85
internal_calibration = 1.1 if baseline > 60 else 0.95

adjusted_stability = stability_index * external_factor * internal_calibration

# Secondary irrelevant transformation
dummy_weights = [0.1, 0.2, 0.3, 0.2, 0.1]
weighted_sum = sum(w * d for w, d in zip(dummy_weights, data_points[:5]))
penalty = weighted_sum * 0.05 if weighted_sum > 40 else 0  # Unused penalty

# Final processing with nested logic and conditional expression
def process_metrics(metrics):
    peak = max(metrics)
    avg = sum(metrics) / len(metrics)
    efficiency_ratio = (avg / peak) if peak != 0 else 0
    
    # Conditional expression usage (required Python feature)
    performance_tier = 'A' if efficiency_ratio >= 0.8 else ('B' if efficiency_ratio >= 0.6 else 'C')
    
    # Hidden key calculation
    hidden_offset = 5 if performance_tier == 'A' else (-3 if performance_tier == 'C' else 0)
    
    # Critical variable assignment
    efficiency_score = int((efficiency_ratio * 100) + hidden_offset)
    
    # Red herring: unused return components
    debug_info = {
        'raw': metrics,
        'peak': peak,
        'tier': performance_tier
    }
    
    return efficiency_score, debug_info

# Execute main logic
final_output = process_metrics(data_points)
efficiency_score = final_output[0]

# Print required result
print(f"Target result: {efficiency_score}")