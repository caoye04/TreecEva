def analyze_growth_potential(temp, moist):
    if temp < 20 or temp > 35:
        return False
    if moist < 40 or moist > 80:
        return False
    return True

# Sensor data from greenhouse zones
temperature_readings = [18, 24, 31, 36, 27]
moisture_levels = [35, 60, 75, 85, 55]
status_codes = [200, 404, 500, 200, 200]  # Irrelevant diagnostic codes

# Tracking valid growth windows
valid_periods = 0
peak_moisture = max(moisture_levels)  # Distractor: not used in final result
baseline_temp = sum(temperature_readings) / len(temperature_readings)  # Semi-relevant

for i, (temp, moist) in enumerate(zip(temperature_readings, moisture_levels)):
    if analyze_growth_potential(temp, moist):
        valid_periods += 1

# Auxiliary calculation with red herring variables
adjustment_factor = 0.0
if valid_periods >= 2:
    adjustment_factor = 1.2  # Unused in critical path
else:
    adjustment_factor = 0.8

# Simulate equipment lag (irrelevant loop)
latency_buffer = []
for _ in range(3):
    latency_buffer.append(0)

# Core yield model
def calculate_optimal_yield(temps, moistures):
    yield_score = 0
    for idx, (t, m) in enumerate(zip(temps, moistures)):
        # Only valid conditions contribute
        if 20 <= t <= 35 and 40 <= m <= 80:
            contribution = (t - 19) * (m / 100)
            yield_score += contribution
    # Apply fixed efficiency rate
    final_score = yield_score * 1.6
    return round(final_score, 4)

# Critical execution point
final_yield = calculate_optimal_yield(temperature_readings, moisture_levels)

# Diagnostic print (not affecting logic)
diagnostic_mode = False
if diagnostic_mode:
    print(f"Valid periods: {valid_periods}")

print(f"Result: {final_yield}")