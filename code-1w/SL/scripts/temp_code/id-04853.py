from itertools import combinations

# Simulate sensor data processing with noise filtering and pattern detection
def preprocess_sensors(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    sorted_vals = sorted(filtered)
    smoothed = []
    for i in range(len(sorted_vals)):
        left = sorted_vals[i-1] if i > 0 else sorted_vals[i]
        right = sorted_vals[i+1] if i < len(sorted_vals)-1 else sorted_vals[i]
        avg = (left + sorted_vals[i] + right) / 3
        smoothed.append(round(avg, 2))
    return smoothed

# Identify equilibrium point where left sum ≈ right sum
def find_equilibrium(series):
    total_sum = sum(series)
    left_accum = 0
    for idx, value in enumerate(series):
        right_sum = total_sum - left_accum - value
        if abs(left_accum - right_sum) < 1e-5:  # floating-point safe comparison
            return idx
        left_accum += value
    return -1

# Auxiliary function to generate synthetic test patterns
def generate_test_pattern(base, shift):
    result = []
    for x in base:
        result.append(x + shift)
    return result

# Main execution flow
raw_sensor_data = [5, 15, 22, 35, 48, 65, 77, 90, 95, 105, 120]
processed_data = preprocess_sensors(raw_sensor_data)

# Irrelevant transformation: generates unused combinatorial pairs
temp_pairs = list(combinations(processed_data[::2], 2))
pair_count = len(temp_pairs)
sum_placeholder = 0
for p in temp_pairs:
    sum_placeholder += p[0] * 0.1  # Distractor computation

# Simulated secondary analysis (dead code path)
if len(processed_data) > 10:
    adjusted = [x * 1.1 for x in processed_data]
else:
    adjusted = [x * 0.9 for x in processed_data]  # Not used

# Key assignment statement
equilibrium_index = find_equilibrium(processed_data)

# Print final target result
print(f"Result: {equilibrium_index}")