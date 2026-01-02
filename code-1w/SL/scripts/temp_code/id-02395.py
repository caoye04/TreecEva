from collections import Counter

def calculate_efficiency(loads, thresh):
    filtered = [x for x in loads if x > thresh]
    count_map = Counter(filtered)
    total_peaks = sum(1 for x in count_map.values() if x >= 2)
    base_energy = sum(filtered) // len(filtered) if filtered else 0
    adjustment = 7 if total_peaks > 0 else 3
    return base_energy * adjustment

# System load data (in MW)
sensor_readings = [12, 15, 9, 15, 10, 14, 15, 8]
grid_loads = sensor_readings[1:6]  # Focused window of interest
threshold = 11

# Irrelevant auxiliary variables (minimal distraction)
diagnostic_mode = False
log_entries = ['init', 'calibrate', 'run']

energy_capacity = calculate_efficiency(grid_loads, threshold)

Result: {energy_capacity}