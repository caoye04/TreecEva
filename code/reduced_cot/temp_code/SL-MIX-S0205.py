import statistics

def compute_variance_window(temps, start, end):
    window = temps[start:end+1]
    return statistics.variance(window)

def find_stable_period(temps, threshold):
    sorted_temps = sorted(enumerate(temps), key=lambda x: x[1])
    low, high = 0, len(sorted_temps) - 1
    while low <= high:
        mid = (low + high) // 2
        idx, temp = sorted_temps[mid]
        left_bound = max(0, idx - 2)
        right_bound = min(len(temps) - 1, idx + 2)
        var = compute_variance_window(temps, left_bound, right_bound)
        if var < threshold:
            return idx, var
        elif temp < temps[idx]:
            low = mid + 1
        else:
            high = mid - 1
    return -1, float('inf')

temperature_readings = [23.5, 24.1, 23.8, 24.0, 23.9, 24.2, 23.7, 24.3, 23.6, 24.4]
sensor_indices = list(range(len(temperature_readings)))
stability_threshold = 0.05

# Compute initial stability metrics
window_variances = {i: compute_variance_window(temperature_readings, max(0, i-1), min(len(temperature_readings)-1, i+1)) for i in sensor_indices}

# Identify stable regions using binary search
stable_positions = {}
for idx in sensor_indices:
    pos, var = find_stable_period(temperature_readings, stability_threshold * (idx + 1))
    if pos != -1:
        stable_positions[pos] = var

# Calculate overall stability index
if stable_positions:
    stability_index = sum(stable_positions.values()) / len(stable_positions)
else:
    stability_index = 0.0

# Adjust for sensor distribution skew
unique_variances = set(window_variances.values())
if len(unique_variances) > 1:
    stability_index *= len(unique_variances) / len(window_variances)

print(f"Result: {stability_index}")