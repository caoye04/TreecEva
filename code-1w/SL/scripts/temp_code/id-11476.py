from collections import defaultdict

# Simulate sensor data with some noise
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.2, 23.6]
humidity_readings = [45, 47, 50, 44, 46, 48, 45]
pressure_readings = [1013, 1012, 1015, 1011, 1014, 1013, 1012]

# Misleading variable - not used in final computation
dummy_aggregate = sum([t * h for t, h in zip(temperature_readings, humidity_readings)])

# Preprocess: normalize temperature relative to baseline
def normalize_temperatures(readings, baseline=20.0):
    return [(temp - baseline) for temp in readings]

normalized_temps = normalize_temperatures(temperature_readings)

# Track state across time steps using defaultdict
state_tracker = defaultdict(int)
for i, temp in enumerate(normalized_temps):
    if temp > 3:
        state_tracker['high'] += 1
    elif temp > 2:
        state_tracker['moderate'] += 1
    else:
        state_tracker['low'] += 1

# Compute rolling average over 3-day window (irrelevant but plausible)
rolling_averages = [
    sum(normalized_temps[i:i+3]) / 3 for i in range(len(normalized_temps) - 2)
]

# Destructuring assignment - partially relevant
first_avg, second_avg, *remaining_avgs = rolling_averages

# Simulate data quality flags (distraction)
quality_flags = []
for h, p in zip(humidity_readings, pressure_readings):
    if h < 46 and p < 1013:
        quality_flags.append('YELLOW')
    elif h > 48 or p > 1014:
        quality_flags.append('RED')
    else:
        quality_flags.append('GREEN')

# Process data: focus on normalized temp trend and stability
processed_data = {
    'stable_days': len([t for t in normalized_temps if 2 <= t <= 4]),
    'peak_deviation': max(normalized_temps) - min(normalized_temps),
    'duration': len(normalized_temps),
    'warning_count': state_tracker['high']
}

# Extra distraction: unused helper function
def predict_trend(data):
    if len(data) < 2:
        return 0
    return (data[-1] - data[0]) / len(data)

# Main scoring logic
def calculate_final_score(data):
    base_score = data['stable_days'] * 10
    penalty = 0
    
    if data['peak_deviation'] > 3.0:
        penalty += 15
    if data['warning_count'] >= 2:
        penalty += 10
    
    # Bonus for longer duration
    if data['duration'] >= 7:
        base_score += 5
    
    return base_score - penalty

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")