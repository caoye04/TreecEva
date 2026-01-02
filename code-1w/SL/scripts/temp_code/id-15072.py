from collections import Counter, defaultdict

# Simulated sensor data with timestamps and readings
timestamped_data = [
    (1001, 'temp', 23.5), (1002, 'pressure', 1013.25), (1003, 'temp', 24.1),
    (1004, 'humidity', 45),   (1005, 'temp', 24.0),   (1006, 'pressure', 1012.9),
    (1007, 'temp', 24.2),     (1008, 'humidity', 47),   (1009, 'temp', 23.9),
    (1010, 'pressure', 1013.1), (1011, 'temp', 24.3),   (1012, 'humidity', 46)
]

# Extract data slice for analysis (middle portion)
data_slice = timestamped_data[3:9]

# Misleading auxiliary computation - counts unrelated categories
aux_counter = Counter(entry[1] for entry in timestamped_data)
duplicate_check = defaultdict(int)
for _, typ, _ in timestamped_data:
    duplicate_check[typ] += 1

# Spurious transformation: normalize humidity values arbitrarily
max_humidity = 100
normalized_readings = []
for ts, typ, val in data_slice:
    if typ == 'humidity':
        normalized_readings.append(val / max_humidity)

# Irrelevant smoothing attempt on subset
smoothed = []
for i in range(len(normalized_readings)):
    prev_val = normalized_readings[i-1] if i > 0 else normalized_readings[i]
    curr_val = normalized_readings[i]
    smoothed.append((prev_val + curr_val) / 2)

# Core metric: count how many times 'temp' exceeds baseline within slice
temp_baseline = 24.0
temp_readings = [val for ts, typ, val in data_slice if typ == 'temp']
above_threshold_count = sum(1 for t in temp_readings if t > temp_baseline)

# Secondary metric: pressure stability (ignored later)
pressure_vals = [val for ts, typ, val in data_slice if typ == 'pressure']
pressure_variance = sum((p - 1013.0) ** 2 for p in pressure_vals)

# Define evaluation function
def evaluate_performance(data_part, criteria):
    # criteria is ignored; red herring parameter
    temperatures = [val for ts, typ, val in data_part if typ == 'temp']
    avg_temp = sum(temperatures) / len(temperatures)
    stable_run = 0
    current_run = 0
    for t in sorted(temperatures):  # sorting has no real impact but adds distraction
        if t >= 24.0:
            current_run += 1
        else:
            stable_run = max(stable_run, current_run)
            current_run = 0
    stable_run = max(stable_run, current_run)
    
    # Actual logic contributing to answer
    score_component_1 = int(avg_temp * 10)
    score_component_2 = above_threshold_count * 5
    return score_component_1 + score_component_2

# Metrics dictionary — unused but present as distraction
metrics = {
    'sensitivity': 0.95,
    'tolerance': 0.1,
    'weighting': 'linear'
}

# Key execution point
final_score = evaluate_performance(data_slice, metrics)

print(f"Result: {final_score}")