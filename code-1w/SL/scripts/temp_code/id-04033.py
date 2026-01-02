def analyze_temperature_patterns(data, threshold=25):
    high_temp_days = []
    temp_sum = 0
    day_count = 0
    anomaly_flags = []

    for i, temp in enumerate(data):
        if temp > threshold:
            high_temp_days.append(i)
            temp_sum += temp
            day_count += 1
        else:
            moving_avg = sum(data[max(0, i-2):i+1]) / (i+1) if i > 0 else temp
            if moving_avg < 18:
                anomaly_flags.append((i, round(moving_avg, 2)))

    avg_high_temp = temp_sum / day_count if day_count > 0 else 0
    return high_temp_days, avg_high_temp, anomaly_flags


def transform_readings(raw_readings):
    normalized = [round((r - 10) * 1.8, 2) for r in raw_readings]
    inverted = [100 - n for n in normalized]
    paired = list(zip(normalized, inverted))
    filtered = [p for p in paired if p[0] > 20]
    return filtered

# Simulated sensor data from environmental monitoring station
temperature_data = [22, 26, 30, 19, 27, 33, 24, 28, 17, 31]

# Irrelevant auxiliary computation (distractor)
power_levels = [t ** 0.5 * 2.1 for t in temperature_data]
efficiency_ratios = [round((p + 5) / 10, 3) for p in power_levels]

# Primary processing pipeline
processed_data = transform_readings(temperature_data)
high_days, mean_peak, anomalies = analyze_temperature_patterns(temperature_data)

# State tracking with misleading intermediate variables
current_state = {'phase': 'analysis', 'version': '2.1', 'active': True}
state_history = []
for _ in range(3):
    state_history.append(current_state.copy())

# Core logic disguised among semi-relevant operations
total_base_score = sum(t for t in temperature_data if t >= 24)
discount_factor = len(anomalies) * 0.5 if anomalies else 0.1

adjusted_components = []
for idx, val in enumerate([item[0] for item in processed_data]):
    if idx % 2 == 0:
        adjusted_components.append(val * 1.1)
    else:
        adjusted_components.append(val * 0.9)

component_offset = sum(1 for x in adjusted_components if x > 25)

# Critical execution point
final_score = calculate_adjusted_score(processed_data)

# Supporting function defined after use (adds cognitive load)
def calculate_adjusted_score(cleaned_data):
    base = sum(cd[0] for cd in cleaned_data)
    bonus = len(cleaned_data) * 2.5
    penalty = component_offset * 1.5  # Uses outer-scope variable
    return int(base + bonus - penalty)

print(f"Result: {final_score}")