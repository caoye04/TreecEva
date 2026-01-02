from itertools import accumulate, cycle

# Simulate thermal processing stages in a chemical reactor
def generate_stage_temperatures(base_temp, cycles):
    temps = []
    for i, c in zip(range(cycles), cycle([1.1, 0.9, 1.05])):
        base_temp *= c
        temps.append(round(base_temp, 2))
    return temps

def assess_stability_metric(temps):
    diffs = [abs(temps[i] - temps[i-1]) for i in range(1, len(temps))]
    return sum(diffs) / len(diffs) if diffs else 0

def calculate_thermal_output(stages):
    # Irrelevant tracking variables (distractors)
    peak_moment = None
    cumulative_drift = 0
    adjustment_log = []
    
    temp_profile = generate_stage_temperatures(200, stages)
    stability = assess_stability_metric(temp_profile)
    
    # Simulate non-linear response with accumulation
    power_ramp = [t**1.08 for t in temp_profile]
    energy_accumulation = list(accumulate(power_ramp))
    
    # Dead code path - never affects final result
    if len(temp_profile) > 10:
        smoothing_factor = 0.85
        filtered = [x * smoothing_factor for x in energy_accumulation]
        cumulative_drift += sum(filtered)
    
    # Key intermediate transformation
    scaled_output = [x * 0.76 for x in energy_accumulation if x > 300]
    
    # More distractors: unused analysis
    peak_moment = max(enumerate(scaled_output), key=lambda x: x[1])[0] if scaled_output else 0
    adjustment_log.append('baseline_set')
    
    # Core logic: average of last three accumulated values, adjusted by stability
    relevant_accum = energy_accumulation[-3:] if len(energy_accumulation) >= 3 else [0]
    raw_avg = sum(relevant_accum) / len(relevant_accum)
    
    # Final computation - depends on raw_avg and stability
    thermal_output = int(raw_avg - (stability * 12.4))
    
    # Critical assignment
    thermal_capacity = thermal_output
    return thermal_capacity

# Auxiliary monitoring function (not used in main flow)
def log_reactor_state(state_code, timestamp=None):
    if timestamp is None:
        from time import time
        timestamp = time() % 1000
    return f"[{timestamp:.2f}] REACTOR_{state_code}"

# Setup and execution
process_stages = 8
monitoring_interval = 15  # Unused parameter
baseline_threshold = 195.5  # Semi-relevant but not directly used

# Execute main calculation
thermal_capacity = calculate_thermal_output(process_stages)

# Print result as required
print(f"Result: {thermal_capacity}")