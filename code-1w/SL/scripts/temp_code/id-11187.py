import math

# Simulated sensor data processing pipeline with red herrings
def collect_signals():
    raw = [0.7, 1.2, 3.5, 4.1, 5.0, 6.3, 7.2, 8.1, 9.0, 10.5]
    noise_floor = 3.8
    threshold = 7.0
    adjusted = [x * 1.05 for x in raw if x > noise_floor]
    return adjusted

# Irrelevant transformation - dead path
def deprecated_filter(data):
    return [x for x in data if x % 2 == 0]

# Distractor: complex but unused signal smoothing
def smooth_signal(series):
    smoothed = []
    for i in range(len(series)):
        window = series[max(0, i-2):min(i+3, len(series))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Bit manipulation decoy - looks important but unused
security_key = 0b110101
mask = 0b111000
encrypted_flag = security_key ^ mask | (mask << 2)

# Data normalization with distraction
baseline = [1.0, 2.0, 3.0]
normalized_baseline = list(map(lambda x: x ** 2, baseline))  # Unused

# Real processing starts here
sensor_readings = collect_signals()

# Misleading intermediate calculation
aggregate_power = sum([x**2 for x in sensor_readings]) / len(sensor_readings)
dummy_metric = math.log(aggregate_power + 1, 2)

# Actual relevant filtering
valid_range = [x for x in sensor_readings if x >= 6.0]

# Decoy loop with enumerate - appears analytical but unused
analysis_report = {}
for idx, val in enumerate(valid_range):
    analysis_report[idx] = {
        'value': val,
        'offset': val - 6.0,
        'flagged': val > 9.5
    }

# Critical data restructuring using zip and enumerate
indexed = list(enumerate(valid_range))
pairs = list(zip([p[1] for p in indexed[::2]], [p[1] for p in indexed[1::2]]))

# Secondary filter - only pairs where both elements exist and meet criteria
stable_pairs = [p for p in pairs if p[0] < 8.5 and p[1] > 7.5]

# Another distraction: unused recursive function
def calculate_depth(data, depth=0):
    if not data or len(data) == 1:
        return depth
    return calculate_depth(data[1:-1], depth + 1)

recursion_test = calculate_depth([1,2,3,4,5])  # Dead computation

# Core logic disguised among noise
pair_sums = [a + b for a, b in stable_pairs]
if len(pair_sums) > 0:
    avg_sum = sum(pair_sums) / len(pair_sums)
else:
    avg_sum = 0.0

# Final transformation chain
transformed = map(lambda x: x * 0.85 + 2.5, pair_sums)
correction_factor = math.sin(math.pi / 6) * 2  # = 1.0
filtered_data = [round(x * correction_factor, 3) for x in transformed]

# Final analysis function - uses the filtered data
def final_analysis(data):
    if not data:
        return -1
    total = sum(data)
    count = len(data)
    penalty = 0
    for val in data:
        if val > 10.0:
            penalty += 0.5
    return total - penalty * 2.5

# Key execution point
filtration_score = final_analysis(filtered_data)
print(f"Result: {filtration_score}")