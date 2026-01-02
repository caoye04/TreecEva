def analyze_temperatures(temp_data):
    avg_temp = sum(temp_data) / len(temp_data)
    high_count = sum(1 for t in temp_data if t > avg_temp)
    low_count = sum(1 for t in temp_data if t < avg_temp)
    balance_factor = (high_count - low_count) * 0.5
    return avg_temp, balance_factor

# Simulate sensor data drift correction
drift_compensation = lambda x: [val + 0.1 for val in x]
raw_readings = [23.5, 24.1, 22.9, 25.3, 23.8, 24.7, 22.6]
adjusted_readings = drift_compensation(raw_readings)

# Noise filtering with moving average
filtered_readings = []
for i in range(1, len(adjusted_readings)-1):
    window_avg = (adjusted_readings[i-1] + adjusted_readings[i] + adjusted_readings[i+1]) / 3
    filtered_readings.append(window_avg)

# Extraneous computation - simulate failed calibration attempt
calibration_matrix = [[1.01, -0.02], [0.99, 0.01]]
misaligned_sum = sum(sum(row) for row in calibration_matrix)  # Unused variable

# Analyze the filtered temperature data
mean_temp, bias = analyze_temperatures(filtered_readings)

data = list(enumerate(zip(filtered_readings, [r * 1.1 for r in raw_readings[1:-1]])))

# Weighting logic for system health score
def calculate_weight(index, value):
    if index % 2 == 0:
        return value * 1.2
    else:
        return value * 0.8

temp_dict = {i: calculate_weight(i, v[0]) for i, v in data}

# Calculate final composite score
base_score = sum(temp_dict.values())
penalty = len([v for v in temp_dict.values() if v < mean_temp]) * 1.5
bonus = bias * 2 if bias > 0 else 0
final_score = base_score + bonus - penalty

# Irrelevant debugging output
debug_info = {"count": len(temp_dict), "min_val": min(temp_dict.values()), "extra_flag": False}

# Red herring calculation
temporary_accumulator = 0
for k, v in temp_dict.items():
    temporary_accumulator += k * (v % 3)

Result: final_score