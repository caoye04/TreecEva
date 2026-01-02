from collections import defaultdict
import itertools

# Simulate sensor data with noise and redundant readings
data_stream = [
    (1, 'temp', 23.5), (2, 'temp', 24.1), (3, 'pressure', 1013), (4, 'temp', 23.9),
    (5, 'humidity', 45), (6, 'pressure', 1012), (7, 'temp', 24.0), (8, 'humidity', 47),
    (9, 'pressure', 1015), (10, 'temp', 24.2)
]

# Misleading variable - looks important but unused in final logic
baseline_calibration = {'temp': 22.0, 'pressure': 1000, 'humidity': 50}
redundant_aggregates = []

# Process raw data into grouped structure
grouped_data = defaultdict(list)
for seq_id, sensor_type, reading in data_stream:
    grouped_data[sensor_type].append(reading)
    if reading > 100:  # Only pressure exceeds 100, this creates misleading branching
        redundant_aggregates.append(seq_id * 0.1)  # Distractor computation

# Extract only temperature for thermal analysis
temp_readings = grouped_data['temp']

# Unnecessary intermediate transformation - distracts from core logic
temp_deltas = [round(b - a, 2) for a, b in zip(temp_readings, temp_readings[1:])]

# Simulate gap-filling for missing data (no gaps here - adds distraction)
synthetic_fill = []
for i in range(len(temp_readings) - 1):
    if temp_deltas[i] > 0.3:
        synthetic_fill.append((temp_readings[i] + temp_readings[i+1]) / 2)

# Augment original data with synthetic values (but none are actually added)
expanded_temps = temp_readings.copy()
expanded_temps.extend(synthetic_fill)

# Statistical summary with irrelevant precision
mean_temp = sum(expanded_temps) / len(expanded_temps)
variance_proxy = sum((t - mean_temp) ** 2 for t in expanded_temps) / len(expanded_temps)
adjusted_mean = round(mean_temp + 0.1 * (variance_proxy > 0.1), 2)

# Weight assignment using itertools.cycle to create artificial complexity
cycle_weights = list(itertools.islice(itertools.cycle([0.8, 0.9, 1.0]), len(expanded_temps)))
weighted_sum = sum(t * w for t, w in zip(expanded_temps, cycle_weights))
normalized_sum = weighted_sum / sum(cycle_weights)

# Secondary processing chain on pressure (never used later)
pressure_readings = grouped_data['pressure']
pressure_change_rate = [(b - a) for a, b in zip(pressure_readings, pressure_readings[1:])]
pressure_trend = sum(pressure_change_rate)

# Core scoring logic - depends only on adjusted_mean and normalized_sum
def calculate_base_score(value):
    return max(0, (value - 20) * 5)

def apply_bonus(score, threshold=24.0):
    return score * 1.1 if adjusted_mean >= threshold else score

def calculate_final_score(processed_data):
    base = calculate_base_score(normalized_sum)
    bonus_applied = apply_bonus(base)
    penalty = 5 if variance_proxy < 0.05 else 0
    return int(bonus_applied - penalty)

# Key execution point
final_score = calculate_final_score(processed_data=None)
print(f"Result: {final_score}")