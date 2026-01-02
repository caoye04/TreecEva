def analyze_growth_cycle(data):
    peak_readings = []
    for i, row in enumerate(data):
        avg = sum(row) / len(row)
        if avg > 25:
            peak_readings.append((i, avg))
    return peak_readings

# Simulate agricultural sensor data across 7 plots over 5 days
sensors = [
    [20, 22, 23, 24, 26],
    [27, 28, 29, 30, 31],
    [15, 16, 18, 19, 20],
    [33, 35, 36, 34, 32],
    [12, 14, 13, 15, 16],
    [40, 42, 41, 43, 44],
    [18, 19, 20, 21, 22]
]

plots = ['north', 'east', 'west', 'south', 'northeast', 'northwest', 'southeast']

# Misleading preprocessing: irrelevant normalization
normalized_sensors = [[round(val * 0.95, 2) for val in row] for row in sensors]
baseline_shift = sum([sum(row) for row in normalized_sensors]) / (len(sensors) * len(sensors[0]))

# Dummy state tracking (not used in final result)
cycle_logs = {}
for idx, name in enumerate(plots):
    cycle_logs[name] = {'start': idx * 2, 'active': True}

# Core logic disguised among auxiliary operations
total_productivity = 0
efficiency_flags = []
for i, (plot_name, readings) in enumerate(zip(plots, sensors)):
    # Calculate daily growth delta (irrelevant to final answer but looks important)
    deltas = [readings[j+1] - readings[j] for j in range(len(readings)-1)]
    smooth_trend = sum(deltas) / len(deltas) if deltas else 0
    
    # Actual relevant metric: count of high-yield days
    high_yield_days = sum(1 for val in readings if val >= 30)
    plot_score = len(readings) * high_yield_days
    
    # This condition appears significant but only logs side info
    if high_yield_days >= 3:
        efficiency_flags.append(plot_name)
    
    # Only this accumulation matters
    total_productivity += plot_score

# Secondary validation using string-based plot classification
valid_prefixes = {name[:2] for name in plots if 'th' not in name}  # red herring
penalty_rate = 0.1 if len(valid_prefixes) > 2 else 0.05

# Critical computation buried after distractions
base_efficiency = total_productivity / len(plots)
adjustment_factor = len(efficiency_flags) * 1.5

# Final yield depends only on base_efficiency and adjustment_factor
final_yield = base_efficiency + adjustment_factor

# Extraneous post-processing
final_yield_rounded = round(final_yield, 4)
scaled_output = final_yield_rounded * 1.02

# Output the required variable
print(f"Result: {final_yield}")