from collections import deque, Counter

# Simulate time-series energy load analysis with noise filtering
def analyze_grid_stability(load_profile):
    filtered_loads = []
    noise_counter = Counter()
    
    for i, load in enumerate(load_profile):
        if abs(load - (sum(load_profile) / len(load_profile))) > 2 * (max(load_profile) - min(load_profile)) / 3:
            noise_counter['outliers'] += 1
            continue
        filtered_loads.append(load)

    # Misleading transformation: frequency domain distraction
    spectral_peak = 0
    for i in range(len(filtered_loads)):
        phase = 0
        for j in range(0, len(filtered_loads), 2):
            phase ^= int(filtered_loads[min(j, len(filtered_loads) - 1)])
        spectral_peak += phase % 10

    # Real processing: rolling window analysis
    window_size = 3
    rolling_loads = []
    temp_window = deque(maxlen=window_size)
    
    for load in filtered_loads:
        temp_window.append(load * 0.85 + 0.15 * (load * 0.5 + load * 0.5))  # Weighted inclusion
        if len(temp_window) == window_size:
            avg_load = sum(temp_window) / window_size
            rolling_loads.append(round(avg_load, 3))

    # Add dummy entries to mislead temporal reasoning
    rolling_loads.insert(0, rolling_loads[0] * 0.9)
    rolling_loads.append(rolling_loads[-1] * 1.1)

    # Critical statement
    peak_capacity = max(rolling_loads)

    # Irrelevant post-processing
    capacity_margin = 1.2
    projected_growth = [x * capacity_margin for x in rolling_loads]
    growth_entropy = 0
    for g in projected_growth:
        if g > peak_capacity:
            growth_entropy += g % (peak_capacity + 1)

    return peak_capacity

# Input data: hourly energy consumption (MW)
raw_load_data = [120, 125, 130, 90, 135, 140, 110, 145, 150, 138, 132, 128]

# Execute analysis
result = analyze_grid_stability(raw_load_data)
print(f"Result: {result}")