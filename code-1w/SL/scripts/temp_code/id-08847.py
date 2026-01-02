from itertools import cycle

# Simulate a geothermal energy grid with fluctuating input and phase adjustments
base_temperatures = [120, 135, 140, 130, 125]
flow_rates = [85, 90, 88, 92, 87]
diagnostic_logs = []

# Irrelevant auxiliary computation: system health score (not used in final result)
system_health = sum([abs(base_temperatures[i] - flow_rates[i]) for i in range(len(base_temperatures))]) // 5

# Misleading data transformation
adjusted_temps = [t * 0.95 + 5 for t in base_temperatures]
buffer_levels = list(map(lambda x: x * 1.1, adjusted_temps))  # Dead-end calculation

# Core process: build grid flow with cycling inputs
grid_flow = [base_temperatures[i] * flow_rates[i] for i in range(5)]
phase_shift = sum([grid_flow[i] % (i + 2) for i in range(5)])

# Secondary distraction: simulate sensor drift compensation (unused)
sensor_drift = 0.0
for i in range(3):
    for j in range(2):
        sensor_drift += (adjusted_temps[j] - buffer_levels[i]) / 100

# Helper function to compute thermal output based on effective flow and phase
def calculate_thermal_output(flow, phase):
    accumulator = 0
    phase_cycle = cycle([1, -1, 0])
    
    for idx, value in enumerate(flow):
        adjustment = next(phase_cycle)
        # Only even indices contribute meaningfully
        if idx % 2 == 0:
            intermediate = value + (phase * adjustment)
            accumulator += intermediate // (idx + 1) if idx > 0 else intermediate
    
    # Distractor: unused internal metric
    efficiency_ratio = accumulator / (sum(flow) + 1)
    return int(accumulator)

# Key statement
thermal_capacity = calculate_thermal_output(grid_flow, phase_shift)

# Final output
print(f"Result: {thermal_capacity}")