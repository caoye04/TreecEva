from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, [23.5, 24.1, 22.9]),
    (105, [25.0, None, 24.3]),
    (110, [23.8, 24.0, 24.7]),
    (115, [None, 23.9, 24.2]),
    (120, [24.5, 24.6, None])
]

# Misleading: energy consumption not used in final logic
total_energy_used = 0.0
energy_per_reading = 0.023
for ts, vals in timestamped_readings:
    valid_count = len([v for v in vals if v is not None])
    total_energy_used += valid_count * energy_per_reading

# Process data: clean, normalize, and aggregate
cleaned_data = []
invalid_count = 0
for ts, readings in timestamped_readings:
    filtered = [r for r in readings if r is not None]  # Remove nulls
    if filtered:
        avg = sum(filtered) / len(filtered)
        cleaned_data.append((ts, avg))
    else:
        invalid_count += 1

# Compute time-weighted average temperature
weighted_sum = 0.0
total_weight = 0
for i in range(1, len(cleaned_data)):
    prev_ts, prev_avg = cleaned_data[i-1]
    curr_ts, curr_avg = cleaned_data[i]
    delta_t = curr_ts - prev_ts
    # Weight by duration between readings
    weighted_sum += prev_avg * delta_t
    total_weight += delta_t

# Add last interval manually to complete integration
if cleaned_data:
    last_ts, last_avg = cleaned_data[-1]
    weighted_sum += last_avg * 5  # Assume final 5-unit interval
    total_weight += 5

time_weighted_avg = weighted_sum / total_weight if total_weight > 0 else 0

# Distractor variables: unrelated statistical measures
peak_fluctuation = max([abs(a-b) for (_, a), (_, b) in zip(cleaned_data, cleaned_data[1:])], default=0)
avg_temperature = sum(avg for _, avg in cleaned_data) / len(cleaned_data)
median_temp = sorted([avg for _, avg in cleaned_data])[len(cleaned_data)//2]

# Prepare feature vector using list comprehension and slicing
temp_sequence = [t for _, t in cleaned_data]
windowed_features = [
    {
        'mean': sum(temp_sequence[i:i+3]) / len(temp_sequence[i:i+3]),
        'trend': temp_sequence[i+2] - temp_sequence[i] if i+2 < len(temp_sequence) else 0,
        'stable': abs(temp_sequence[i+2] - temp_sequence[i]) < 0.5 if i+2 < len(temp_sequence) else True
    }
    for i in range(0, len(temp_sequence), 2)
]

# State tracking via defaultdict (used in calculation)
state_summary = defaultdict(int)
for feature in windowed_features:
    state_summary['stable_periods'] += 1 if feature['stable'] else 0
    state_summary['total_periods'] += 1

# Core scoring logic based on stability ratio and time-weighted average
def calculate_stability_score(summary):
    if summary['total_periods'] == 0:
        return 0
    return (summary['stable_periods'] / summary['total_periods']) * 100

def calculate_base_score(twa):
    return max(0, min(100, (twa - 20) * 10))  # Map 20->0, 30->100

def calculate_final_score(data):
    base = calculate_base_score(time_weighted_avg)
    stability = calculate_stability_score(state_summary)
    # Final score is harmonic mean of base and stability
    if base + stability == 0:
        return 0
    return (2 * base * stability) / (base + stability)

final_score = calculate_final_score(processed_data=None)
print(f"Result: {final_score}")