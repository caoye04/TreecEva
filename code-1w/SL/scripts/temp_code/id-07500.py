def calculate_thermal_output(energy, efficiency):
    base_output = energy * efficiency
    adjustment_factor = 1.0 if energy > 500 else 0.85
    decay_rate = 0.95
    transient_loss = 12.5

    # Simulate intermediate heat dissipation cycles (distractor computations)
    cycle_count = 0
    temp_buffer = base_output
    while temp_buffer > 100 and cycle_count < 3:
        temp_buffer *= decay_rate
        cycle_count += 1

    # Unrelated diagnostic metrics (dead computation - distractor)
    diagnostic_score = (temp_buffer / base_output) * 100 if base_output != 0 else 0
    normalization_constant = 2.718  # Unused in final logic

    # Actual relevant computation path
    adjusted_output = base_output * adjustment_factor - transient_loss
    return adjusted_output

# System initialization parameters
energy_reserves = 720
efficiency_factor = 0.92
ambient_stability = 0.987  # Misleading environmental variable
baseline_threshold = 650     # Not used beyond comparison

# Auxiliary tracking variables (irrelevant to final result)
monitoring_log = []
time_step = 0
for t in range(2):
    time_step += 1
    status_flag = "STABLE" if energy_reserves > baseline_threshold else "CAUTION"
    monitoring_log.append(f"{status_flag}-{time_step}")

# Core computation with conditional expression
system_mode = "high_throughput" if energy_reserves > 600 else "standard"
boost_multiplier = 1.1 if system_mode == "high_throughput" else 1.0  # Defined but not used

# Key assignment statement
thermal_capacity = calculate_thermal_output(energy_reserves, efficiency_factor)

# Print final result as required
print(f"Result: {thermal_capacity}")