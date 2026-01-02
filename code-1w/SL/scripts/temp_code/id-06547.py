def analyze_growth_factor(temp, hum):
    if temp < 20 or hum < 40:
        return 0.0
    growth_index = (temp * 0.7) + (hum * 0.3)
    adjustment = 1.0
    if temp > 30:
        adjustment -= 0.15
    if hum > 80:
        adjustment -= 0.10
    return growth_index * adjustment

# Simulated sensor data from greenhouse zones
temperature_data = [22, 25, 19, 31, 28, 33, 24]
humidity_data = [45, 60, 35, 85, 70, 90, 50]

# Irrelevant baseline metrics (distractor)
baseline_temp = sum(temperature_data) / len(temperature_data)
baseline_hum = sum(humidity_data) / len(humidity_data)
avg_growth_potential = 0.0
growth_fluctuation = 0.0

# Tracking variables for debugging (partially relevant)
count_above_threshold = 0
temp_variance_sum = 0.0
reference_log = []

for i, (t, h) in enumerate(zip(temperature_data, humidity_data)):
    temp_variance_sum += (t - baseline_temp) ** 2
    zone_growth = analyze_growth_factor(t, h)
    avg_growth_potential += zone_growth
    
    # Logging for audit (semi-relevant)
    status_flag = "OK" if t >= 20 and h >= 40 else "WARN"
    reference_log.append(f"Zone {i}: {status_flag}")
    
    if zone_growth > 20.0:
        count_above_threshold += 1

# Dead code path - never executed due to data (distractor)
emergency_shutdown = False
for log_entry in reference_log:
    if "CRITICAL" in log_entry:
        emergency_shutdown = True
        break

# Secondary computation on string representations (semi-relevant distraction)
valid_zones = []
for entry in reference_log:
    if "WARN" not in entry:
        zone_num_str = entry.split(':')[0]
        zone_num = int(zone_num_str.split()[-1])
        valid_zones.append(zone_num)

# Core calculation obscured by prior noise
def calculate_optimal_yield(temps, hums):
    total_yield = 0.0
    efficiency_corrections = []
    
    for t, h in zip(temps, hums):
        base_yield = analyze_growth_factor(t, h)
        if t > 25:
            peak_bonus = 1.1 if h > 60 else 0.9
n            base_yield *= peak_bonus
        efficiency_corrections.append(base_yield * 0.95)  # Calibration
    
    for val in efficiency_corrections:
        total_yield += val
    
    return total_yield * 0.9  # Final environmental stress factor

final_yield = calculate_optimal_yield(temperature_data, humidity_data)
print(f"Result: {final_yield}")